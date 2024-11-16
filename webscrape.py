import requests
from bs4 import BeautifulSoup
import time

# Step 1: Define dynamic variables
job_title = "data scientist"
location = "New York"

# Step 2: Function to perform Google Search
def google_search(query, num_results):
    profile_urls = []
    for start in range(0, num_results, 10):  # Google shows 10 results per page
        url = f"https://www.google.com/search?q={query}&start={start}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract LinkedIn URLs
        for link in soup.select("a"):
            href = link.get("href")
            if href and "linkedin.com/in" in href:
                url_start = href.find("https")
                url_end = href.find("&", url_start)
                clean_url = href[url_start:url_end] if url_end != -1 else href[url_start:]
                if clean_url not in profile_urls:
                    profile_urls.append(clean_url)
        
        time.sleep(2)  # Be respectful and avoid rate-limiting
        
    return profile_urls

# Step 3: Scrape a LinkedIn Profile Without Selenium
def scrape_linkedin_profile(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract basic details (limited to static, publicly available information)
    try:
        name = soup.select_one(".text-heading-xlarge").text.strip()
    except:
        name = "N/A"
    try:
        headline = soup.select_one(".text-body-medium.break-words").text.strip()
    except:
        headline = "N/A"
    try:
        location = soup.select_one(".text-body-small.inline.t-black--light.break-words").text.strip()
    except:
        location = "N/A"
    
    return {"Name": name, "Headline": headline, "Location": location}

# Step 4: Perform Google Search and Scrape Profiles
query = f'site:linkedin.com/in "{job_title}" "{location}" -jobs'
profiles = google_search(query, num_results=20)  # Scrape first 20 results

print("LinkedIn Profiles Found:")
for profile in profiles:
    print(profile)

print("\nScraping LinkedIn Profiles...\n")
for profile_url in profiles:
    print(scrape_linkedin_profile(profile_url))
