import requests
from bs4 import BeautifulSoup
import csv
import time

# Function to scrape a page and return its content and links
def scrape_page(url, level, max_depth):
    if level > max_depth:
        return None, []

    print(f"Scraping level {level}: {url}")

    # Send GET request to the URL
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch page. Status code: {response.status_code}")
        return None, []

    # Parse HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract title and content
    title = soup.find('h1', class_='article-title')
    content = soup.find('div', class_='article-body')
    title_text = title.text.strip() if title else 'No Title'
    content_text = content.text.strip() if content else 'No Content'

    # Find all links on the page
    links = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.startswith('/hc/en-us'):
            links.append(f"https://{url.split('/')[2]}{href}")

    # Return content and links
    return (title_text, content_text), links

# Recursive function to scrape 3 levels deep
def scrape_deep(url, max_depth=3):
    scraped_data = []
    queue = [(url, 1)]  # Tuple of (URL, current level)

    while queue:
        current_url, level = queue.pop(0)
        data, links = scrape_page(current_url, level, max_depth)
        
        if data:
            scraped_data.append(data)
        
        # Add next level links to the queue
        if level < max_depth:
            for link in links:
                queue.append((link, level + 1))
                time.sleep(1)  # To avoid rate-limiting

    return scraped_data

# Save the scraped data to a CSV file
def save_to_csv(scraped_data, file_name='zendesk_data.csv'):
    with open(file_name, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Title', 'Content'])
        for title, content in scraped_data:
            writer.writerow([title, content])

# Main function to execute the scraping process
if __name__ == "__main__":
    # Replace with the actual starting URL of the Zendesk site
    start_url = 'https://stackuphelpcentre.zendesk.com/hc/en-us'
    max_depth = 3  # Define the scraping depth

    scraped_data = scrape_deep(start_url, max_depth)
    save_to_csv(scraped_data)

    print(f"Scraping completed. Data saved to 'zendesk_data.csv'.")
