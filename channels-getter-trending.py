from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os
import json

options = Options()
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options)
driver.get("https://www.youtube.com/feed/trending")

time.sleep(5)
#input("Press enter to begin >>> ")

css_selector_imgs = (
    ".yt-core-image.yt-spec-avatar-shape__image."
    "yt-core-image--fill-parent-height.yt-core-image--fill-parent-width."
    "yt-core-image--content-mode-scale-to-fill.yt-core-image--loaded"
)

css_selector_names = (
    ".yt-simple-endpoint.style-scope.yt-formatted-string"
)

print("\nGetting elements...")

for i in range(15):
    nameElements = driver.find_elements(By.CSS_SELECTOR, css_selector_names)[:30]
    driver.execute_script("window.scrollBy(0,5000);")
    time.sleep(1)

print("\nFound elements, getting links...")
name_list = [element.get_attribute("href") for element in nameElements if element.get_attribute("href")]

print("\nFound links, getting PFPS (this may take a while)...")
seen = set()
channels_pruned = [x for x in name_list if not (x in seen or seen.add(x))]

final_channels = {
    
}

i = 0
for channel in channels_pruned:
    driver.get(channel)
    time.sleep(1)
    
    i += 1
    print(f"Found channel PFP ({str(i)})")
    
    channel = channel.strip("https://www.youtube.com/")
    
    imgElements = driver.find_elements(By.CSS_SELECTOR, css_selector_imgs)
    src_list = [element.get_attribute("src") for element in imgElements if element.get_attribute("src")]
    
    final_channels[channel] = src_list[0]

print("\nCreated dictionary, dumping channels to channels.json...")
with open("channels.json", "w") as f:
    json.dump(final_channels, f, indent=4)
    
print("\nDone! :3")

driver.quit()
