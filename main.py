import data
from helpers import is_url_reachable


class TestUrbanDrive:
    @classmethod
    def setup_class (cls):
        if is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print('Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.')



    def test_set_route(self):
        #Adicionar em S8
        print("função criada para definir a rota")
        pass

    def test_select_plan(self):
        print("função criada para definir a rota")
        #Adicionar em S8
        pass


    def test_fill_phone_number(self):
        print("função criada para definir a rota")
        # Adicionar em S8
        pass

    def test_fill_card(self):
       print("função criada para definir a rota")
       # Adicionar em S8
       pass

    def test_comment_for_driver(self):


        # Adicionar em S8
        pass
    def test_order_blanket_and_handkerchiefs(self):

       # Adicionar em S8
       pass

    def test_order_2_ice_creams(self):

       # Adicionar em S8
        print("Função para adicionar dois sorvetes")
        for i in range(2):
        #Adicionar em S8
            pass

    def test_car_search_model_appears(self):
        # Adicionar em S8
        pass