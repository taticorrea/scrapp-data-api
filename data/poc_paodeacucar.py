from modules.scrapper import getWithBs4, getNextUrl
from modules.paodeacucar import getItensAndPrices

url_base = 'https://www.paodeacucar.com/categoria/'
args = 'qt=12&p='

categories = [
    'alimentos', 'beleza-e-perfumaria', 'bebidas','bebidas-alcoolicas','limpeza','bebes-e-criancas','cuidados-pessoais',
    'suplementos-alimentares','eventos-e-festas','utensilios-e-descartaveis','petshop','floricultura-e-jardim',
    'esportes-e-lazer','cuidados-com-a-saude','moveis-e-decoracao','cama-mesa-e-banho','papelaria',
    'brinquedos-e-jogos','automotivos','casa-e-construcao','celulares-e-smartphones','eletrodomesticos',
    'eletroportateis','games-e-videogames','informatica','moda','telefonia-fixa','tv-audio-e-video'
]
url = getNextUrl(url_base,categories[0],args,str(1))
print(url)
# print(getWithBs4(url))
print(getItensAndPrices(getWithBs4(url)))

# print(getItensAndPrices(getWithBs4(url)))

# for category in categories:
#     print("Category: ", category)
#     try:
#         for page in range(1,5):
#             next_url = getNextUrl(url_base, category, args, str(page))
#             print("Sending a GET request to a: ", next_url)
            # getItensAndPrices(getWithBs4(next_url)).to_csv(f"itens_precos_{category}_paodeacucar.csv", header = False, index = False, mode='a')
    # except:
    #     pass
