import markdown
import markdownify
from bs4 import BeautifulSoup
from distutils.version import StrictVersion
from natsort import natsorted

with open('CHANGELOG.md', 'r') as f:
    markdown_string = f.read()


html_string = markdown.markdown(markdown_string)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

soup = BeautifulSoup(html_string, 'html.parser')

h1_href = soup.h1
h1_all = soup.find_all('h1')

dict_changelog = {}

for h1 in h1_all:

    print('|====================== START ======================|')
    h1.name = 'h2'
    release_version = h1
    print(h1.text)
    ul = h1.find_next('ul')
    print(ul)
    dict_changelog[release_version] = ul
    print('|======================= END =======================|')

print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
print(dict_changelog)
print('>>>>>>>>>> RESORTED DICT >>>>>>')

dict_changelog_sorted = natsorted(dict_changelog.items(), reverse=True)

print(dict_changelog_sorted)

print('______________________________________________________________')

html_string_sorted = ''
for key, value in dict_changelog_sorted:

    html_string_sorted += str(key)
    html_string_sorted += '\n'

    html_string_sorted += str(value)
    html_string_sorted += '\n'

print('|-----------------------       MARKDOWN       ------------------->')
print(html_string)

markdown_string = markdownify.markdownify(html_string_sorted, heading_style='ATX', bullets='-')
print(markdown_string)

with open("CHANGELOG_sorted.md", "w") as markdown_file:
    markdown_file.write(markdown_string)
