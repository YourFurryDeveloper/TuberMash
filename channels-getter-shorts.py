from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os
import json

options = Options()
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options)
driver.get("https://www.youtube.com/shorts")

# -----| SET THE AMOUNT OF CHANNELS HERE |-----
channelsToGet = 100

time.sleep(5)

print("\nGetting elements...\n\n")

final_channels = {}
i = 0

for i in range(channelsToGet):
    i += 1
    print(f"Getting channel ({str(i)})")
    channelName = driver.find_element(By.CSS_SELECTOR, 'a.yt-core-attributed-string__link.yt-core-attributed-string__link--call-to-action-color.yt-core-attributed-string--link-inherit-color')
    pfpElement = driver.find_element(By.CSS_SELECTOR, 'img.yt-core-image.yt-spec-avatar-shape__image.yt-core-image--fill-parent-height.yt-core-image--fill-parent-width.yt-core-image--content-mode-scale-to-fill.yt-core-image--loaded')
    channelPfp = pfpElement.get_attribute('src')
    print(f"Channel handle: {channelName.text} | Channel PFP: {channelPfp}\n")
    final_channels[channelName.text] = channelPfp
    time.sleep(1.5)
    if i == 1:
        nextBtn = driver.find_element(By.CSS_SELECTOR, 'button.yt-spec-button-shape-next.yt-spec-button-shape-next--text.yt-spec-button-shape-next--mono.yt-spec-button-shape-next--size-xl.yt-spec-button-shape-next--icon-button.yt-spec-button-shape-next--enable-backdrop-filter-experiment')
        nextBtn.click()
    else:
        nextBtnList = driver.find_elements(By.CSS_SELECTOR, 'button.yt-spec-button-shape-next.yt-spec-button-shape-next--text.yt-spec-button-shape-next--mono.yt-spec-button-shape-next--size-xl.yt-spec-button-shape-next--icon-button.yt-spec-button-shape-next--enable-backdrop-filter-experiment')
        nextBtn = nextBtnList[1]
        nextBtn.click()

print("\nCreated dictionary, dumping channels to channels.json...")
with open("channels.json", "w") as f:
    json.dump(final_channels, f, indent=4)
    
print("\nDone! :3")

driver.quit()
