class ExtratorURL: 
    def __init__(self,url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
    
    def sanitiza_url(self,url):
        return url.strip()
    
    def valida_url(self):
        if self.url == "":
            raise ValueError("A URL está vazia")
     
    def get_url_base(self):
        ind_interroga = self.url.find("?")
        url_base = self.url[:ind_interroga]   
        return url_base
    
    def get_url_params(self):
        ind_interroga = self.url.find("?")
        url_parametros = self.url[ind_interroga + 1:]
        return url_parametros
    
    def get_valor_param(self,param_busca):
        ind_param = self.get_url_params().find(param_busca)
        ind_valor = ind_param + len(param_busca) + 1
        ind_e_com = self.get_url_params().find("&",ind_valor)
        if ind_e_com == -1:
            valor = self.get_url_params()[ind_valor:]
        else:
            valor = self.get_url_params()[ind_valor:ind_e_com]
        return valor
        
        
                
extrator_url = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
valor_quant =  extrator_url.get_valor_param("quantidade")
print(valor_quant)