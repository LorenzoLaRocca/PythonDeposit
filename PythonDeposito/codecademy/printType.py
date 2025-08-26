def tryPrintType():
    int_value = 4
    print(int_value)
    print(type(int_value))

    print(    )

    float_value = float(int_value)
    print(float_value)
    print(type(float_value))

    temperature = int(101.2)
    print(type(temperature))
    
    temperature = float(101.2)
    print(type(temperature))
    
    temperature = bool(101.2)
    print(type(temperature))
    
    temperature = str(101.2)
    print(type(temperature))

tryPrintType()