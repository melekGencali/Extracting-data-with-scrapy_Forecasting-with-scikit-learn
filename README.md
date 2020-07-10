# Extracting data with scrapy - Forecasting with scikit-learn
Hazırlayan: Melek GENÇALİ :blush:


####Extracting data with scrapy 

What is the Scrapy?

- Scrapy provides a powerful framework for extracting the data, processing it and then save it.

- Scrapy uses spiders, which are self-contained crawlers that are given a set of instructions.
In Scrapy it is easier to build and scale large crawling projects by allowing developers to reuse their code.

#####Foders
  - Scrapy.py
  - items.py
  - settings.py
  - train.json
  - train.csv
  - cmdline
  
a) Scrapy.py
- First, a scrapy project is created in the terminal with 'scrapy startproject Scrapy'.Spider name Scrapy is given.
- Then the domain address of the desired web page is embedded in the code with 'scrapy genspider Scrapy fullhdfilmizlesene.com'.
- Data extraction was performed with parsev and parseData functions.
- The desired items were created in the items.py file and used here.

b) settings.py
- ROBOTSTXT_OBEY = False
- DOWNLOAD_DELAY = 3

c) cmdline
- Operation of scrapy
-Edit Configurations --> parameters = crawl Scrapy -o train.json , path= cmdline.py


d) train.json and train.csv
- The data captured is in the train json file.
- json file converted to csv file
-------------------------------

####Forecasting with scikit-learn 
At this stage, jupyter notebook was used.
- machinelerning.ipynb
  - Category prediction with actor and actress
  - Star prediction with actor and actrees
  - Created models saved as model.pkl and model2.pkl

