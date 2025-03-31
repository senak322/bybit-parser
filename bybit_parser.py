from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# настройка драйвера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# открытие страницы Bybit P2P (RUB → USDT)
url = "https://www.bybit.com/fiat/trade/otc/?actionType=1&token=USDT&fiat=RUB"
driver.get(url)

# ждем загрузки контента
time.sleep(10)  # увеличим время, чтобы страница точно успела прогрузиться

# Ищем элементы с курсами
rates_elements = driver.find_elements(By.CSS_SELECTOR, ".price-amount")

# Выводим первые 5 курсов
for rate in rates_elements[:5]:
    print("Курс:", rate.text)

# Закрываем браузер
driver.quit()