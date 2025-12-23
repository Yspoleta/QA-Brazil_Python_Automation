import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import data
import helpers


# Definição da classe da página, dos localizadores e do métdo na classe
class UrbanRoutesPage:

    # Localizadores como atributos de classe
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')

    PERSONAL_OPTION_LOCATOR = (By.XPATH, '//div[text()="Personal"]')
    TAXI_ICON_LOCATOR = (By.XPATH, "//img[contains(@src, 'b0be3054.svg') or contains(@src, '9a02abc6.svg')]")#Busca imagem do taxi ativo ou não.
    TAXI_CALL_LOCATOR = (By.CLASS_NAME, "button.round")
    COMFORT_ICON_LOCATOR = (By.XPATH, "(//img[@alt='Comfort'])[1]")

    ADD_PHONE_NUMBER_BUTTON_LOCATOR = (By.CLASS_NAME, "np-text")
    NEXT_BUTTON_LOCATOR = (By.XPATH, "//button[contains(text(), 'Próximo')]")
    PHONE_CODE_LOCATOR = (By.XPATH,"(//*[@id='code'])[1]")
    PHONE_NUMBER_FIELD_LOCATOR = (By.XPATH,"//input[@id='phone']")
    CONFIRM_BUTTON_LOCATOR = (By.XPATH,"//button[contains(text(), 'Confirmar')]")
    DIV_COMFORT_ICON_LOCATOR = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[1]/div[5]")

    PAYMENT_METHOD_LOCATOR = (By.CLASS_NAME, "pp-text")
    ADICIONAR_CARTAO_LOCATOR = (By.XPATH, "(//*[@class = 'pp-title'])[2]")
    ADD_CARD_NUMBER_BUTTON_LOCATOR = (By.XPATH, "//*[@name = 'number']")

    #CARD_NUMBER_FIELD_LOCATOR = (By.XPATH, "//*[@id='number']")#Está duplicado com a linha de cima
    CARD_CODE_LOCATOR = (By.XPATH,"//*[@name='code']")
    ADICIONAR_LOCATOR = (By.XPATH, "(//*[contains(@type, 'submit')])[3]")
    CONFIRMED_PAYMENT_METHOD_LOCATOR = (By.XPATH, "(//*[@class = 'pp-title'])[2]")

    SEND_MESSAGE_FOR_DRIVER_LOCATOR = (By.XPATH,"//input[@id='comment']")
    #SEND_MESSAGE_FOR_DRIVER_LOCATOR = (By.ID,"comment") Equivalente ao que esta na linha 37.
    BLANKET_AND_STUFF_LOCATOR = (By.XPATH, "//div[contains(@class,'r-sw-container')][.//div[@class='r-sw-label' and normalize-space()='Cobertor e lençóis']]//div[contains(@class,'switch')]")
    BLANKET_AND_STUFF_ACTIVE_LOCATOR = (By.XPATH, "//div[contains(@class,'r-sw-container')][.//div[@class='r-sw-label' and normalize-space()='Cobertor e lençóis']]//div[contains(@class,'switch')]//input")

    ADD_ICECREAM_BUTTON_LOCATOR = (By.XPATH,"(//*[contains(@class, 'counter-plus')])[1]")
    AMOUNT_OF_ICE_CREAMS_LOCATOR = (By.XPATH, "(//*[contains(@class, 'counter-value')])[1]")

    DIGIT_THE_NUMBER_AND_THE_ORDER_BUTTON = (By.XPATH, "//*[contains(@class, 'smart-button-main')]")
    SEARCH_CAR_LOCATOR = (By.XPATH,'//div[text()="Buscar carro"]')


    def __init__(self, driver):
        self.driver = driver  # Inicializar o driver

    def enter_from_and_to_location(self, from_text, to_text):
        # Inserir De
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)
        # Inserir Para
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def get_from_and_to_fields_values(self):
        return self.driver.find_element(*self.FROM_LOCATOR).get_property('value'),self.driver.find_element(*self.TO_LOCATOR).get_property('value')


    def click_personal_option(self):
        # Clicar em Personal
        self.driver.find_element(*self.PERSONAL_OPTION_LOCATOR).click()

    def click_taxi_icon(self):
        # Clicar no ícone de Scooter
        self.driver.find_element(*self.TAXI_ICON_LOCATOR).click()

    def click_taxi_call(self):
        self.driver.find_element(*self.TAXI_CALL_LOCATOR).click()

    def click_comfort_icon(self):
        wait = WebDriverWait(self.driver, 10)
        comfort = wait.until(EC.element_to_be_clickable(self.COMFORT_ICON_LOCATOR))
        comfort.click()

    def get_comfort_icon_classes(self):
        return self.driver.find_element(*self.DIV_COMFORT_ICON_LOCATOR).get_attribute('class')    #Retorna uma string com todas as classes do objeto(nesse caso confort icon)

    def get_placeholder_phone(self):
        return self.driver.find_element(*self.ADD_PHONE_NUMBER_BUTTON_LOCATOR).text    #Vai recuperar o texto do objeto.

    def click_phone_number(self):
        self.driver.find_element(*self.ADD_PHONE_NUMBER_BUTTON_LOCATOR).click()

    def enter_number(self, number):
        self.driver.find_element(*self.PHONE_NUMBER_FIELD_LOCATOR).send_keys(number)

    def enter_phone_code(self):
        phone_code = helpers.retrieve_phone_code(self.driver)
        self.driver.find_element(*self.PHONE_CODE_LOCATOR).send_keys(phone_code)

    def click_next_button(self):
        # Esperar o botão ficar clickavel.
        wait = WebDriverWait(self.driver, 15)
        next_button = wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON_LOCATOR))
        next_button.click()

    def click_confirm_button(self):
        self.driver.find_element(*self.CONFIRM_BUTTON_LOCATOR).click()

     #Abre os metodos de pagamento (possibilitando adicionar o cartão)
    def click_payment_method(self):
        self.driver.find_element(*self.PAYMENT_METHOD_LOCATOR).click()

    #clicka no botão de adicionar cartão
    def click_add_card_button(self):
        self.driver.find_element(*self.ADICIONAR_CARTAO_LOCATOR).click()

    #Adiciona numero do cartão
    def enter_card_number(self, number):
        self.driver.find_element(*self.ADD_CARD_NUMBER_BUTTON_LOCATOR).send_keys(number)

    #Adiciona o código do cartão
    def enter_card_code(self, code):
        self.driver.find_element(*self.CARD_CODE_LOCATOR).send_keys(code)

    #Clickar no botão "Adicionar"
    def click_adicionar_button(self):
        self.driver.find_element(*self.ADICIONAR_LOCATOR).click()

    #Confirmar que o cartão foi adicionado
    def get_payment_method(self):
        return self.driver.find_element(*self.CONFIRMED_PAYMENT_METHOD_LOCATOR).text

    #Clicka em "Mandar mensagem para o motorista e escreve a mensagem
    def click_send_message_for_driver(self, text):
        self.driver.find_element(*self.SEND_MESSAGE_FOR_DRIVER_LOCATOR).send_keys(text)

    #Confirmar que a mensagem foi escrita
    def get_message_for_driver(self):
        return self.driver.find_element(*self.SEND_MESSAGE_FOR_DRIVER_LOCATOR).get_attribute('value')

    #Clicar no botão "Cobertor e Lençóis"
    def click_blanket_and_handkerchiefs_option(self):
        self.driver.find_element(*self.BLANKET_AND_STUFF_LOCATOR).click()

    #Confirmar que o botão "Cobertor e Lençóis" foi clickado
    def get_blanket_and_handkerchiefs_option_checked(self):
        return self.driver.find_element(*self.BLANKET_AND_STUFF_ACTIVE_LOCATOR).is_selected()

    #Adicionar os dois sorvetes
    def add_ice_cream(self):
        self.driver.find_element(*self.ADD_ICECREAM_BUTTON_LOCATOR).click()

    #Confirmar que tem dois sorvetes selecionados.
    def get_amount_of_ice_creams(self):
        return self.driver.find_element(*self.AMOUNT_OF_ICE_CREAMS_LOCATOR).text

    #Clickar no botão "Digitar o numero e o pedido"
    def click_digit_the_number_and_the_order(self):
        self.driver.find_element(*self.DIGIT_THE_NUMBER_AND_THE_ORDER_BUTTON).click()

    #Confirmar que chegou na aba "Buscar carro"
    def get_search_car_page(self):
        return self.driver.find_element(*self.SEARCH_CAR_LOCATOR).text




