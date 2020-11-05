import requests
from bs4 import BeautifulSoup
#variables
url="https://quotes.toscrape.com/" #This is the url of the site from which we have to scrape the data
response=requests.get(url)#The requests.Response() Object contains the server's response to the HTTP request.
soup=BeautifulSoup(response.text,'lxml')#turning that response into text
quotes=soup.find_all('span',class_='text')#extracting quotes
authors=soup.find_all('small',class_='author')#extracting author_name
tags=soup.find_all('div',class_='tags')#extracting tags

# for loop to itrate author_name and quotes one by one
#.text prints the text inside the html tag

for i in range(0, len(authors)): 

    print(authors[i].text,':')
    print(quotes[i].text)
    quotags=tags[i].find_all('a',class_='tag')#getting the tag inside the tags 

    for quotag in quotags:#looping through those tags
        print(quotag.text)


print('Task completed')