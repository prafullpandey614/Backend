# myapp/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup
from facebook_scraper import get_profile
from truecallerpy import search_phonenumber
import pandas as pd
#abandoned
def initialize_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://web.whatsapp.com")
    driver.implicitly_wait(25)
    return driver

@require_GET
@csrf_exempt
def scrape_data(request):
    phone_number = request.GET.get("phone_number", "8268291167")
    username = request.GET.get("username", "virat")
    email_address = "akshatbjain.aj@gmail.com"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
    }

    driver = initialize_driver()

    whatsapp_data = {
        "Registered": None,
        "Name": None,
        "Status": None,
        "Last Seen": None,
        "Profile Picture": None,
    }

    driver.get(f"https://api.whatsapp.com/send?phone=91{phone_number}")
    time.sleep(5)

    window_1 = driver.find_element(By.LINK_TEXT, "Continue to Chat")
    window_1.click()

    window_2 = driver.find_element(By.LINK_TEXT, "use WhatsApp Web")
    window_2.click()

    try:
        chat_screen = driver.find_element(By.CSS_SELECTOR, '[class="_2lSWV _3cjY2 copyable-area"]')
        whatsapp_data["Registered"] = "Yes"

        try:
            last_seen = driver.find_element(By.CSS_SELECTOR, '[class="ggj6brxn gfz4du6o r7fjleex lhj4utae le5p0ye3 _11JPr selectable-text copyable-text"]')
            whatsapp_data["Last Seen"] = last_seen.text
        except NoSuchElementException:
            print("WhatsApp last scene is disabled!")

        driver.find_element(By.CSS_SELECTOR, '[title="Profile Details"]').click()

        name_node = driver.find_element(By.CSS_SELECTOR, '[data-testid="contact-info-subtitle"]').text
        check_whats_scraped_name_or_number = "".join(name_node.split())

        if phone_number == check_whats_scraped_name_or_number[3:]:
            try:
                whatsapp_data["Name"] = driver.find_element(By.CSS_SELECTOR, '[class="enbbiyaj e1gr2w1z hp667wtd"]').text
            except NoSuchElementException:
                print("No name found on WhatsApp")
        else:
            whatsapp_data["Name"] = name_node

        try:
            profile_pic_container = driver.find_element(By.CSS_SELECTOR, '[style="height: 200px; width: 200px; cursor: pointer;"]')
            profile_pic = profile_pic_container.find_element(By.TAG_NAME, "img")
            whatsapp_data["Profile Picture"] = profile_pic.get_attribute("src")
        except NoSuchElementException:
            print("No Display picture found on WhatsApp")

        try:
            status = driver.find_element(By.CSS_SELECTOR, '[class="cw3vfol9 _11JPr selectable-text copyable-text"]')
            whatsapp_data["Status"] = status.get_attribute("title")
        except NoSuchElementException:
            print("No status found on WhatsApp!")

    except NoSuchElementException:
        whatsapp_data["Registered"] = "No"
        print("User not found on WhatsApp!")

    truecaller_data = {"Registered": None, "Name": None, "Email id": None}

    try:
        id = 'a1i0P--gTcTrhFL-cyftjtOM_bFbSibQvojcniZznUB19Hre4oiEwBH946s33NB1'
        owner = search_phonenumber(phone_number, 'IN', id)
        truecaller_data["Registered"] = 'Yes'
        truecaller_data["Name"] = owner['data'][0]['name']
        truecaller_data["Address"] = owner['data'][0]['addresses']
        truecaller_data["Email id"] = owner['data'][0].get('internetAddresses', None)[0]['id']
    except:
        print("User/Email not found in truecaller!")

    facebook_data = {
        "Registered": None,
        "Name": None,
        "Username": None,
        "Profile URL": None,
        "Cover URL": None,
    }

    try:
        scrap_fb = get_profile(username, cookies="facebookCookies.txt")
        url = f"https://www.facebook.com/{username}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        if len(scrap_fb) > 5:
            facebook_data["Registered"] = "Yes"
            facebook_data["Name"] = scrap_fb["Name"]
            facebook_data["Username"] = response.url.split("https://www.facebook.com/")[1]
            facebook_data["Profile URL"] = scrap_fb["profile_picture"]
            facebook_data["Cover URL"] = scrap_fb["cover_photo"]

    except:
        facebook_data["Registered"] = "No"
        print("Username not found on FaceBook!")

    url = f"https://gpay.app.goo.gl/{phone_number}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    registered_element = soup.find("div", {"class": "DfTQ5d"})
    registered = registered_element.text if registered_element else None

    name = registered
    upi_id_elements = soup.find_all("div", {"class": "DfTQ5d"})
    upi_ids = [element.text for element in upi_id_elements]

    gpay_data = {"Registered": registered, "Name": name, "UPI IDs": upi_ids}

    results = []
    results.append(("WhatsApp", whatsapp_data))
    results.append(("Truecaller", truecaller_data))
    results.append(("Facebook", facebook_data))
    results.append(("Gpay", gpay_data))

    df = pd.DataFrame(results, columns=["Platform", "Data"])
    print(df)

    return JsonResponse(results, safe=False)

# myproject/urls.py
from django.urls import path
from .views import scrape_data

urlpatterns = [
    path('scrape-data/', scrape_data, name='scrape_data'),
]

# myproject/settings.py
INSTALLED_APPS = [
    # ...
    'myapp',
]

ROOT_URLCONF = 'myproject.urls'
