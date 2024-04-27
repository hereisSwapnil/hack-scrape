from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

def scrapeDevfolio():
    hackathons = []
    for urlType in ["open", "upcoming"]:
        url = "https://devfolio.co/hackathons/"+urlType
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.set_window_size(1920, 1080)

        driver.get(url)
        reachedBottom = False
        
        while(not reachedBottom):
            source = driver.page_source
            soup = bs(source, "html.parser")
            time.sleep(5)
            for i in range(0, 5):
                driver.execute_script("window.scrollBy(0, 1000)")
                time.sleep(2)
            reachedBottom = True
        time.sleep(5)
        source = driver.page_source
        soup = bs(source, "html.parser")
        hackthonDivs = soup.find_all("div", attrs={"class": "CompactHackathonCard__StyledCard-sc-4a10fa2a-0"})
        
        for div in hackthonDivs:
            isFeatured = False
            hackathonLink = div.find("a", attrs={"class": "Link__LinkBase-sc-af40de1d-0 lkflLS"}).get("href")
            hackathonName = div.find("h3").text
            detailDiv = div.find("div", attrs={"class": "sc-hKMtZM sc-gKXOVf hBeBfX"})
            detailDivs = detailDiv.find_all("div")
            hackathonDate = detailDivs[2].text
            hackathonLocation = detailDivs[0].text
            prizes = "None"
            hackathonStatus = detailDivs[1].text
            
            try:
                participants = div.find("p", attrs={"class": "sc-dkzDqf hDculK"}).text
            except:
                participants = "0"
            
            themesDiv = div.find_all("div", attrs={"class": "sc-hKMtZM jmNVBK"})
            themes = []
            for theme in themesDiv:
                themes.append(theme.text.strip())
            hackathon = {
                "link": hackathonLink.strip(),
                "name": hackathonName.strip(),
                "date": hackathonDate.strip().replace("Starts ", ""),
                "location": hackathonLocation.strip(),
                "prizes": prizes,
                "participants": participants.replace("participating", "").strip(),
                "themes": themes,
                "status": hackathonStatus.strip(),
                "featured": isFeatured,
                "source": "Devfolio"
            }
            hackathons.append(hackathon)
        
    #     # print(hackathonLink + "\n" +  hackathonName + "\n" + hackathonDate + "\n" + hackathonLocation + "\n" + prizes + "\n" + participants + "\n" + themeText + "\n\n")
    
    return hackathons

if __name__ == "__main__":
    print(scrapeDevfolio())