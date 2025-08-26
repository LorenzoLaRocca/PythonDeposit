def passbreakcontinue():

    names = ["Joyce", "Hannah", "Manny", "troy", "Manoy", "Ezekiel", "Lorenzo"]

    for name in names:
        if 'j' in name.lower():
            pass
        elif 'z' in name.lower():
            break
        elif 't' in name.lower():
            continue
        else:
            print(name)

passbreakcontinue()