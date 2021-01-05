from __future__ import print_function
import sys
import pickle
import os.path
import urllib.request
from collections import OrderedDict
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from mdutils.mdutils import MdUtils
import re
import argparse

'''
To get the credentials.json file go here "https://developers.google.com/docs/api/quickstart/js" click on
"Create API key" and follow the instructions
'''

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']


# TODO strikethrough, links with titles are broken

# '1L1vU0YWf1PjVMc7LL_nFTA0lApuC4hlVgjztXQ-MLSU'
# '16U5sLssOMuG8X8GF-qIo7VXW9BQJ_E0QIz6C5CzP7t0'
# '1XkBuOBcy4g69mRGiHzLAFff_qDwadPKogV3E-lnNcgc' primary file


def starts_or_ends_with_space(text):
    starts_with_space = False
    ends_with_space = False

    if re.match(r'\s', text):
        starts_with_space = True
    if text.endswith(' '):
        ends_with_space = True

    return [starts_with_space, ends_with_space]


def get_emphasis_values(text_run):
    """

    :param text_run: The google doc text_run attribute
    :return: First item is a string of the "bi" format which indicates if the text is bold or italic,
    Second item is a boolean which indicates if the text is strikethrough
    """
    try:
        is_bold = text_run.get('textStyle').get('bold')
        is_italic = text_run.get('textStyle').get('italic')
        is_strikethrough = text_run.get('textStyle').get('strikethrough')
    except AttributeError:
        is_italic = False
        is_bold = False
        is_strikethrough = False
    bold_italics_code = ''
    if is_bold:
        bold_italics_code = bold_italics_code + 'b'
    if is_italic:
        bold_italics_code = bold_italics_code + 'i'

    return [bold_italics_code, is_strikethrough]


def get_md(text_run):
    """

    :param text_run: The google doc text_run attribute
    :param bold_italics: "i" to get italics, "b" to get bold or "bi" to get both
    :return: Markdown text
    """

    [bold_italics, is_strikethrough] = get_emphasis_values(text_run)
    text = text_run.get('content')
    if text.strip() == "":
        return ""

    [starts_with_space, ends_with_space] = starts_or_ends_with_space(text)

    if "i" in bold_italics:
        text = "*" + text.rstrip() + "*"
    if "b" in bold_italics:
        text = "**" + text.rstrip() + "**"

    if starts_with_space:
        text = " " + text

    if ends_with_space:
        text = text + " "

    return text


def is_heading(paragraph):
    """

    :param paragraph: Accepts a google doc paragraph element
    :return: The number of the heading found in the paragraph element, for example "h2" return 2, "h4" returns 4
    """
    named_style_type = paragraph.get('paragraphStyle').get('namedStyleType')
    if 'HEADING' in named_style_type:
        return int(re.search(r'[-+]?[0-9]+', named_style_type)[0])
    return 0


def render_table(mdFile, table):
    """

    :param mdFile: The markdown file we will be writing to
    :param table: Accepts a google doc table element
    :return: Writes the table to the as markdown to the mdFile
    """
    cols = table.get('columns')
    rows = table.get('rows')
    list_of_rows = []
    for row in table.get('tableRows'):
        for cell in row.get('tableCells'):
            row_items = []
            cell_content = None
            for count, content in enumerate(cell.get('content')):
                if content.get('paragraph'):
                    for element in content.get('paragraph', {}).get('elements'):
                        if element.get('textRun'):
                            element_content = element.get('textRun').get('content')
                            if '\n' in element_content and count!=len(cell.get('content')):
                                element_content = element_content.replace('\n', ' ')
                            if not cell_content:
                                cell_content = element_content
                            else:
                                cell_content += element_content
            row_items.append(cell_content.rstrip('\n'))
            list_of_rows.extend(row_items)
    mdFile.new_table(columns=cols, rows=rows, text=list_of_rows, text_align='center')


def get_ordered_footnotes(document):
    """

    :param document: Accepts the google doc document
    :return: An order variable which contains a sorted list with "footnoteId" and "footnoteNumber" values
    """
    order = []
    for item in document['body']['content']:
        if item.get('paragraph'):
            if item.get('paragraph').get('bullet'):
                for element in item.get('paragraph').get('elements'):
                    if element.get('footnoteReference', {}).get('footnoteNumber'):
                        footnoteReference = element.get('footnoteReference')
                        order.append({'id': footnoteReference['footnoteId'],
                                      'index': footnoteReference['footnoteNumber']})
            else:
                for element in item.get('paragraph').get('elements'):
                    if element.get('footnoteReference'):
                        footnoteReference = element.get('footnoteReference')
                        order.append({'id': footnoteReference['footnoteId'],
                                      'index': footnoteReference['footnoteNumber']})
    return order


def get_element_formatting(mdFile, index, document, item, content_length, element, static_path, unify_content=False):
    """

    :param static_path: The static path the images will be sent to (defaults to '../docs/_static/img/')
    :param mdFile: The mdFile we will be writing to
    :param index: The index of the current element
    :param document: The google doc
    :param item: A document['body']['content'] item
    :param content_length: The length of document['body']['content']
    :param element: A "paragraph" element
    :param unify_content: Use this to strip the newlines at the end of the content
    :return: Writes the formatted element to the mdFile
    """
    if item.get('paragraph', {}).get('paragraphStyle', {}):
        headingId = item.get('paragraph', {}).get('paragraphStyle', {}).get('headingId')
        if headingId:
            mdFile.write(f"[]({headingId})")

    # search for images
    if element.get('inlineObjectElement'):
        inline_object = document.get('inlineObjects'). \
            get(element.get('inlineObjectElement').get('inlineObjectId'))
        object_properties = inline_object.get('inlineObjectProperties').get('embeddedObject')
        image_path = object_properties.get('imageProperties').get('contentUri')
        urllib.request.urlretrieve(image_path,
                                   filename=f"${static_path}{image_path.split('/')[-1]}.jpg")

        mdFile.new_line(mdFile.new_inline_image(text='image',
                                                path=f"${static_path}{image_path.split('/')[-1]}.jpg"))

        # add an empty character to prevent image collision with text
        mdFile.write(' ')

    if element.get('footnoteReference'):
        footnoteReference = element.get('footnoteReference')
        mdFile.write(f"[{footnoteReference['footnoteNumber']}](#{footnoteReference['footnoteId']})")

    # search for text elements
    if element.get('textRun'):
        text_run = element.get('textRun')
        is_section_link = True if text_run.get("textStyle", {}).get('link', {}).get('bookmarkId') or \
                                  text_run.get("textStyle", {}).get('link', {}).get('headingId') else False

        is_regular_link = True if text_run.get("textStyle", {}).get('link', {}).get('url') else False
        content = text_run.get('content')

        # this is used for the references table at the bottom
        # sometimes there are multiple "content" values which end with a newline
        # we should strip the newline at all the values except the last one or else
        # a reference will be skipped
        if unify_content and index != content_length - 1:
            content = content.rstrip('\n')
        if is_section_link:
            link_to = content.replace(" ", "-").lower()
            content = f"[{content}](#{link_to})"

        if is_regular_link:
            url = text_run.get("textStyle", {}).get('link', {}).get('url')
            content = f"[{content}]({url})"
        # escape starting strings like "n." where n is any number to prevent breaking md format
        for match in re.finditer(r'^[-+]?[0-9]+\.', content):
            content = content[:match.start() + 1] + '\\' + content[match.start() + 1:]

        # managing some edge cases for now
        # until a solution is found for every case

        if content.replace(' ', '') == '\n':  # using strip() removes \n as well
            mdFile.new_line()
            return
        if content == ' ':
            mdFile.write(' ')
            return

        bold_italics_code, is_strikethrough = get_emphasis_values(text_run)

        # find newlines in text
        add_new_line = False
        if '\n' in content:
            add_new_line = True

        # find if text starts or ends with space or tab
        [starts_with_space, ends_with_space] = starts_or_ends_with_space(content)

        # add the white space before any formatting to prevent breaking the format
        if starts_with_space:
            mdFile.write(' ')

        # if these conditions meet we should transform the text to a header
        _is_heading = is_heading(item.get('paragraph'))
        if _is_heading:
            mdFile.new_header(level=_is_heading, title=content.rstrip('\n').strip(),
                              add_table_of_contents='n')
        # else just write plain text
        else:
            stripped_content = content.rstrip('\n').strip()

            if is_strikethrough:
                stripped_content = f"~~{stripped_content}~~"
            mdFile.write(stripped_content,
                         bold_italics_code=bold_italics_code)

        # add them after all formatting
        if ends_with_space:
            mdFile.write(' ')
        if add_new_line:
            mdFile.write('\n')
            mdFile.new_line()


def get_formatting(mdFile, index, document, item, content_length, static_path, unify_content=False):
    """
    :param static_path: The static path the images will be sent to (defaults to '../docs/_static/img/')
    :param mdFile: The mdFile we will be writing to
    :param index: The index of the current element
    :param document: The google doc
    :param item: A document['body']['content'] item
    :param content_length: The length of document['body']['content']
    :param unify_content: Use this to strip the newlines at the end of the content
    :return: Writes the formatted element to the mdFile
    """
    # TODO: Check the "OHDSI Network" and fix broken formatting (This case might need manual fixing after
    #  the md is actually generated)
    if item.get('table'):
        render_table(mdFile, item.get('table'))
    if item.get('paragraph'):
        if item.get('paragraph').get('bullet'):
            bullet_point = ''
            # don't currently use this, until I understand how gdocs handles ordered lists
            is_ordered = False
            for element in item.get('paragraph').get('elements'):
                if element.get('footnoteReference', {}).get('footnoteNumber'):
                    footnoteReference = element.get('footnoteReference')
                    mdFile.write(f"[{footnoteReference['footnoteNumber']}](#{footnoteReference['footnoteId']})")
                else:
                    content = get_md(element.get('textRun'))
                    bullet_point = bullet_point + content

            ordering_separator = f"{is_ordered} " if is_ordered else '- '
            # apply 2 spaces per nesting level
            nesting_level = item.get('paragraph').get('bullet').get('nestingLevel')
            spacing = ''
            if nesting_level:
                spacing = (int(nesting_level)) * 2 * ' '
            mdFile.write(spacing + ordering_separator + bullet_point)

            # check next item, if it is not a bullet point then add a new line so the next item does not
            # collide with the last bullet point
            try:
                if document['body']['content'][index + 1]:
                    if not document['body']['content'][index + 1].get('paragraph', {}).get('bullet'):
                        mdFile.new_line()
            except IndexError:
                pass

        else:
            for element in item.get('paragraph').get('elements'):
                get_element_formatting(mdFile, index, document, item, content_length,
                                       element, static_path, unify_content)

        # add a space between each element
        spacing = item.get('paragraph').get('paragraphStyle').get('lineSpacing')
        if spacing:
            mdFile.write((int(spacing) // 100) * '\n')
        else:
            pass


def main():
    """

    :return: Call this with an optional arg which corresponds to the google doc id
    """
    # The ID of a sample document.
    # https://docs.google.com/document/d/1tS1nIgpFi9LKM3LgJodtQvMuN_z4uqdq1JZkjqRIq_0
    DOCUMENT_ID = '1tS1nIgpFi9LKM3LgJodtQvMuN_z4uqdq1JZkjqRIq_0'

    my_parser = argparse.ArgumentParser(description='''Converts google docs directly to markdown.
                                                    You can export the output to a folder rendered by sphinx.
                                                    In order for this script to be able to run you need to get your credentials.json 
                                                    file. To get the credentials.json file go here 
                                                    "https://developers.google.com/docs/api/quickstart/js" click on 
                                                    "Create API key" and follow the instructions. Then place the credentias.json file
                                                    in the "scripts folder" where gdoc2md.py is contained.'''
                                                )

    my_parser._action_groups.pop()

    required = my_parser.add_argument_group('required arguments (you can use either of the two arguments)')
    optional = my_parser.add_argument_group('optional arguments')

    required.add_argument('--id', action='store', type=str, help='You can use a google doc id directly, or use the --url argument')
    required.add_argument('--url', action='store', type=str, help="Enter the google doc url. (Open the google doc "
                                                                    "at your browser and copy the url e.g. "
                                                                    "https://docs.google.com/document/d/"
                                                                    "1GPjtEAFUQVrB7oOcQaejA287ZnSaqkHKykvQ4Hl_DhQ/edit)"
                                                                    ". You can either use the --id argument")
    # TODO add credentials.json instructions
    optional.add_argument('--output', action='store', type=str, default='../docs/chapters/Example_Markdown',
                           help="Specify the output file. Defaults to ../docs/chapters/Example_Markdown")

    optional.add_argument('--static_path', action='store', type=str, default='../docs/_static/img/',
                           help="Specify the static folder. Images will be stored there. Defaults to ../docs/_static/img/")

    args = my_parser.parse_args()

    try:
        result = re.search('/document/d/([a-zA-Z0-9-_]+)', args.url)
        if result.group(1):
            DOCUMENT_ID = result.group(1)
    except (IndexError, TypeError) as e:
        DOCUMENT_ID = args.id

    #return
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    try:
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
    except FileNotFoundError:
        print('''credentials.json was not found, run "python gdoc2md.py -h" for instructions on how to get your credentials. 
        Exiting...''')
        return

    service = build('docs', 'v1', credentials=creds)

    # Retrieve the documents contents from the Docs service.
    try:

        document = service.documents().get(documentId=DOCUMENT_ID).execute()
    except TypeError:
        print('''A document id or url is required for this script to run. 
            Please use either the "--id" or the "--url" paramaters.''')
        return

    document.get('inlineObjects')
    mdFile = MdUtils(file_name=args.output, title=document.get('title'))

    # iterate all basic formatting first
    # google docs api splits the document in a non-directional format
    # 'body', 'footnotes', 'footers', 'lists', 'inlineObjects' etc
    for (index, item) in enumerate(document['body']['content']):
        get_formatting(mdFile, index, document, item, content_length=len(document['body']['content']),
                       static_path=args.static_path)

    if 'footnotes' in document:
        # then add and iterate all the footnotes
        mdFile.new_header(level=2, title='References',
                          add_table_of_contents='n')

        # The process below makes footnotes appear in order
        # "get_ordered_footnotes" gives us the order of the citations as they are found in the document
        order = get_ordered_footnotes(document)

        try:
            # document['footnotes'] are in mixed order so we assign the values found in order to document['footnotes']
            for key, value in document['footnotes'].items():
                first_or_default = next((footnote for footnote in order if
                                         footnote['id']==document['footnotes'][key]['footnoteId']), None)
                if first_or_default:
                    document['footnotes'][key]['footnoteNumber'] = first_or_default['index']

            # then we order by they 'footnoteNumber' we assigned above
            document['footnotes'] = OrderedDict(sorted(document['footnotes'].items(),
                                                       key=lambda k: int(k[1]['footnoteNumber'])))
        except KeyError:
            pass

        # and everything is sorted :D
        for key, value in document['footnotes'].items():
            # Adding a shadow link to then fix reference ordering in javascript
            footnoteId = document['footnotes'][key]['footnoteId']
            mdFile.write(f"[](#{footnoteId})")
            for (index, item) in enumerate(value['content']):
                get_formatting(mdFile, index, document, item, content_length=len(value['content']),
                               static_path=args.static_path, unify_content=True)
    mdFile.create_md_file()


if __name__ == '__main__':
    main()
