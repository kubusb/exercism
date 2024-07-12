import re

def parse(markdown):
    # Define regex patterns
    header_pattern = r'^(#{1,6}) (.+)'
    list_item_pattern = r'^\* (.+)'
    bold_pattern = r'__(.+?)__'
    italic_pattern = r'_(.+?)_'

    # Split markdown into lines
    lines = markdown.split('\n')
    html = []
    in_list = False

    for line in lines:
        # Process headers
        if header_match := re.match(header_pattern, line):
            level, content = header_match.groups()
            html.append(f'<h{len(level)}>{content}</h{len(level)}>')
            continue

        # Process list items
        if list_match := re.match(list_item_pattern, line):
            if not in_list:
                html.append('<ul>')
                in_list = True
            content = list_match.group(1)
            html.append(f'<li>{process_inline_markup(content, bold_pattern, italic_pattern)}</li>')
            continue

        # Close list if necessary
        if in_list:
            html.append('</ul>')
            in_list = False

        # Process paragraph
        html.append(f'<p>{process_inline_markup(line, bold_pattern, italic_pattern)}</p>')

    # Close any open list
    if in_list:
        html.append('</ul>')

    return ''.join(html)

def process_inline_markup(text, bold_pattern, italic_pattern):
    # Process bold text
    text = re.sub(bold_pattern, r'<strong>\1</strong>', text)
    # Process italic text
    text = re.sub(italic_pattern, r'<em>\1</em>', text)
    return text
