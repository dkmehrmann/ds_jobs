# ds_jobs

### Intro

This web scraping project focuses on programmatically compiling job postings from common job boards for two purposes:

1. To augment my personal ongoing job search by compiling a list of companies that hire data scientists
2. To analyze the differences between job postings for **Statisticians** and **Data Scientists**

The end goal for item 1 is clear, but the end goal for item 2 is not clearly defined. In the field of Data Science/Statistics, we often hear arguments from both sides regarding the differences between the two job titles. Personally, I think the difference is largely superficial, although I acknowledge that it is likely possible to differentiate between the two job titles based on their job descriptions. Indeed, that is what I hope to accomplish by performing text classification on job descriptions I pull from the web. 

### Technical Details

In order to better demonstrate my process and provide the necessary tools to repeat this analysis, I code each step in a Jupyter(iPython) Notebook and then write the steps in the form of functions in a Python script called `scrapy.py`. The steps are as follows:

1. `web_scraping.ipynb` gets the BeautifulSoup from each job board and parses the links to the actual jobs
2. `iterate.ipynb` provides pagination functionality to walk through each page of job postings
3. `open_gd.ipynb` opens the links for Glassdoor and gets the job description, job title, and location


### Job Boards
[Glassdoor](http://www.glassdoor.com/Job/data-scientist-jobs-SRCH_KO0,14.htm)
[Indeed](http://www.indeed.com/q-Data-Scientist-jobs.html)
[Kaggle](https://www.kaggle.com/forums/f/145/data-science-jobs)
[LinkedIn](https://www.linkedin.com/job/data-scientist-jobs/)
[CareerBuilder](http://www.careerbuilder.com/jobseeker/jobs/jobdetails.aspx?APath=2.21.0.0.0&job_did=JHR48M74YGL48GRLK66&showNewJDP=yes&IPath=JRKV0A)
