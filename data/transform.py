from pandas import read_csv

sources = {
    "prezunic" : [
        "carnes-e-aves",
        "bebida-alcoolica",
        "bebida-nao-alcoolica",
        "congelados",
        "frios-e-laticinios",
        "higiene-e-beleza",
        "hortifruti",
        "limpeza",
        "mercearia",
    ]
}


def transform(sources: dict) -> list:
    for source, categories in sources.items():
        for category in categories:
            df = read_csv(f"data/{source}_data/{category}/{category}.csv", sep=';',header=None,names=["id","item",'preco',"fonte"],index_col=0)
            df.drop_duplicates(inplace=True)
            df.dropna(inplace=True)
            df.reset_index(drop=True,inplace=True)
            df.reset_index(drop=False,inplace=True)
            df.rename(inplace=True, columns={"index":"id"})
            df.to_json(f"data/{source}_data/{category}/{category}.json", orient='records', lines=False)

transform(sources)
