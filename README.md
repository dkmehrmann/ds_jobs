# ds_jobs

### Intro

This web scraping project focuses on programmatically compiling job postings from common job boards for two purposes:

1. To augment my personal ongoing job search by compiling a list of companies that hire data scientists
2. To analyze the differences between job postings for **Statisticians** and **Data Scientists**

The end goal for item 1 is clear, but the end goal for item 2 is not clearly defined. In the field of Data Science/Statistics, we often hear arguments from both sides regarding the differences between the two job titles. Personally, I think the difference is largely superficial, although I acknowledge that it is likely possible to differentiate between the two job titles based on their job descriptions. Indeed, that is what I hope to accomplish by performing text classification on job descriptions I pull from the web. DISCLAIMER: This is my first attempt at web scraping.

### Technical Details

1. `scrapy.py` holds the helper functions
2. `get_data.py` pulls the data into csv files. It can be run multiple times and will update instead of overwrite existing files


### To Do

* Add comments to .py files
* Perform text analysis on data

### Job Boards
[Glassdoor](http://www.glassdoor.com/Job/data-scientist-jobs-SRCH_KO0,14.htm)
[Indeed](http://www.indeed.com/q-Data-Scientist-jobs.html)
[Kaggle](https://www.kaggle.com/forums/f/145/data-science-jobs)
[LinkedIn](https://www.linkedin.com/job/data-scientist-jobs/)
[CareerBuilder](http://www.careerbuilder.com/jobseeker/jobs/jobdetails.aspx?APath=2.21.0.0.0&job_did=JHR48M74YGL48GRLK66&showNewJDP=yes&IPath=JRKV0A)

One last note: I didn't know of the actual `scrapy` module until after I had named my files. Oops :/