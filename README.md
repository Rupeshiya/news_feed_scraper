## News-Scrapper

A simple scrapper using python and newspaper library

### Application flow:
**Step wise:**
1. When we enter “python3 src/news_scrapper.py --root_dir scraper/Articles --source_list scraper/news_source.txt” then python going to execute the file src/news_scrapper.py
 
2. --root_dir and --source_list is passed as an argument to get the store location and news source respectively.
.
3. Then execute the application accordingly as given below:


![flow](https://user-images.githubusercontent.com/31209617/93479031-8fc87880-f919-11ea-9b8b-b8890a9d5253.png)


#### Libraries used:
1. newspaper3k==0.2.8
2. jsonpickle==1.1.0
3. simplejson==3.16.0
4. pymongo==3.9.0
5. dnspython==1.16.0
6. environs==6.0.0
7. cryptography==2.7
 
#### Dev specific dependencies
8. pylint==2.3.0
9. git-pylint-commit-hook==2.5.1
10. pycodestyle==2.5.0
11. mypy==0.730
12. mockito==1.1.1
13. flake8==3.7.6
14. pep8-naming==0.5.0
 



### Main Goal
---

We want to build a small newsfeed management system which will accept a simple text file as input containing news sites such as:
```
http://slate.com
https://www.reuters.com/places/india
...
```

1. The system will crawl through all of these sites, extract individual news and store them as JSON files/documents.
Functionality
2. Download the news feed from different sources in parallel. This feature is natively provided by the library used for scraping in this app.
 
3. Store all news feeds as JSON files to the local file system. For example, if the app is run for date 2020-09-16, it will create a folder named 2020-09-16 and place all json files there. The format of the json file is "_.json". Example - reuters_2020-09-16T12.05.32.json
 
4. Dump all news feeds to MongoDB as json documents. This app uses a free cloud hosted version of MongoDB (MongoDB Atlas or mLab).
 
5. Check for duplicity of feed by combination of (title, publish_date). If present, it skips the insertion to MongoDB.
 
### Generate summary.
---

1. Create a summary file (summary.txt) in the output folder, e.g, 2019-10-08. The file summarizes the count of all downloaded articles from all sources.
2. Create an error log file (error_logs.txt) in the output folder, e.g, 2019-10-08. The log file contains details of all the news feeds that errored out during parsing/building. It stores the stack trace which can be used for debugging purposes.

### How to setup and run tests/lint
---

Make sure python3.7 is installed and added to path. 
```
python --version
```

or
```
python3.7 --version
```

Then create a virtual environment for the project.
```
virtualenv -p python venv
. venv/bin/activate
```

or
```
virtualenv -p python3.7 venv
. venv/bin/activate
```

Or 
```
python3 -m pip venv .
cd scripts/activate
```

Then on all platforms install the python dependencies:
```
pip install -r requirements-dev.txt
```

> **Note:** there is a separate requirements.txt file that excludes all but the dependencies required for deployment. Any production dependencies should be added to both files.


### Run Linting:
---

```
sh scripts/lint.sh
```

### What does this give me?
---


The scraping can be run by running the python program.
```
python3  src/news_scrapper.py   --root_dir <output-directory>   --source_list <path-to-source-file>
```

### For example
---

```
python3  src/news_scrapper.py   --root_dir   F:/Scraper/Articles   --source_list F:/Scraper/news_source.txt
```

### Output:
---


![output](https://user-images.githubusercontent.com/31209617/93479268-bdadbd00-f919-11ea-9145-2b921bc2c9cb.PNG)


Make sure the file news_source.txt exists in the specified location. <br/>
A sample news_source.txt has been provided in the repo. All the output files (json files, summary.txt and error_logs.txt) will be generated in the specified output directory.<br/>
To make things easier, the above command is wrapped by a shell script news_feed.sh.<br/>
The script contains the above python command to run the app with a default output directory and relative location to the source file present in the repo. <br/>
We can just run the script or we can edit it and provide our custom path. <br/>
To do this, open the script in a text editor and replace the values for root_dir and source_list with custom values where we want to have our input/output.<br/>
 
### Now run the script
---


```
sh scripts/news_feed.sh
```

The script will run for some time (~mins) depending on the count of sources we provided and the total number of articles present on those sources for the particular day the app is run.<br/>
For functionality testing, It is advised to provide a single source containing a small number of articles. `http://slate.com` is one preferred input for which it takes about 3 mins to scrape all articles on any given day. <br/>
For testing multiple sources,<br/>
`http://slate.com` <br/>
`https://www.reuters.com/places/india` <br/>
are two example values and it takes about 8 mins to scrape articles from these 2 sources combined.
Once the script execution completes, the output can be found in the local file system and MongoDB cluster.<br/>
 

