import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://realpython.github.io/fake-jobs/"

def scrape_jobs():
    response = requests.get(URL)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    job_cards = soup.find_all("div", class_="card-content")

    jobs = []
    for card in job_cards:
        title = card.find("h2", class_="title").text.strip()
        company = card.find("h3", class_="company").text.strip()
        location = card.find("p", class_="location").text.strip()
        date = card.find("time").text.strip()

        jobs.append({"title": title, "company": company, "location": location, "date": date})

    df = pd.DataFrame(jobs)
    df.to_csv("jobs.csv", index=False)
    print(f"✅ Scraped {len(df)} jobs and saved to jobs.csv")

if __name__ == "__main__":
    scrape_jobs()
