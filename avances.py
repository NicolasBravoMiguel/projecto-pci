

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

# Nueva función para verificar las calorías hasta que estén dentro del rango
def verificar_calorias():
    calorias = obtener_calorias()
    while calorias < 1500 or calorias > 4000:
        print("Las calorías ingresadas están fuera del rango saludable (1500-4000). Inténtalo de nuevo.")
        calorias = obtener_calorias()
    return calorias

# Ciclo principal para seguir ejecutando el programa
def ejecutar_programa():
    while True:
        sexo = obtener_sexo()
        calorias = verificar_calorias()  # Asegura que las calorías estén en el rango
        peso = float(input("Ingresa tu peso (kg): "))
        altura = float(input("Ingresa tu altura (m): "))
        imc = calcular_imc(peso, altura)
        
        print(obtener_mensaje(calorias, imc))
        
        continuar = input("¿Deseas realizar otra consulta? (Sí/No) ").lower()
        if continuar != "sí":
            print("Gracias por usar el programa.")
            break

# Llamada para iniciar el programa
ejecutar_programa()
