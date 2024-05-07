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
            name = profile.find('h2').text.strip()
            email = profile.find('img', class_='email-image').get('alt', '')
            panel_bodies = soup.find_all('div', class_='panel-body')

            for panel_body in panel_bodies:
                # Find p tags inside the panel-body div
                p_tags = panel_body.find_all('p')
                # Extract text from each p tag
                text = ' '.join([p.get_text().strip() for p in p_tags])
                # Append text to data list

            # education = profile.find('div', clss_='panel-body').get_text()
            # office_phone = profile.find('div', clss_='panel-body').get_text()

            # Append data to list
            data.append([name, email, text, ]) # education, office_phone

        return data
    except Exception as e:
        print("An exception happened while scraping")


def save_to_csv(data, filename='profile_data.csv'):
    df = pd.DataFrame(data, columns=['Name', 'Email','Research', ]) # 'Education', 'Phone'
    df.to_csv(filename, index=False)


if __name__ == "__main__":
    base_url = 'https://cs.txstate.edu/accounts/profiles/'  # Replace with the actual URL
    profile_data = scrape_profile_data(base_url)
    profile_arr = ["hs15", "ma04", "t_i24", "sox16", "ok11"]
    scraped_data = []
    for item in profile_arr:
        url = base_url + item
        text_data = scrape_profile_data(url)
        scraped_data.append(text_data)
    save_to_csv(profile_data)
