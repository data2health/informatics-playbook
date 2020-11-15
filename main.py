from __future__ import print_function
import sys
import pickle
import os.path
import urllib.request
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from mdutils.mdutils import MdUtils
import re

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

# this regex is kinda long :D
WEB_URL_REGEX = r"""(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))"""

# TODO start parsing tables and strikethrough

# '1L1vU0YWf1PjVMc7LL_nFTA0lApuC4hlVgjztXQ-MLSU'
# '16U5sLssOMuG8X8GF-qIo7VXW9BQJ_E0QIz6C5CzP7t0'
# '1XkBuOBcy4g69mRGiHzLAFff_qDwadPKogV3E-lnNcgc' primary file

def is_heading(paragraph):
    named_style_type = paragraph.get('paragraphStyle').get('namedStyleType')
    if 'HEADING' in named_style_type:
        # m2r2 does not parses headers to paragraphs if there are different sized headers with the same content
        # using this for now until I find an alternative
        return int(re.search(r'[-+]?[0-9]+', named_style_type)[0])
    return 0


def main():
    # The ID of a sample document.
    DOCUMENT_ID = '1XkBuOBcy4g69mRGiHzLAFff_qDwadPKogV3E-lnNcgc' #'1GPjtEAFUQVrB7oOcQaejA287ZnSaqkHKykvQ4Hl_DhQ'

    try:
        result = re.search('d/(.*)/edit', sys.argv[1])
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

    for (index, item) in enumerate(document['body']['content']):
        if item.get('paragraph'):
            bullet_list = []
            if item.get('paragraph').get('bullet'):
                bullet_point = ''
                # don't currently use this, until I understand how gdocs handles ordered lists
                is_ordered = False
                for element in item.get('paragraph').get('elements'):
                    if element.get('footnoteReference', {}).get('footnoteNumber'):
                        # don't know why this exists, I just pass it to not break the script
                        pass
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
                '''for element in item.get('paragraph').get('elements'):
                    content = element.get('textRun').get('content')
                    bullet_list.append(content.rstrip('\n').strip())
                    mdFile.new_list(bullet_list)'''
            else:
                for element in item.get('paragraph').get('elements'):
                    # search for images
                    if element.get('inlineObjectElement'):
                        inline_object = document.get('inlineObjects'). \
                            get(element.get('inlineObjectElement').get('inlineObjectId'))
                        object_properties = inline_object.get('inlineObjectProperties').get('embeddedObject')
                        image_path = object_properties.get('imageProperties').get('contentUri')
                        urllib.request.urlretrieve(image_path,
                                                   filename=f"docs/_static/{image_path.split('/')[-1]}.jpg")

                        mdFile.new_line(mdFile.new_inline_image(text='image',
                                                                path=f"../_static/{image_path.split('/')[-1]}.jpg"))

                        # add an empty character to prevent image collision with text
                        mdFile.write(' ')

                    # search for text elements
                    if element.get('textRun'):
                        text_run = element.get('textRun')
                        is_section_link = True if text_run.get("textStyle", {}).get('link', {}).get('bookmarkId') or \
                            text_run.get("textStyle", {}).get('link', {}).get('headingId') else False

                        content = text_run.get('content')
                        if is_section_link:
                            link_to = content.replace(" ", "-").lower()
                            content = f"[{content}](#{link_to})"

                        #  escape starting strings like "n." where n is any number to prevent breaking md format
                        for match in re.finditer(r'^[-+]?[0-9]+\.', content):
                            content = content[:match.start()+1] + '\\' + content[match.start()+1:]

                        # find links in text and format them accordingly
                        for match in re.finditer(WEB_URL_REGEX, content):
                            wrapped_in_parenthesis = False
                            try:
                                # if string is already wrapped in parenthesis we do not need to add our own
                                # for the markdown formatting
                                if content[:match.start()-1] == '(' and content[match.start()+1:] == ')':
                                    wrapped_in_parenthesis = True
                            except IndexError:
                                pass
                            if wrapped_in_parenthesis:
                                content = content[:match.start() - 1] + f"[{match.group(1)}]" + \
                                          content[match.start() - 1:]
                            else:
                                # we must add the parenthesis around the matching url on our own
                                # this SHOULD work not tested yet
                                content = content[:match.start()] + f"[{match.group(1)}]" + \
                                          f"({content[match.start():match.end()]})" + content[match.end():]
                        # managing some edge cases for now
                        # until a solution is found for every case

                        if content.replace(' ', '') == '\n':  # using strip() removes \n as well
                            mdFile.new_line()
                            continue
                        if content == ' ':
                            mdFile.write(' ')
                            continue

                        try:
                            is_bold = element.get('textRun').get('textStyle').get('bold')
                            is_italic = element.get('textRun').get('textStyle').get('italic')
                            is_strikethrough = element.get('textRun').get('textStyle').get('strikethrough')
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
                            #if is_strikethrough:
                            #    stripped_content = f"~~{stripped_content}~~"
                            mdFile.write(stripped_content,
                                         bold_italics_code=bold_italics_code)

                        # add them after all formatting
                        if ends_with_space:
                            mdFile.write(' ')
                        if add_new_line:
                            # alternatively use mdFile.write('\n') to add a completely new line
                            # mdFile.write('\\')
                            mdFile.write('\n')
                            mdFile.new_line()

            # add a space between each element
            spacing = item.get('paragraph').get('paragraphStyle').get('lineSpacing')
            if spacing:
                mdFile.write((int(spacing) // 100) * '\n')
            else:
                pass
                #mdFile.new_line()
                # mdFile.write('\n')
    #mdFile.new_table_of_contents(table_title='Contents', depth=2)
    mdFile.create_md_file()
    print('The title of the document is: {}'.format(document.get('title')))


if __name__ == '__main__':
    main()
