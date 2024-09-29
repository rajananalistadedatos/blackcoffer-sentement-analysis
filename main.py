import requests
from bs4 import BeautifulSoup

try:

    
        
        
    source = requests.get("https://insights.blackcoffer.com/a-leading-firm-website-seo-optimization/")


    source.raise_for_status()

    

    soup = BeautifulSoup(source.text,"html.parser")

    def save_to_file(filename, *args):
      with open(filename, 'w') as file:
        for arg in args:
            file.write(str(arg) + '\n')
    
    title = soup.find("h1", class_="entry-title").text
    
    
    paragraph = soup.find("div",class_="td-post-content tagdiv-type").text

    save_to_file('bctech2130.txt', title, paragraph)
   

    

    

except Exception as e:
     # handle exception here
     print(e)