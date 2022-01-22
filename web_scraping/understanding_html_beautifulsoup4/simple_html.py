from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem some crap goes in here.</p>
<p id="supertitle">Another Lorem some crap goes in here.</p>
<p>Here's another p without attr</p>
<ul>
<li>Ralph</li>
<li>Sizi</li>
<li>Supandi</li>
<li>Mike</li>
</ul>
</body>
</html>'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')


def find_title():
    h1_tag = simple_soup.find('h1').string
    print(h1_tag)


def find_list_items():
    list_items = simple_soup.find_all('li')
    list_contents = [e.string for e in list_items]
    print(list_items)
    print(list_contents)


def find_subtitle():
    subtile_tag = simple_soup.find('p', {'class': 'subtitle'}).string
    print(subtile_tag)


def find_subtitle2():
    subtile_tag = simple_soup.find('p', {'id': 'supertitle'}).string
    print(subtile_tag)


def find_other_para():
    paras = simple_soup.find_all('p')
    other_para = [p for p in paras if 'subtitle' not in p.attrs.get('class', [])]
    print(other_para[1].string)


find_title()
find_list_items()
find_subtitle()
find_subtitle2()
find_other_para()
