from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Configura o WebDriver
driver = webdriver.Chrome()

# Acessa o site do Omelete
driver.get('https://www.omelete.com.br/')

# Encontra o botão de busca e clica nele
search_button = driver.find_element(By.CLASS_NAME, 'h-menu__search')
search_button.click()

# Espera até que o campo de busca seja visível e interativo
try:
    search_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, 'q'))
    )
    search_box.send_keys('Deadpool')
    search_box.send_keys(Keys.RETURN)
except TimeoutException:
    print("O campo de busca não ficou interativo a tempo.")

# Espera a página carregar os resultados
time.sleep(10)

# Captura os títulos e datas das notícias
news_items = driver.find_elements(By.CLASS_NAME, 'mark')

results = []
for item in news_items:
    title = item.find_element(By.TAG_NAME, 'h2').text
    date = item.find_element(By.CLASS_NAME, "mark__time").text
    results.append(f"{date} - {title}")

# Armazena os resultados em um arquivo .txt
with open('noticias_deadpool.txt', 'w', encoding='utf-8') as file:
    for result in results:
        file.write(result + '\n')

# Fecha o navegador
driver.quit()
