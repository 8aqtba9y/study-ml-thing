from selenium import webdriver

# PhantomJSドライバーを生成し、３秒間待機
browser = webdriver.PhantomJS()
browser.implicitly_wait(3)


# ログインページを開く
browser.get("https://nid.naver.com/nidlogin.login")
# idテキスト入力ボックス
element_id = browser.find_element_by_id("id")
element_id.clear()
element_id.send_keys("<ID>")
# pwテキスト入力ボックス
element_pw = browser.find_element_by_id("pw")
element_pw.clear()
element_pw.send_keys("<PW>")
browser.save_screenshot("01_screenshot_001.png")# 途中経過スクリーンショット_001

# タグがinput, クラスがbtn_global, typeがsubmitであるボタン
element_login_btn = browser.find_element_by_css_selector("input.btn_global[type=submit]")
element_login_btn.submit()
browser.save_screenshot("01_screenshot_002.png")# 途中経過スクリーンショット_002

# メールページを開く
browser.get("https://mail.naver.com/")
browser.save_screenshot("01_screenshot_003.png") # 途中経過スクリーンショット_003

# タグがstrong, クラスがmain_titleであるタイトル(;element's')
titles = browser.find_elements_by_css_selector("strong.mail_title")
# タイトルを確認
for title in titles:
    print("-", title.text)


# ブラウザを終了
browser.quit()

# Seleniumの活用方法
# 1. getでページを取得
# 2. find_element_by_idまたは、css_selectorでelementsを取得
# 3. elementの関数を利用
# 4. screenshotで確認
# 5. 再帰関数を作成し、1.2.3.4.をループ