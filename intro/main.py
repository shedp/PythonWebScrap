from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content = html_file.read()
    
    # create an instance of beautiful soup
    soup = BeautifulSoup(content, 'lxml')
    
    # Grab ONE h2 tag
    ## tags = soup.find('h2')

    #Grab ALL h2 tags
    ##h2_tags = soup.find_all('h2')
    ##facts = h2_tags[2:]
    ##print(facts)

    ## for fact in facts:
    ##     print(fact.text)

    #Find all secations with class ='full-width-image__wrapper'
    fact_sections = soup.find_all('section', class_='full-width-image__wrapper')
    for fact in fact_sections:
        fact_title = fact.h2.text
        fact_description = fact.p.text
        print(fact_title)
        print(fact_description)