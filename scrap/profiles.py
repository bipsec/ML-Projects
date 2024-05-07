import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_profile_data(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find elements containing profile data
        profiles = soup.find_all('body', class_='home-page')

        data = []
        for profile in profiles:
            name = profile.find('h1').text.strip().split()
            # Find email image
            email_image = profile.find('img', class_='email-image')
            if email_image:
                email_text = email_image.get('alt', '').split('email', 1)[
                    -1].strip()  # Extract email after the word "email"
                email = email_text.split(' ')[0]  # Take the first word after "email"
            else:
                email = ''

            # Find panel-body inside profile for research information
            panel_body = profile.find('div', class_='panel-body')
            if panel_body:
                p_tags = panel_body.find_all('p')
                research_text = ' '.join([word.strip() for p in p_tags for word in p.get_text().split() if word.strip()])

            else:
                research_text = ''

            data.append([name, email, research_text ])

        return data
    except Exception as e:
        print("An exception happened while scraping:", e)


def save_to_csv(data, filename='profile_data.csv'):
    df = pd.DataFrame(data, columns=['Name', 'Email', 'Research'])
    df.to_csv(filename, index=False)


if __name__ == "__main__":
    base_url = 'https://cs.txstate.edu/accounts/profiles/'
    profile_data = scrape_profile_data(base_url)
    profile_arr = ["hs15/", "ma04/", "t_i24/", "sox16/", "ok11/"]
    scraped_data = []
    for item in profile_arr:
        url = base_url + item
        text_data = scrape_profile_data(url)
        if text_data:
            # cleaned_data = [[item.strip().replace('\n', '') for item in profile] for profile in text_data]
            scraped_data.extend(text_data)

    if scraped_data:
        save_to_csv(scraped_data)
