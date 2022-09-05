from bs4 import BeautifulSoup
import requests


# use this if you want to parse from live website
# url = 'https://www.thecrag.com/de/klettern/spain/barcelona-area'
# r = requests.get(url)


with open('crags.html', 'r') as html_file:
    # read all content
    content = html_file.read()
    # parse
    soup = BeautifulSoup(content, 'lxml')

# use this if you want to parse from live website
# soup = BeautifulSoup(r.content, "lxml")

area_divs = soup.find_all("div", class_ = "area")

for div in area_divs:
    div = div.find("span", class_ = "primary-node-name")


    if div is None:
        pass
    else:
        crag_name = div.text
        print(crag_name)

        a = div.find("div", class_ = "name")
        print(a['href'])


# with open('crags.html', 'r') as html_file:
#     # read all content
#     content = html_file.read()
#     # parse
#     soup = BeautifulSoup(content, 'lxml')
#     # find all divs with class area
#     mydivs = soup.find_all("div", class_ = "area")

#     # example div with a crag (Can Boquet)
#     # example = mydivs[10].find("span", class_ = "primary-node-name").text

#     # loop over all divs
#     for div in mydivs:
#         div = div.find("span", class_ = "primary-node-name")
#         if div is None:
#             pass
#         else:
#             crag_name = div.text
#             print(crag_name)
