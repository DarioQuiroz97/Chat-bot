# Función para imprimir un mensaje cuando la selección no es válida.
def print_message():
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

# Función para obtener el tamaño de la bebida.
def get_size():
    res = input('What size drink can I get for you?\n[a] Small\n[b] Medium\n[c] Large\n> ')
    
    if res == 'a':
        return 'small'
    elif res == 'b':
        return 'medium'
    elif res == 'c':
        return 'large'
    else:
        print_message()
        return get_size()

# Función para obtener el tipo de bebida.
def get_drink_type():
    res = input('What type of drink would you like?\n[a] Brewed Coffee\n[b] Mocha\n[c] Latte\n> ')
    
    if res == 'a':
        return 'brewed coffee'
    elif res == 'b':
        return 'mocha'
    elif res == 'c':
        return order_latte()
    else:
        print_message()
        return get_drink_type()

# Función para realizar el pedido de un latte.
def order_latte():
    res = input('And what kind of milk for your latte?\n[a] 2% milk\n[b] Non-fat milk\n[c] Soy milk\n> ')
    
    if res == 'a':
        return 'latte'
    elif res == 'b':
        return 'non-fat latte'
    elif res == 'c':
        return 'soy latte'
    else:
        print_message()
        return order_latte()

# Función principal del bot coffee_bot.
def coffee_bot():
    print("Welcome to the cafe!")

    # Obtener tamaño y tipo de bebida.
    size = get_size()
    drink_type = get_drink_type()

    # Obtener nombre del usuario.
    name = input("Can I get your name please?\n> ")

    # Resultado final.
    print(f"Alright, that's a {size} {drink_type}!")
    print(f"Thanks, {name}! Your drink will be ready shortly.\nOrder complete!")

# Llamar a la función coffee_bot.
coffee_bot()

# Cerrar el programa.
input("Press Enter to exit")
