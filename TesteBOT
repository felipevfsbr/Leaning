from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

navegador = webdriver.Chrome()

navegador.get("https://www.magazineluiza.com.br/")
navegador.find_element(By.XPATH, '/html/body/div[1]/div/main/section[1]/div[2]/header/div/div[1]/ul[2]/li[1]/a').click()
WebDriverWait(navegador, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/div[1]/div/div["
                                                                        "1]/header/div/div[1]/div/div/div[2]/div["
                                                                        "1]/div[1]/div[2]/a"))).click()
navegador.find_element(By.NAME, "login").click()
