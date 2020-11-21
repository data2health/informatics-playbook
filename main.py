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

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']


# TODO strikethrough, links with titles are broken

# '1L1vU0YWf1PjVMc7LL_nFTA0lApuC4hlVgjztXQ-MLSU'
# '16U5sLssOMuG8X8GF-qIo7VXW9BQJ_E0QIz6C5CzP7t0'
# '1XkBuOBcy4g69mRGiHzLAFff_qDwadPKogV3E-lnNcgc' primary file


def is_heading(paragraph):
    named_style_type = paragraph.get('paragraphStyle').get('namedStyleType')
    if 'HEADING' in named_style_type:
        return int(re.search(r'[-+]?[0-9]+', named_style_type)[0])
    return 0


def render_table(mdFile, table):
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
                                #element_content = element_content.rstrip('\n')
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

    :param document:
    :return: Return an order variable which contains a sorted list with "footnoteId" and "footnoteNumber" values
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


def get_formatting(mdFile, index, document, item, content_length, unify_content=False):
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
                    content = element.get('textRun').get('content')
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
            if item.get('paragraph', {}).get('paragraphStyle', {}):
                headingId = item.get('paragraph', {}).get('paragraphStyle', {}).get('headingId')
                if headingId:
                    mdFile.write(f"[]({headingId})")

            for element in item.get('paragraph').get('elements'):

                # search for images
                if element.get('inlineObjectElement'):
                    inline_object = document.get('inlineObjects'). \
                        get(element.get('inlineObjectElement').get('inlineObjectId'))
                    object_properties = inline_object.get('inlineObjectProperties').get('embeddedObject')
                    image_path = object_properties.get('imageProperties').get('contentUri')
                    urllib.request.urlretrieve(image_path,
                                               filename=f"docs/_static/images/{image_path.split('/')[-1]}.jpg")

                    mdFile.new_line(mdFile.new_inline_image(text='image',
                                                            path=f"../_static/images/{image_path.split('/')[-1]}.jpg"))

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
                    #  escape starting strings like "n." where n is any number to prevent breaking md format
                    for match in re.finditer(r'^[-+]?[0-9]+\.', content):
                        content = content[:match.start() + 1] + '\\' + content[match.start() + 1:]

                    # managing some edge cases for now
                    # until a solution is found for every case

                    if content.replace(' ', '') == '\n':  # using strip() removes \n as well
                        mdFile.new_line()
                        continue
                    if content == ' ':
                        mdFile.write(' ')
                        continue

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

                    # find newlines in text
                    add_new_line = False
                    if '\n' in content:
                        add_new_line = True

                    # find if text starts or ends with space or tab
                    starts_with_space = False
                    ends_with_space = False

                    if re.match(r'\s', content):
                        starts_with_space = True
                    if content.endswith(' '):
                        ends_with_space = True

                    # add the white space before any formatting to prevent breaking the format
                    if starts_with_space:
                        mdFile.write(' ')

                    # if these conditions meet we should transform the text to a header
                    # google docs is weird with its results so we have to check a lot of conditions
                    _is_heading = is_heading(item.get('paragraph'))
                    if _is_heading:
                        mdFile.new_header(level=_is_heading, title=content.rstrip('\n').strip(),
                                          add_table_of_contents='n')
                    # else just write plain text
                    else:
                        stripped_content = content.rstrip('\n').strip()

                        # recommonmark doesn't allow strikethroughs :(
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

        # add a space between each element
        spacing = item.get('paragraph').get('paragraphStyle').get('lineSpacing')
        if spacing:
            mdFile.write((int(spacing) // 100) * '\n')
        else:
            pass
            # mdFile.new_line()


def main():
    # The ID of a sample document.
    DOCUMENT_ID = '1XkBuOBcy4g69mRGiHzLAFff_qDwadPKogV3E-lnNcgc'

    try:
        result = re.search('/document/d/([a-zA-Z0-9-_]+)', sys.argv[1])
        if result.group(1):
            DOCUMENT_ID = result.group(1)
    except IndexError:
        pass

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
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

    service = build('docs', 'v1', credentials=creds)

    # Retrieve the documents contents from the Docs service.
    document = service.documents().get(documentId=DOCUMENT_ID).execute()
    document.get('inlineObjects')
    mdFile = MdUtils(file_name='docs/chapters/Example_Markdown', title=document.get('title'))

    # iterate all basic formatting first
    # google docs api splits the document in a non-directional format
    # 'body', 'footnotes', 'footers', 'lists', 'inlineObjects' etc
    for (index, item) in enumerate(document['body']['content']):
        get_formatting(mdFile, index, document, item, content_length=len(document['body']['content']))

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
                get_formatting(mdFile, index, document, item, content_length=len(value['content']), unify_content=True)
    mdFile.create_md_file()


if __name__ == '__main__':
    main()
