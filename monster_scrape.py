from bs4 import BeautifulSoup
import requests

url = 'https://www.monster.com/jobs/search/?q=developer&where=San-Francisco__2C-CA&intcid=skr_navigation_nhpso_searchMain'
page = requests.get(url).text
soup = BeautifulSoup(page, 'lxml')
# print(soup.prettify())


query = soup.title.text
# print(query)

results = soup.find(id="ResultsContainer")
# print(results.prettify())

job_elems = results.find_all('section', class_='card-content')
for job in job_elems:
    title_elem = job.find('h2', class_='title')
    company_elem = job.find('div', class_='company')
    location_elem = job.find('div', class_='location')

    if None in (title_elem, company_elem, location_elem):
        continue

    fs_jobs = results.find_all('h2', string=lambda text: "software engineer" in text.lower())

    for fs_job in fs_jobs:
        link = fs_job.find('a')['href']

    # print(title_elem)
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print(f'Apply here: {link}')
    print()
    print()


