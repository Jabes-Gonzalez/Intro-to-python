String = "My First String"
Number = 10  
List = ["red", "green", "blue", "yellow", "orange"]
Boolean = True
print("Some_text", String)
print("Age", Number)
print("Colors", List)
print("You are Young", Boolean)

print()

String = "My First String"
primeras_tres_letras = String[:4]
print(primeras_tres_letras)

print()

my_list = [10, 20, 30, 40, 50]
first_element = my_list[0]
print(first_element) 

print()

number_original = 20
new_number = number_original + 10
print(new_number)

print()

my_list_two = [10, 20, 30, 40, 50]
last_element = my_list_two[-1]
print(last_element)

print()

names = 'harry,alex,susie,jared,gail,conner'
name_list = names.split(',')
print(name_list)

print()

String = "string for python"
first_word = String.split()[0]
word_mayus = first_word.upper()
new_phrase = word_mayus + String[len(first_word):]
print(new_phrase)

print()

number = 10
phrase = f"My favorite number is {number}"
print(phrase)

print()

print('hello world')

print()

# Crear una cadena que contenga la palabra "Hola"
Bienvenida = "Hola, bienvenido a Python"
buscador = Bienvenida.find("Hola")
seleccion = Bienvenida[0:4]
print(f"{seleccion}")

# Reemplazar "Hola" con "adiós" usando el método replace()
nueva = Bienvenida.replace("Hola", "adiós")
print(f"{Bienvenida}")
print(f"{nueva}")

