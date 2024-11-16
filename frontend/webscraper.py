import os
import requests
from bs4 import BeautifulSoup
import time
import subprocess

# Step 1: Define dynamic variables
job_title = "data scientist"
location = "New York"

# Step 2: Function to perform Google Search
# Step 2: Function to perform Google Search with URL validation
def google_search(query, num_results):
    profile_urls = []
    for start in range(0, num_results, 10):  # Google shows 10 results per page
        url = f"https://www.google.com/search?q={query}&start={start}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }
        print(f"Requesting URL: {url}")
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f"Error: Request failed with status code {response.status_code}")
            break
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract LinkedIn URLs with additional validation
        for link in soup.select("a"):
            href = link.get("href")
            if href and "linkedin.com/in" in href:
                # Remove any Google redirect prefix and keep only valid URLs
                url_start = href.find("https")
                url_end = href.find("&", url_start)
                clean_url = href[url_start:url_end] if url_end != -1 else href[url_start:]
                if clean_url.startswith("https://www.linkedin.com/in") and clean_url not in profile_urls:
                    profile_urls.append(clean_url)

        time.sleep(2)  # Delay to avoid rate-limiting
        
    return profile_urls


# Step 3: Scrape a LinkedIn Profile Without Selenium
def scrape_linkedin_profile(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    print(f"Scraping LinkedIn profile: {url}")  # Debugging line to see the URLs being scraped
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract basic details (limited to static, publicly available information)
    profile_info = {
        "Name": "N/A",
        "Headline": "N/A",
        "Location": "N/A"
    }
    
    try:
        name = soup.select_one("h1.text-heading-xlarge").text.strip()
        profile_info["Name"] = name
    except AttributeError:
        pass
    
    try:
        headline = soup.select_one(".text-body-medium.break-words").text.strip()
        profile_info["Headline"] = headline
    except AttributeError:
        pass
    
    try:
        location = soup.select_one(".text-body-small.inline.t-black--light.break-words").text.strip()
        profile_info["Location"] = location
    except AttributeError:
        pass
    
    return profile_info

# Step 4: Perform Google Search and Scrape Profiles
query = f'site:linkedin.com/in "{job_title}" "{location}" -jobs'
print("Searching Google for profiles...")  # Debugging line
profiles = google_search(query, num_results=20)  # Scrape first 20 results

# If no profiles were found, print a message
if not profiles:
    print("No LinkedIn profiles found.")
else:
    print("LinkedIn Profiles Found:")
    for profile in profiles:
        print(profile)

    print("\nScraping LinkedIn Profiles...\n")
    for profile_url in profiles:
        profile_data = scrape_linkedin_profile(profile_url)
        print(profile_data)

# Step 5: Run the script using subprocess (optional)
# Using os.path to ensure proper directory handling
script_dir = os.path.dirname(os.path.realpath(__file__))  # Get the current script directory
script_path = os.path.join(script_dir, "webscrape.py")  # Construct the path to the script

# Check if the path is correct
print(f"Script Path: {script_path}")  # Debugging line to see the path