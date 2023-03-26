from modules.scrapper import getWithBs4
from modules.prezunic import getItensAndPrices

def main():
    url = "https://www.prezunic.com.br/carnes-e-aves/carnes"
    getItensAndPrices(getWithBs4(url)).to_csv(f"itens_precos_prezunic.csv", index = False, mode='a')

main()