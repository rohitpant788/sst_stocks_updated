PATH="D:\\1. softwares\\chromedriver_win32\\chromedriver.exe"

DELAY_IN_SEC=1

KITE_LOGIN_URL = "https://kite.zerodha.com/"

#XPATHS
KITE_USER_ID_XPATH="//*[@id='userid']"
KITE_PASSWORD_XPATH="//*[@id='password']"
KITE_LOGIN_BUTTON_XPATH="//*[@id='container']/div/div/div/form/div[4]/button"
KITE_RISK_DISCLOSURE_XPATH="//*[@id='app']/div[6]/div/div/div[3]/div/div/div/button"
KITE_PIN_XPATH="//*[@id='pin']"
KITE_CONTINUE_BTN_XPATH="//*[@id='container']/div/div/div/form/div[3]/button"
KITE_HOLDINGS_MENU_XPATH="//*[@id='app']/div[1]/div/div[2]/div[1]/a[3]/span"
KITE_HOLDINGS_DOWNLOAD_BTN_XPATH="//*[@id='app']/div[2]/div[2]/div/div/section/div/div/div/span[3]/span"
KITE_ORDERS_MENU_XPATH="//*[@id='app']/div[1]/div/div[2]/div[1]/a[2]/span"
KITE_GTT_MENU_XPATH="//*[@id='app']/div[2]/div[2]/div[1]/a[2]/span"
KITE_NEW_GTT_BTN_XPATH="//*[@id='app']/div[2]/div[2]/div[2]/div/section/div/div/div/span[1]/button"
KITE_NEW_GTT_BTN_FROM_POPUP_XPATH="//button[@type='button']"
KITE_SEARCH_STOCK_XPATH="//*[@id='app']/div[5]/div/div/div[1]/div/div/div/div/div/input"
KITE_SEARCH_STOCK_RESULT_XPATH="//*[@id='app']/div[5]/div/div/div[1]/div/div/div/ul/div/li[1]"
KITE_CREATE_GTT_BTN_XPATH="//*[@id='app']/div[5]/div/div/div[3]/div/div/div[1]/button"
KITE_GTT_TRIGER_PRICE_XPATH="//*[@id='app']/div[4]/div/div/div/div[2]/div/div[2]/form/div/div[1]/div[2]/div/input"
KITE_GTT_ORDER_PRICE_XPATH="//*[@id='app']/div[4]/div/div/div/div[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/input"
KITE_GTT_ORDER_QTY_XPATH="//*[@id='app']/div[4]/div/div/div/div[2]/div/div[2]/form/div/div[3]/div[2]/div[1]/div/input"
KITE_GTT_ORDER_SUBMIT_BTN_XPATH="//*[@id='app']/div[4]/div/div/div/div[3]/div/div/div[2]/button[1]"

#DELETE GTT
KITE_GTT_DOWNLOAD_CSV_BTN_XPATH="//span[@class='download-csv link']"
KITE_GTT_ORDER_HOVER_SELECTOR_XPATH="//tbody/tr[1]/td[2]/span[1]/span[1]"
KITE_GTT_ORDER_HOVER_DELETE_XPATH="//span[@class='icon icon-ellipsis']"
KITE_GTT_ORDER_DELETE_BTN_XPATH="//a[normalize-space()='Delete']"
KITE_GTT_ORDER_DELETE_BTN_FROM_POPUP_XPATH="//button[@class='button-blue']"

#Secrets
# Secrets moved to Environment variables.