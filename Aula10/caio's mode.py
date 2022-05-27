import this


class utils:
    def convert_string_to_donout_request(self, arr) -> dict:
        __obj__ = {
            "typeDonout":arr[0],
            "qtndDonout":int(arr[1]),
            "txService":arr[2]
        }

        return __obj__

    def list_donout_requests_and_convert_to_list(self, arr:list, separatorN:int) -> list:
        __arr__ = []
        _arr_len_= (len(arr) / separatorN)
        _arr_len_ = int(_arr_len_)

        for i in range(0,len(arr),3):
            
            temp = arr[i:i+3]

            __request_obj__ = self.convert_string_to_donout_request(temp)
            __arr__.append(__request_obj__)
        return __arr__
        
    def convertStringToArr(self, string: str) -> list:
        __arr__ = string.split(' ')
        return __arr__

    def fixString(self, str:str) -> str:
        __request__ = str
        __request__ = __request__.lower()
        __request__ = __request__.replace('sim', 's')
        __request__ = __request__.replace('não', 'n')
        return __request__

    def convert_request_str_to_list(self, string: str):
        __temp_string__ = self.convertStringToArr(string)
        __temp_list__ = self.list_donout_requests_and_convert_to_list(arr=__temp_string__,separatorN=3)
        return __temp_list__

class pedido(utils): 
    def __init__(self) -> None:
        self.salvar_pedido = ""
        self.pedidos = []
        super().__init__()

    def set_pedido_string(self, pedidoStr: str) -> None:
        request = self.fixString(pedidoStr)
        self.salvar_pedido = request
        
    def get_pedidos_str(self):
        return self.salvar_pedido
    
    def get_pedidos_list(self):
        return self.pedidos

    def set_pedidos (self, arr:list):
        self.pedidos = arr
        
if __name__ == "__main__":
    salvar_pedido = 'Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s classico 10 sim Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s classico 10 sim recheado 12 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s classico 10 sim Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s classico 10 sim recheado 12 s classico 15 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s classico 10 sim Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s classico 10 sim recheado 12 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s classico 10 sim Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s classico 10 sim recheado 12 s classico 15 s recheado 2 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s classico 10 sim Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s classico 10 sim recheado 12 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s classico 10 sim Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s classico 10 sim recheado 12 s classico 15 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s classico 10 sim Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s classico 10 sim recheado 12 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s classico 10 sim Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s Classico 12 s Classico 12 s classico 8 S Classico 12 s Classico 12 s classico 8 S recheado 6 s recheado 12 n premium 4 s classico 10 sim recheado 12 s classico 15 s recheado 2 n premium 10 s'
    
    pedido = pedido()
    
    pedido.set_pedido_string(salvar_pedido)
    requestsStr: str = pedido.get_pedidos_str()

    requestsList = pedido.convert_request_str_to_list(requestsStr)
    pedido.set_pedidos(requestsList)
    requestsList = pedido.get_pedidos_list()

    listOfTypeDonout = [
        list(filter(lambda request: request['typeDonout'] == 'classico', requestsList)),
        list(filter(lambda request: request['typeDonout'] == 'recheado', requestsList)),
        list(filter(lambda request: request['typeDonout'] == 'premium', requestsList)),
    ]

    listOfTypeTx = [
        list(filter(lambda request: request['txService'] == 's', listOfTypeDonout[0])),
        list(filter(lambda request: request['txService'] == 's', listOfTypeDonout[1])),
        list(filter(lambda request: request['txService'] == 's', listOfTypeDonout[2])),
    ]

    string = f'''
    1. Quantos clientes optaram pelo tipo classico?
        R: <{len(listOfTypeDonout[0])}>

    2. Quantos clientes optaram pelo tipo recheado?
        R: <{len(listOfTypeDonout[1])}>


    3. Quantos clientes optaram pelo tipo premium?
        R: <{len(listOfTypeDonout[2])}>


    4. Qual foi a quantidade total de comprada de cada tipo de Donut?
        R: <{len(requestsList)}>

    5. Quantos clientes concordaram em pagar a taxa de servico?
        R: <{sum([len(listOfTypeTx[0]), len(listOfTypeTx[1]), len(listOfTypeTx[2])])}>

    6. Sabendo que a taxa de servico é de 10% sob o valor da compra (preco*qt)
    e os precos unitacios constam abaixo, qual a receita deste dia?
    Classico = R$ 9.90 R. < R$: {(9.9 * len(listOfTypeTx[0])) * 0.1:.2f} >
    Recheado = R$ 11.90 R. < R$: {(11.9 * len(listOfTypeTx[1])) * 0.1:.2f} >
    Premium = R$ 13.90 R. < R$: {(13.9 * len(listOfTypeTx[2])) * 0.1:.2f} >
    '''

    print(string)