# projecto-pci
Repositorio para el projecto de pci Idea general: Cantabilizador de calorias

El projecto consiste en poder contabilizar las colarias el el usuario quiere comer. Al usuario entrar el munero de calorias el cual quiere ingerir en un dia el programa arrojara un plan de comida. Este plan podra ser cambiado a la preferencia del usuario.

Algoitmo
Entradas
Numero de calorias
Sexo
Alergias

Proceso
1- Definir variables:
   - sexo: Texto
   - calorias: Entero
   - tieneAlergia: Booleano
   - mensaje: Texto

2- Preguntar "¿Cuál es tu sexo?" y almacenar en la variable `sexo`

3- Pedir "¿Cuántas calorías necesitas?" y almacenar en la variable `calorias`

4- Preguntar "¿Tienes alguna alergia?" (Sí/No) y almacenar la respuesta en la variable `tieneAlergia`

5- Si `calorias` < 1500, entonces:
   - mensaje = "Se requiere poder comer un mínimo de 1500 calorías para mantener una dieta saludable."
   - Imprimir mensaje

6- Si `calorias` > 4000, entonces:
   - mensaje = "Por encima de las 4000 calorías ya no se considera una comida saludable. Ingrese los datos nuevamente."
   - Imprimir mensaje

7- Si `calorias` entre 1500 y 1800, entonces:
   - mensaje = "Plan 1: Opción A, Plan 2: Opción B, Plan 3: Opción C"
   - Imprimir mensaje

8- Si `calorias` entre 1801 y 2000, entonces:
   - mensaje = "Plan 1: Opción D, Plan 2: Opción E, Plan 3: Opción F"
   - Imprimir mensaje

9- Si `calorias` entre 2001 y 2200, entonces:
   - mensaje = "Plan 1: Opción G, Plan 2: Opción H, Plan 3: Opción I"
   - Imprimir mensaje

10- Si `calorias` entre 2201 y 2500, entonces:
    - mensaje = "Plan 1: Opción J, Plan 2: Opción K, Plan 3: Opción L"
    - Imprimir mensaje

11- Si `calorias` entre 2501 y 2800, entonces:
    - mensaje = "Plan 1: Opción M, Plan 2: Opción N, Plan 3: Opción O"
    - Imprimir mensaje

12- Si `calorias` entre 2801 y 3100, entonces:
    - mensaje = "Plan 1: Opción P, Plan 2: Opción Q, Plan 3: Opción R"
    - Imprimir mensaje

13- Si `calorias` entre 3101 y 3300, entonces:
    - mensaje = "Plan 1: Opción S, Plan 2: Opción T, Plan 3: Opción U"
    - Imprimir mensaje

14- Si `calorias` entre 3301 y 3600, entonces:
    - mensaje = "Plan 1: Opción V, Plan 2: Opción W, Plan 3: Opción X"
    - Imprimir mensaje

15- Si `calorias` entre 3601 y 4000, entonces:
    - mensaje = "Plan 1: Opción Y, Plan 2: Opción Z, Plan 3: Opción AA"
    - Imprimir mensaje

Salida
- Plan de altimentacion para el dia


Codigo:

# Función para solicitar el sexo
def obtener_sexo():
    return input("¿Cuál es tu sexo? ")

# Función para solicitar las calorías necesarias
def obtener_calorias():
    return int(input("¿Cuántas calorías necesitas? "))

# Función para determinar si la persona tiene alguna alergia
def tiene_alergia():
    respuesta_alergia = input("¿Tienes alguna alergia? (Sí/No) ").lower()
    return respuesta_alergia == "sí"

# Función para calcular el IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Función para determinar el mensaje basado en las calorías y el IMC
def obtener_mensaje(calorias, imc):
    if calorias < 1500:
        return "Se requiere poder comer un mínimo de 1500 calorías para mantener una dieta saludable."
    elif calorias > 4000:
        return "Por encima de las 4000 calorías ya no se considera una comida saludable. Ingrese los datos nuevamente."
    else:
        if imc < 18.5:
            mensaje = "Tienes un IMC bajo. Aumenta tu ingesta de calorías con cuidado. "
        elif 18.5 <= imc <= 24.9:
            mensaje = "Tienes un IMC normal. Mantén tu ingesta de calorías actual. "
        elif 25 <= imc <= 29.9:
            mensaje = "Tienes un IMC de sobrepeso. Reduce ligeramente tu ingesta de calorías. "
        else:
            mensaje = "Tienes un IMC de obesidad. Considera reducir tu ingesta de calorías y consulta a un profesional."

        # Añadir la recomendación basada en la ingesta calórica
        mensaje += obtener_plan(calorias)
        return mensaje

# Función para obtener un plan basado en las calorías
def obtener_plan(calorias):
    if 1500 <= calorias <= 1800:
        return "Plan 1: Opción A, Plan 2: Opción B, Plan 3: Opción C"
    elif 1801 <= calorias <= 2000:
        return "Plan 1: Opción D, Plan 2: Opción E, Plan 3: Opción F"
    elif 2001 <= calorias <= 2200:
        return "Plan 1: Opción G, Plan 2: Opción H, Plan 3: Opción I"
    elif 2201 <= calorias <= 2500:
        return "Plan 1: Opción J, Plan 2: Opción K, Plan 3: Opción L"
    elif 2501 <= calorias <= 2800:
        return "Plan 1: Opción M, Plan 2: Opción N, Plan 3: Opción O"
    elif 2801 <= calorias <= 3100:
        return "Plan 1: Opción P, Plan 2: Opción Q, Plan 3: Opción R"
    elif 3101 <= calorias <= 3300:
        return "Plan 1: Opción S, Plan 2: Opción T, Plan 3: Opción U"
    elif 3301 <= calorias <= 3600:
        return "Plan 1: Opción V, Plan 2: Opción W, Plan 3: Opción X"
    elif 3601 <= calorias <= 4000:
        return "Plan 1: Opción Y, Plan 2: Opción Z, Plan 3: Opción AA"
    else:
        return ""

# Función para sumar o restar calorías
def ajustar_calorias(calorias, ajuste):
    return calorias + ajuste

# Función principal para ejecutar el programa
def main():
    sexo = obtener_sexo()
    calorias = obtener_calorias()
    alergia = tiene_alergia()
    peso = float(input("¿Cuál es tu peso en kilogramos? "))
    altura = float(input("¿Cuál es tu altura en metros? "))
    imc = calcular_imc(peso, altura)

    print("Calorías actuales:", calorias)
    ajuste = int(input("¿Cuántas calorías deseas ajustar? (Usa números negativos para restar): "))
    calorias = ajustar_calorias(calorias, ajuste)

    mensaje = obtener_mensaje(calorias, imc)
    print(mensaje)

# Ejecutar el programa
main()
