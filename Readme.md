# [Bombay Stock Exchange Shareholding Pattern](https://www.bseindia.com/index.html)

## Introduction

This is a scraping script made in order to scrape the data from bombay stock exchange.


## Ground Rules

-   You need to download  python from the below link
    >[python v3.6.9](https://www.python.org/downloads/)
    
-   You need to  **clone or download** the below repository
    >[https://github.com/abhishekzgithub/bseholder/tree/develop](https://github.com/abhishekzgithub/bseholder.git)

- You need to download [Visual Studio code](https://code.visualstudio.com/download)
    
--------------
 ## Getting started
 1. Clone or download the repository or code from the github repository.
 2. Make sure you can open it inside visual studio code.
 3. Goto the **bseholder** folder
    * > cd **bseholder**
 4. Run on the command line
    * > pip install pipenv
    * > pipenv shell
    * > pipenv install -r requirements.txt
    * > python run.py
 5. The results will be downloaded in the **scraped_data** folder in an excel format.
 
 -------------------
 ## Place to know from where the data is getting scraped
 1. https://www.bseindia.com/index.html
 2. Goto **Corporates** tab
 3. Goto the **Corporate Fillings** tab
 4. Then goto **Shareholding Patterns**
 5. For bseid 539807 and quarter 102, this will lead to
    * >https://www.bseindia.com/corporates/shpPromoterNGroup.aspx?scripcd=539807&qtrid=102 

 ## Thanks
 Please give star if you are using or like it.