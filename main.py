import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import helpers
from pages import UrbanRoutesPage
import time


class TestUrbanRoutes:


    @classmethod
    def setup_class (cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}

        options = Options()
        options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

        cls.driver = webdriver.Chrome(options=options)
        cls.driver.implicitly_wait(5)


        # Verifique se a URL não expirou
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não é possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução")

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)#Abre uma pagina no navegador.
        routes_page = UrbanRoutesPage(self.driver)#Cria objeto
        address_from = data.ADDRESS_FROM
        address_to = data.ADDRESS_TO
        routes_page.enter_from_and_to_location(address_from, address_to)
        routes_page.conferir_preenchimento_correto()

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.ADDRESS_FROM
        address_to = data.ADDRESS_TO
        routes_page.enter_from_and_to_location(address_from, address_to)
        routes_page.conferir_preenchimento_correto()
        #Clickar no botão "Personal".
        routes_page.click_personal_option()
        time.sleep(3)
        #Escolher o botão "Taxi"
        routes_page.click_taxi_icon()
        time.sleep(3)
        #Clickar no botão "Chamar um táxi"
        routes_page.click_taxi_call()
        time.sleep(3)
        #Clickar no icone "Comfort"
        routes_page.click_comfort_icon()
        time.sleep(10)
        assert "active" in routes_page.get_comfort_icon_classes()

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.ADDRESS_FROM
        address_to = data.ADDRESS_TO
        routes_page.enter_from_and_to_location(address_from, address_to)
        routes_page.conferir_preenchimento_correto()
        # Clickar no botão "Personal".
        routes_page.click_personal_option()
        time.sleep(3)
        # Escolher o botão "Taxi"
        routes_page.click_taxi_icon()

        # Clickar no botão "Chamar um táxi"
        routes_page.click_taxi_call()

        # Clickar no icone "Comfort"
        routes_page.click_comfort_icon()
        #Clicar no espaço pra inserir o telefone
        routes_page.click_phone_number()
        #Digitar numero de telefone
        routes_page.enter_number(data.PHONE_NUMBER)
        time.sleep(3)
        #Clickar no botão "Proximo"
        routes_page.click_next_button()
        time.sleep(1)
        #Inserir o codigo do telefone
        routes_page.enter_phone_code()
        #Clickar no botão "Confirmar".
        routes_page.click_confirm_button()
        time.sleep(5)
        #Confirmar que o telefone foi adicionado.
        assert "+1 123 123 12 12" == routes_page.get_placeholder_phone()

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.ADDRESS_FROM
        address_to = data.ADDRESS_TO
        routes_page.enter_from_and_to_location(address_from, address_to)
        routes_page.conferir_preenchimento_correto()
        # Clickar no botão "Personal".
        routes_page.click_personal_option()
        time.sleep(3)
        # Escolher o botão "Taxi"
        routes_page.click_taxi_icon()

        # Clickar no botão "Chamar um táxi"
        routes_page.click_taxi_call()
        # Clickar no icone "Comfort"
        routes_page.click_comfort_icon()


        # Clickar no botão "metodo de pagamento".
        routes_page.click_payment_method()
        #Clickar em "Adicionar um cartão".
        routes_page.click_add_card_button()
        #adicionar o numero do cartão
        routes_page.enter_card_number(data.CARD_NUMBER)
        time.sleep(3)
        #Adicionar o código do cartão
        routes_page.enter_card_code(data.CARD_CODE)
        time.sleep(5)
        #Clickar no botão "Adicionar"
        routes_page.click_adicionar_button()
        time.sleep(3)
        #confirmar se o cartão foi adicionado
        assert routes_page.get_payment_method() == 'Cartão'

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.ADDRESS_FROM
        address_to = data.ADDRESS_TO
        routes_page.enter_from_and_to_location(address_from, address_to)
        routes_page.conferir_preenchimento_correto()
        # Clickar no botão "Personal".
        routes_page.click_personal_option()
        time.sleep(3)
        # Escolher o botão "Taxi"
        routes_page.click_taxi_icon()
        # Clickar no botão "Chamar um táxi"
        routes_page.click_taxi_call()
        # Clickar no icone "Comfort"
        routes_page.click_comfort_icon()
        time.sleep(5)
        # Enviar mensagem pro motorista
        routes_page.click_send_message_for_driver(data.MESSAGE_FOR_DRIVER)
        #Lembrar que é possivel fazer testes negativos também.
        time.sleep(5)
        #Confirmar que o campo foi preenchido
        assert "Pare no bar de sucos" == routes_page.get_message_for_driver()

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.ADDRESS_FROM
        address_to = data.ADDRESS_TO
        routes_page.enter_from_and_to_location(address_from, address_to)
        routes_page.conferir_preenchimento_correto()
        # Clickar no botão "Personal".
        routes_page.click_personal_option()
        # Escolher o botão "Taxi"
        routes_page.click_taxi_icon()
        # Clickar no botão "Chamar um táxi"
        routes_page.click_taxi_call()
        # Clickar no icone "Comfort"
        routes_page.click_comfort_icon()

        #Selecionar o botão "Cobertor e lençóis"
        routes_page.click_blanket_and_handkerchiefs_option()
        time.sleep(5)

        assert routes_page.get_blanket_and_handkerchiefs_option_checked()

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.ADDRESS_FROM
        address_to = data.ADDRESS_TO
        routes_page.enter_from_and_to_location(address_from, address_to)
        routes_page.conferir_preenchimento_correto()
        # Clickar no botão "Personal".
        routes_page.click_personal_option()
        # Escolher o botão "Taxi"
        routes_page.click_taxi_icon()
        # Clickar no botão "Chamar um táxi"
        routes_page.click_taxi_call()
        # Clickar no icone "Comfort"
        routes_page.click_comfort_icon()
        # Adicionar dois sorvetes.
        for i in range(2):
            routes_page.add_ice_cream()

        time.sleep(5)

        assert routes_page.get_amount_of_ice_creams() == '2'

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.ADDRESS_FROM
        address_to = data.ADDRESS_TO
        routes_page.enter_from_and_to_location(address_from, address_to)
        routes_page.conferir_preenchimento_correto()
        # Clickar no botão "Personal".
        routes_page.click_personal_option()
        time.sleep(3)
        # Escolher o botão "Taxi"
        routes_page.click_taxi_icon()
        # Clickar no botão "Chamar um táxi"
        routes_page.click_taxi_call()
        # Clickar no icone "Comfort"
        routes_page.click_comfort_icon()
        time.sleep(5)
        # Enviar mensagem pro motorista
        routes_page.click_send_message_for_driver(data.MESSAGE_FOR_DRIVER)
        # Lembrar que é possivel fazer testes negativos também.
        time.sleep(5)
        #Clickar em "Digitar o numero e o pedido"
        routes_page.click_digit_the_number_and_the_order()
        time.sleep(5)
        #reconhecer a aba "Buscar carro".
        assert  routes_page.get_search_car_page() == "Buscar carro"


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()