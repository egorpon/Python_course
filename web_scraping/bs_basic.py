from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special super-special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""


# find element with an id
# soup.find(id="foo")
# soup.select("#foo")[0]

# find all elements with a class
# soup.find_all(class_="bar")
# soup.select(".bar")

# find all elements with a data attribute
# soup.find_all(attrs={"data-baz": True})
# soup.select("[data-baz]")

soup = BeautifulSoup(html, "html.parser")
# attr = soup.find("div")["id"]
# print(attr)
# for e in soup.select(".special"):
#     print(e.name)
#     print(e.attrs)

