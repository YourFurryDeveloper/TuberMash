from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os
import json

options = Options()
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options)

# Socialblade URL (You chan change this to any Socialblade page)
driver.get("https://socialblade.com/youtube/lists/top/100/sb/games/US")

# -----| SET THE AMOUNT OF CHANNELS HERE |-----
channelsToGet = 100

# Set debug on or off (Set to False if you're doing a big number.)
debug_output = True

time.sleep(5)

css_selector_imgs = (
    ".inline-flex.ml-3"
)

css_selector_names = (
    ".px-4.h-full"
)

print("\nGetting elements...\n\n")

final_channels = {}

channelNames = driver.find_elements(By.CSS_SELECTOR, css_selector_names)
channelImgs = driver.find_elements(By.CSS_SELECTOR, css_selector_imgs)

for i in range(channelsToGet):
    if debug_output: print(f"Getting channel ({str(i)})")

    pfpElement = channelImgs[i]
    channelName = channelNames[i]

    channelPfp = pfpElement.get_attribute('src')
    if debug_output: print(f"Channel handle: {channelName.text} | Channel PFP: {channelPfp}\n")
    final_channels[channelName.text] = channelPfp

print("\nCreated dictionary, dumping channels to channels.json...")
with open("channels.json", "w") as f:
    json.dump(final_channels, f, indent=4)
    
print("\nDone! :3")

driver.quit()
