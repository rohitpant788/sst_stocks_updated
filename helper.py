import csv
import datetime
import os

import yfinance as yf
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import config
import helper
import kite_automation_config
import time


def get_historical_data(stock_name, lookback_days=40):
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=lookback_days)
    print(f'Getting historical data for {stock_name} from {start_date} to {end_date}')
    stock_data = yf.download(stock_name + '.NS', start=start_date, end=end_date)
    return stock_data


driver = None

driver = None


def get_driver():
    global driver
    if driver is None:
        # driver = webdriver.Chrome(kite_automation_config.PATH)
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver


# def get_driver():
#     global driver
#     if driver is None:
#         # Specify the custom installation path here
#         custom_path = kite_automation_config.PATH
#
#         # Create ChromeOptions and set the executable path
#         options = webdriver.ChromeOptions()
#         options.binary_location = custom_path  # Set the path to the ChromeDriver executable
#
#         # Initialize ChromeDriver with ChromeOptions
#         driver = webdriver.Chrome(options=options)
#     return driver


def login_kite_in_browser():
    driver = get_driver()
    driver.maximize_window()

    driver.get(kite_automation_config.KITE_LOGIN_URL)

    print(driver.title)

    # Access the environment variables using os.getenv
    kite_login = os.getenv("KITE_LOGIN")
    kite_password = os.getenv("KITE_PASSWORD")

    helper.input_field_by_xpath(driver, kite_automation_config.KITE_USER_ID_XPATH, kite_login)
    helper.input_field_by_xpath(driver, kite_automation_config.KITE_PASSWORD_XPATH,
                                kite_password)
    helper.click_label_by_xpath(driver, kite_automation_config.KITE_LOGIN_BUTTON_XPATH)


# def click_label_by_xpath(driver, xpath, wait_time_sec=300):
#     wait = WebDriverWait(driver, wait_time_sec)
#     wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
#     element = driver.find_element(By.XPATH, xpath)
#     if element.is_displayed():
#         element.click()

def click_label_by_xpath(driver, xpath, wait_time_sec=300):
    try:
        wait = WebDriverWait(driver, wait_time_sec)
        wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        element = driver.find_element(By.XPATH, xpath)
        if element.is_displayed():
            element.click()
            return True  # Return True if the operation is successful
    except Exception as e:
        print(f"An exception occurred: {str(e)}")
    return False  # Return False for any exception


# def input_field_by_xpath(driver, xpath, field_value, wait_time_sec=300):
#     wait = WebDriverWait(driver, wait_time_sec)
#     wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
#     element = driver.find_element(By.XPATH, xpath)
#     if element.is_displayed():
#         time.sleep(kite_automation_config.DELAY_IN_SEC)
#         element.clear()
#         element.send_keys(Keys.CONTROL + 'a')
#         element.send_keys(Keys.DELETE)
#         element.send_keys(field_value)

def input_field_by_xpath(driver, xpath, field_value, wait_time_sec=300):
    try:
        wait = WebDriverWait(driver, wait_time_sec)
        wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        element = driver.find_element(By.XPATH, xpath)
        if element.is_displayed():
            time.sleep(kite_automation_config.DELAY_IN_SEC)
            element.clear()
            element.send_keys(Keys.CONTROL + 'a')
            element.send_keys(Keys.DELETE)
            element.send_keys(field_value)
            return True  # Return True if the operation is successful
    except Exception as e:
        print(f"An exception occurred: {str(e)}")
    return False  # Return False for any exception


def delete_all_gtt_orders():
    driver = get_driver()
    time.sleep(kite_automation_config.DELAY_IN_SEC)
    element_order_btn = driver.find_element(By.XPATH, kite_automation_config.KITE_ORDERS_MENU_XPATH)
    if element_order_btn.is_displayed():
        element_order_btn.click()

    time.sleep(kite_automation_config.DELAY_IN_SEC)
    element_gtt_menu_btn = driver.find_element(By.XPATH, kite_automation_config.KITE_GTT_MENU_XPATH)
    if element_gtt_menu_btn.is_displayed():
        element_gtt_menu_btn.click()

    time.sleep(kite_automation_config.DELAY_IN_SEC)
    if check_exists_by_xpath(kite_automation_config.KITE_GTT_DOWNLOAD_CSV_BTN_XPATH):
        element_download_gtt_orders_btn = driver.find_element(By.XPATH,
                                                              kite_automation_config.KITE_GTT_DOWNLOAD_CSV_BTN_XPATH)
        if element_download_gtt_orders_btn.is_displayed():
            element_download_gtt_orders_btn.click()

        time.sleep(kite_automation_config.DELAY_IN_SEC)
        # Read the gtt-list.csv file from downloads directory
        gtt_file = r'C:\Users\Rohit\Downloads\gtt-list.csv'
        with open(gtt_file) as file:
            reader = csv.reader(file)
            for i in range(1, len(list(reader))):
                delete_gtt_order()

        # Delete the gtt_file
        os.remove(gtt_file)


def check_exists_by_xpath(xpath):
    driver = get_driver()
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True


def delete_gtt_order():
    driver = get_driver()
    time.sleep(kite_automation_config.DELAY_IN_SEC)
    element_order_btn = driver.find_element(By.XPATH, kite_automation_config.KITE_ORDERS_MENU_XPATH)
    if element_order_btn.is_displayed():
        element_order_btn.click()

    time.sleep(kite_automation_config.DELAY_IN_SEC)
    element_gtt_menu_btn = driver.find_element(By.XPATH, kite_automation_config.KITE_GTT_MENU_XPATH)
    if element_gtt_menu_btn.is_displayed():
        element_gtt_menu_btn.click()

    # time.sleep(kite_automation_config.DELAY_IN_SEC)
    achain = ActionChains(driver)
    time.sleep(kite_automation_config.DELAY_IN_SEC)
    element_gtt_hover_locator = driver.find_element(By.XPATH,
                                                    kite_automation_config.KITE_GTT_ORDER_HOVER_SELECTOR_XPATH)
    achain.move_to_element(element_gtt_hover_locator).perform()
    time.sleep(kite_automation_config.DELAY_IN_SEC)
    if element_gtt_hover_locator.is_displayed():
        element_gtt_order_hover_del_btn = driver.find_element(By.XPATH,
                                                              kite_automation_config.KITE_GTT_ORDER_HOVER_DELETE_XPATH)
        if element_gtt_order_hover_del_btn.is_displayed():
            element_gtt_order_hover_del_btn.click()
            time.sleep(kite_automation_config.DELAY_IN_SEC)
            element_gtt_del_btn = driver.find_element(By.XPATH, kite_automation_config.KITE_GTT_ORDER_DELETE_BTN_XPATH)
            if element_gtt_del_btn.is_displayed():
                element_gtt_del_btn.click()
                time.sleep(kite_automation_config.DELAY_IN_SEC)
                element_gtt_del_btn_popup = driver.find_element(By.XPATH,
                                                                kite_automation_config.KITE_GTT_ORDER_DELETE_BTN_FROM_POPUP_XPATH)
                if element_gtt_del_btn_popup.is_displayed():
                    element_gtt_del_btn_popup.click()


def place_buy_order(sym, gtt_order_price):
    driver = get_driver()
    time.sleep(kite_automation_config.DELAY_IN_SEC)
    element_order_btn = driver.find_element(By.XPATH, kite_automation_config.KITE_ORDERS_MENU_XPATH)
    if element_order_btn.is_displayed():
        element_order_btn.click()

    time.sleep(kite_automation_config.DELAY_IN_SEC)
    element_gtt_menu_btn = driver.find_element(By.XPATH, kite_automation_config.KITE_GTT_MENU_XPATH)
    if element_gtt_menu_btn.is_displayed():
        element_gtt_menu_btn.click()

    time.sleep(kite_automation_config.DELAY_IN_SEC)
    if check_exists_by_xpath(kite_automation_config.KITE_NEW_GTT_BTN_XPATH):
        element_new_gtt_btn = driver.find_element(By.XPATH, kite_automation_config.KITE_NEW_GTT_BTN_XPATH)
        if element_new_gtt_btn.is_displayed():
            element_new_gtt_btn.click()
    else:
        element_new_gtt_btn_pop_up = driver.find_element(By.XPATH,
                                                         kite_automation_config.KITE_NEW_GTT_BTN_FROM_POPUP_XPATH)
        if element_new_gtt_btn_pop_up.is_displayed():
            element_new_gtt_btn_pop_up.click()

    time.sleep(kite_automation_config.DELAY_IN_SEC)
    element_search_stock_text = driver.find_element(By.XPATH, kite_automation_config.KITE_SEARCH_STOCK_XPATH)
    if element_search_stock_text.is_displayed():
        element_search_stock_text.send_keys(sym)

    time.sleep(kite_automation_config.DELAY_IN_SEC)
    element_search_stock_result_text = driver.find_element(By.XPATH,
                                                           kite_automation_config.KITE_SEARCH_STOCK_RESULT_XPATH)
    if element_search_stock_result_text.is_displayed():
        element_search_stock_result_text.click()

    time.sleep(kite_automation_config.DELAY_IN_SEC)
    element_create_gtt_btn = driver.find_element(By.XPATH, kite_automation_config.KITE_CREATE_GTT_BTN_XPATH)
    if element_create_gtt_btn.is_displayed():
        element_create_gtt_btn.click()

    # I/p for GTT
    trigger_price = format_num_filter(gtt_order_price)
    buy_price = format_num_filter(1.005 * gtt_order_price)
    quantity = get_quantity_of_stock_for_buy(buy_price)

    time.sleep(kite_automation_config.DELAY_IN_SEC)
    element_gtt_trigger_price = driver.find_element(By.XPATH, kite_automation_config.KITE_GTT_TRIGER_PRICE_XPATH)
    if element_gtt_trigger_price.is_displayed():
        element_gtt_trigger_price.clear()
        element_gtt_trigger_price.send_keys(trigger_price)

    time.sleep(kite_automation_config.DELAY_IN_SEC)
    element_gtt_buy_price = driver.find_element(By.XPATH, kite_automation_config.KITE_GTT_ORDER_PRICE_XPATH)
    if element_gtt_buy_price.is_displayed():
        element_gtt_buy_price.clear()
        element_gtt_buy_price.send_keys(buy_price)

    time.sleep(kite_automation_config.DELAY_IN_SEC)
    element_gtt_order_price = driver.find_element(By.XPATH, kite_automation_config.KITE_GTT_ORDER_QTY_XPATH)
    if element_gtt_order_price.is_displayed():
        element_gtt_order_price.clear()
        element_gtt_order_price.send_keys(quantity)

    time.sleep(kite_automation_config.DELAY_IN_SEC)
    element_gtt_order_sub_btn = driver.find_element(By.XPATH, kite_automation_config.KITE_GTT_ORDER_SUBMIT_BTN_XPATH)
    if element_gtt_order_sub_btn.is_displayed():
        element_gtt_order_sub_btn.click()

    return None


def get_quantity_of_stock_for_buy(gtt_buy_price):
    money_available_per_trade = config.TOTAL_MONEY_PER_TRADE
    calculated_quantity = money_available_per_trade / gtt_buy_price

    # Check if calculated_quantity is 0, and replace it with 1
    if calculated_quantity < 1:
        quantity = 1
    else:
        quantity = int(format_num_filter(calculated_quantity))

    print(f' Quantity for this trade is {quantity}')
    return quantity


def format_num_filter(number):
    return round(number, 0)


sym_where_we_have_position = set()
