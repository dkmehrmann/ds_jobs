import requests
from bs4 import BeautifulSoup
import re
import time


def get_soup(url):
    page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    data = page.text
    
    return BeautifulSoup(data)



def get_gd_links(gd_soup, gd_job_ids = []):
    
    gd_uri = 'http://www.glassdoor.com'
    regex = r'ListingId=(.*)'

    gd_jobs = []

    for link in gd_soup.find_all('a'):                              # for each link in the page
        href = link.get('href')                                     # get the href
        if href:                                                    # if the href exists
            if ('partner/job' in href and                           # if it is a link for a job posting
                re.search(regex, href).group(1) not in gd_job_ids): # and we don't alread have that job
                gd_jobs.append(gd_uri + href)                       # add the job to the list of jobs
                gd_job_ids.append(re.search(regex, href).group(1))  # add the job id to the list of job ids
            
    return gd_jobs, gd_job_ids



def get_kg_links(kg_soup, kg_job_ids = []):
    kg_uri = 'https://www.kaggle.com'
    regex = r'/forums/f/145/data-science-jobs/t/(.*?)[/]'
    kg_jobs = []

    for link in kg_soup.find_all('a'):
        for link in kg_soup.find_all('a'):                              # for each link in the page
            href = link.get('href')                                     # get the href
            if href:                                                    # if the href exists
                if ('/forums/f/145/data-science-jobs/t/' in href and    # if it is a link for a job posting
                    re.search(regex, href).group(1) not in kg_job_ids): # and we don't alread have that job
                    kg_jobs.append(kg_uri + href)                       # add the job to the list of jobs
                    kg_job_ids.append(re.search(regex, href).group(1))  # add the job id to the list of job ids
                    
    return kg_jobs, kg_job_ids



def get_li_links(li_soup, li_job_ids = []):
    regex = r'/jobs2/view/(.*?)[?]'
    li_jobs = []

    for link in li_soup.find_all('a'):                              # for each link in the page
        href = link.get('href')                                     # get the href
        if href:                                                    # if the href exists
            if ('/jobs2/view/' in href and                          # if it is a link for a job posting
                re.search(regex, href).group(1) not in li_job_ids): # and we don't alread have that job
                li_jobs.append(href)                                # add the job to the list of jobs
                li_job_ids.append(re.search(regex, href).group(1))  # add the job id to the list of job 
    return li_jobs, li_job_ids



def get_cb_links(cb_soup):
    cb_jobs = []
    for link in cb_soup.find_all('a'):                              # for each link in the page
        href = link.get('href')
        if href:
            if '/jobseeker/jobs/jobdetails' in href:
                cb_jobs.append(href)
    return cb_jobs



def crawl_gd(n_pages=5,sleep_timer=10):
    
    gd_p1 = 'http://www.glassdoor.com/Job/chicago-data-scientist-jobs-SRCH_IL.0,7_IC1128808_KO8,22.htm'
    gd_links = []
    gd_ids = []

    for i in range(1,n_pages + 1):
        print('pulling links from page {0}'.format(i))
        if i == 1:
            gd_links, gd_ids = get_gd_links(get_soup(gd_p1))
            print('Got {0} links from page {1}'.format(len(gd_links),i))
        else:
            gd_url = 'http://www.glassdoor.com/Job/chicago-data-scientist-jobs-SRCH_IL.0,7_IC1128808_KO8,22_IP{0}.htm'.format(i)
            links, ids = get_gd_links(get_soup(gd_url), gd_ids)
            gd_links.extend(links)
            gd_ids.extend(ids)
            print('Got {0} links from page {1}'.format(len(links),i))
        time.sleep(sleep_timer)
        
    return gd_links




def crawl_kg(n_pages = 10, sleep_timer=10):
    
    kg_p1 = 'https://www.kaggle.com/forums/f/145/data-science-jobs'
    kg_links = []
    kg_ids = []

    for i in range(1,n_pages + 1):
        print('pulling links from page {0}'.format(i))
        if i == 1:
            kg_links, kg_ids = get_kg_links(get_soup(kg_p1))
            print('Got {0} links from page {1}'.format(len(kg_links),i))
        else:
            kg_url = 'https://www.kaggle.com/forums/f/145/data-science-jobs?page={0}'.format(i)
            links, ids = get_kg_links(get_soup(kg_url), kg_ids)
            kg_links.extend(links)
            kg_ids.extend(ids)
            print('Got {0} links from page {1}'.format(len(links),i))
        time.sleep(sleep_timer)
        
    return kg_links




def crawl_li(n_pages = 10, sleep_timer=10):
    
    li_p1 = 'https://www.linkedin.com/job/data-scientist-jobs-chicago-il/?sort=relevance&page_num=1&trk=jserp_pagination_1'
    li_links = []
    li_ids = []

    for i in range(1,n_pages + 1):
        print('pulling links from page {0}'.format(i))
        if i == 1:
            li_links, li_ids = get_li_links(get_soup(li_p1))
            print('Got {0} links from page {1}'.format(len(li_links),i))
        else:
            li_url = 'https://www.linkedin.com/job/data-scientist-jobs-chicago-il/?sort=relevance&page_num={0}&trk=jserp_pagination_{0}'.format(i)
            links, ids = get_li_links(get_soup(li_url), li_ids)
            li_links.extend(links)
            li_ids.extend(ids)
            print('Got {0} links from page {1}'.format(len(links),i))
        time.sleep(sleep_timer)
        
    return li_links