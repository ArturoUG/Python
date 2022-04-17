def mayusMinus(s):
    result = ""
    for letra in s:
        if letra == letra.upper():
            result += letra.lower()
        else:
            result += letra.upper()

    print(result)

mayusMinus("hOLA")

