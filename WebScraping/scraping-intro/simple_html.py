from bs4 import BeautifulSoup

SIMPLE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sample Web Page</title>
</head>
<body>

    <header>
        <h1>Welcome to My Sample Website</h1>
    </header>

    <main>
        <section id="section1">
            <h2>Section 1</h2>
            <p>This is the first section of the page.</p>
            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
                <li>Item 3</li>
            </ul>
        </section>

        <section id="section2">
            <h2>Section 2</h2>
            <p class='test'>This is the second section of the page.</p>
            <ol>
                <li>One</li>
                <li>Two</li>
                <li>Three</li>
            </ol>
        </section>
    </main>

    <footer>
        <p>&copy; 2024 Sample Website. All rights reserved.</p>
    </footer>

</body>
</html>
"""
simple_soup = BeautifulSoup(SIMPLE_HTML,'html.parser')
print(simple_soup.find('h1').string)

def find_title():
    h1_tag = simple_soup.find('h1')
    print(h1_tag.string)

def find_list_items():
    list_items = simple_soup.find_all('li')
    print([item.string for item in list_items])

def find_test_p():
    paragraph = simple_soup.find('p',{'class':'test'})
    print(paragraph)

def find_p_no_class():
    paragraphs = simple_soup.find_all('p')
    print(paragraphs)
    no_class = [p for p in paragraphs if 'test' not in p.attrs.get('class',[])]
    print(no_class)


find_list_items()
find_test_p()
find_p_no_class()
