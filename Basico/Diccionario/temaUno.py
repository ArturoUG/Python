def run():
    diccionario ={
        "llave1" : 1,
        "llave2" : 2,
        "llave3" : 3
    }

    print(diccionario["llave1"])
    print(diccionario["llave2"])
    print(diccionario["llave3"])

    población_paises = {
	'Argentina': 44_938_712,
	'Brasil': 210_147_125,
	'Colombia': 50_372_424
    }

    for k,v in población_paises.items():
        print(f"{k} -> {v}")


if __name__ == '__main__':
    run()