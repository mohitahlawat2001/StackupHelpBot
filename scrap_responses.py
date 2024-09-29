
import requests
from datetime import datetime
from bs4 import BeautifulSoup

def fetch_FAQs():
    url = 'https://stackuphelpcentre.zendesk.com/hc/en-us'  # Replace with the actual URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the Promoted Articles section
    articles_section = soup.find('section', class_='articles')
    articles = []

    if articles_section:
        promoted_items = articles_section.find_all('li', class_='promoted-articles-item')
        for item in promoted_items:
            link = item.find('a')
            if link:
                title = link.text.strip()
                url = link['href']
                full_url = f"https://stackuphelpcentre.zendesk.com{url}"
                articles.append(f"[{title}]({full_url})")

    print(articles)

    return articles



# Function to convert timestamp to a readable format
def time_ago(timestamp):
    # Convert the timestamp to a datetime object
    created_time = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
    now = datetime.utcnow()
    # Calculate the difference
    delta = now - created_time
    # Determine the time frame for display
    if delta.days > 30:
        return f"{delta.days // 30} months ago"
    elif delta.days > 0:
        return f"{delta.days} days ago"
    else:
        return "Less than a day ago"
    

def fetch_recent_activities():
    # URL of the recent activities API
    url = "https://stackuphelpcentre.zendesk.com/hc/api/internal/recent_activities.json?locale=en-us&page=1&per_page=5"

    # Fetch the JSON data
    response = requests.get(url)

    # Initialize an empty string to store the output
    formatted_activities = "Recent activity\n\n"  # Start with the heading

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract activities
        activities = data.get('activities', [])

        for activity in activities:
            breadcrumbs = activity.get('breadcrumbs', [])
            title = activity.get('title')
            link = activity.get('url')
            comment_count = activity.get('comment_count', 0)
            created_at = activity.get('timestamp')

            # Create the full URL for the article
            full_article_url = f"https://stackuphelpcentre.zendesk.com{link}"

            # Writing the breadcrumb links
            breadcrumb_links = []
            for breadcrumb in breadcrumbs:
                breadcrumb_name = breadcrumb['name']
                breadcrumb_url = breadcrumb['url']
                full_breadcrumb_url = f"https://stackuphelpcentre.zendesk.com{breadcrumb_url}"
                breadcrumb_links.append(f"[{breadcrumb_name}]({full_breadcrumb_url})")

            # Format the activity output
            if breadcrumbs:
                # Assuming the last breadcrumb is the most relevant section
                last_breadcrumb = breadcrumb_links[-1]  # Take the last breadcrumb as the section title
            else:
                last_breadcrumb = "General"

            # Writing the formatted output with embedded links
            formatted_activities += f"{last_breadcrumb}\n"  # Last breadcrumb as the section title
            formatted_activities += f"[{title}]({full_article_url})\n"  # Markdown link format for the article
            formatted_activities += f"Article created {time_ago(created_at)}  Number of comments: {comment_count}\n\n"

        # Return the formatted activities as a string
        # print(formatted_activities)
        return formatted_activities

    else:
        return f"Failed to retrieve data. Status code: {response.status_code}"



fetch_recent_activities()