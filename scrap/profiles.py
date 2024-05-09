import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_profile_data(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        profiles = soup.find_all('body', class_='home-page')

        data = []
        for profile in profiles:
            get_prof_name = profile.find('h1').text.strip().split()
            name = " ".join(item for item in get_prof_name)

            email_image = profile.find('img', class_='email-image')
            if email_image:
                email_text = email_image.get('alt', '').split('email', 1)[
                    -1].strip()
                email = email_text.split(' ')[0]
            else:
                email = ''

            panel_body = profile.find('div', class_='panel-body')
            if panel_body:
                p_tags = panel_body.find_all('p')
                research_text = ' '.join([word.strip() for p in p_tags for word in p.get_text().split() if word.strip()])

            else:
                research_text = ''

            data.append([name, email, research_text])

        return data
    except Exception as e:
        print("An exception happened while scraping:", e)


def save_to_csv(data, filename='profile_data.csv'):
    df = pd.DataFrame(data, columns=['Name', 'Email', 'Research'])
    df.to_csv(filename, index=False)


if __name__ == "__main__":
    base_url = 'https://cs.txstate.edu/accounts/profiles/'
    profile_data = scrape_profile_data(base_url)
    profile_arr = ["hs15/", "ma04/", "t_i24/", "sox16/", "ok11/", "zz11/", "k_y47/", "j_t463/", "js236/", "vgt16/",
                   "asf93/", "aq10/", "rp31/", "wp01/", "ueg11/", "hn12/", "tgo10/", "v_m137/", "t_l81/", "fsr11/",
                   "ok11/", "lk04/", "sox16/", "t_i24/", "ch01/", "mg65/", "hag10/", "jg66/", "xc10/", "mb92/", "ma04/"]
    scraped_data = []
    for item in profile_arr:
        url = base_url + item
        text_data = scrape_profile_data(url)
        scraped_data.extend(text_data)
        save_to_csv(scraped_data)
