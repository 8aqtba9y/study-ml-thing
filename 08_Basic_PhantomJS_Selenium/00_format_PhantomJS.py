from selenium import webdriver

# url = "http://www.naver.com"
url = "https://nid.naver.com/nidlogin.login"

# Retrieving PhantomJS
browser = webdriver.PhantomJS()

# 初期化のため、3秒間待機
browser.implicitly_wait(3)

# URLの読み込み
browser.get(url)

# スクリーンショットし保存
browser.save_screenshot("00_screenshot.png")

# ブラウザ終了
browser.quit()