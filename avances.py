# Listas de dietas para hombres y mujeres
dietas_hombre = {
    "1500_kcal": [
        {"desayuno": {"nombre": "Avena con manzana", "calorías": 350}},
        {"almuerzo": {"nombre": "Pollo asado con ensalada", "calorías": 500}},
        {"cena": {"nombre": "Sopa de verduras", "calorías": 400}},
        {"snacks": {"nombre": "Frutas variadas", "calorías": 250}}
    ],
    "2000_kcal": [
        {"desayuno": {"nombre": "Omelette de claras", "calorías": 400}},
        {"almuerzo": {"nombre": "Salmón con quinoa", "calorías": 600}},
        {"cena": {"nombre": "Pechuga de pavo y verduras", "calorías": 500}},
        {"snacks": {"nombre": "Yogur y nueces", "calorías": 500}}
    ],
    "2500_kcal": [
        {"desayuno": {"nombre": "Tostadas con aguacate", "calorías": 450}},
        {"almuerzo": {"nombre": "Carne magra con arroz", "calorías": 650}},
        {"cena": {"nombre": "Pasta integral con atún", "calorías": 600}},
        {"snacks": {"nombre": "Batido de proteínas", "calorías": 600}}
    ],
    "3000_kcal": [
        {"desayuno": {"nombre": "Avena con nueces", "calorías": 500}},
        {"almuerzo": {"nombre": "Pollo a la plancha con papas", "calorías": 700}},
        {"cena": {"nombre": "Filete de res con verduras", "calorías": 700}},
        {"snacks": {"nombre": "Frutas con yogurt y miel", "calorías": 600}}
    ],
    "3600_kcal": [
        {"desayuno": {"nombre": "Huevos revueltos con jamón", "calorías": 600}},
        {"almuerzo": {"nombre": "Pechuga de pollo y batatas", "calorías": 800}},
        {"cena": {"nombre": "Salmón con pasta", "calorías": 800}},
        {"snacks": {"nombre": "Barras de granola y frutos secos", "calorías": 600}}
    ]
}


dietas_mujeres = {
    "1500-1800": ["Desayuno: Avena con almendras", "Almuerzo: Ensalada de quinoa", "Cena: Pescado con brócoli"],
    "1801-2000": ["Desayuno: Batido verde", "Almuerzo: Wrap de pollo", "Cena: Tacos de pescado"],
    "2001-2200": ["Desayuno: Pan integral con aguacate", "Almuerzo: Salmón con arroz integral", "Cena: Ensalada con tofu"],
    "2201-2500": ["Desayuno: Yogurt con frutas", "Almuerzo: Sándwich de pavo", "Cena: Filete de pescado con ensalada"],
    "2501-2800": ["Desayuno: Smoothie de bayas", "Almuerzo: Pasta integral con pollo", "Cena: Ensalada griega"],
    "2801-3100": ["Desayuno: Tostadas con hummus", "Almuerzo: Pollo al curry con arroz", "Cena: Pavo al horno con papas"],
    "3101-3300": ["Desayuno: Huevos revueltos con espinacas", "Almuerzo: Hamburguesa vegana", "Cena: Pollo al limón con quinoa"],
    "3301-3600": ["Desayuno: Pan de plátano", "Almuerzo: Ensalada César con salmón", "Cena: Pizza casera vegetariana"],
    "3601-4000": ["Desayuno: Gofres de avena", "Almuerzo: Enchiladas de pollo", "Cena: Paella de mariscos"]
}

# Función para solicitar el sexo
def obtener_sexo():
    return input("¿Cuál es tu sexo? (Hombre/Mujer): ").lower()

# Función para solicitar las calorías necesarias
def obtener_calorias():
    return int(input("¿Cuántas calorías necesitas? "))

# Nueva función para verificar las calorías hasta que estén dentro del rango
def verificar_calorias():
    calorias = obtener_calorias()
    while calorias < 1500 or calorias > 4000:
        print("Las calorías ingresadas están fuera del rango saludable (1500-4000). Inténtalo de nuevo.")
        calorias = obtener_calorias()
    return calorias

# Función para obtener un plan basado en el sexo y las calorías
def obtener_plan_por_sexo(sexo, calorias):
    if 1500 <= calorias <= 1800:
        rango = "1500-1800"
    elif 1801 <= calorias <= 2000:
        rango = "1801-2000"
    elif 2001 <= calorias <= 2200:
        rango = "2001-2200"
    elif 2201 <= calorias <= 2500:
        rango = "2201-2500"
    elif 2501 <= calorias <= 2800:
        rango = "2501-2800"
    elif 2801 <= calorias <= 3100:
        rango = "2801-3100"
    elif 3101 <= calorias <= 3300:
        rango = "3101-3300"
    elif 3301 <= calorias <= 3600:
        rango = "3301-3600"
    elif 3601 <= calorias <= 4000:
        rango = "3601-4000"
    else:
        return []

    if sexo == "hombre":
        return dietas_hombres[rango]
    elif sexo == "mujer":
        return dietas_mujeres[rango]
    else:
        return []

# Función para calcular el IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Función para obtener el mensaje final con la dieta
def obtener_mensaje(calorias, imc, sexo):
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

        # Añadir la recomendación basada en el sexo y las calorías
        plan_dieta = obtener_plan_por_sexo(sexo, calorias)
        if plan_dieta:
            mensaje += "\nAquí tienes tu plan de comidas:\n" + "\n".join(plan_dieta)
        else:
            mensaje += "No se encontró un plan adecuado para las calorías ingresadas."
        return mensaje

# Ciclo principal para seguir ejecutando el programa
def ejecutar_programa():
    while True:
        sexo = obtener_sexo()
        calorias = verificar_calorias()  # Asegura que las calorías estén en el rango
        peso = float(input("Ingresa tu peso (kg): "))
        altura = float(input("Ingresa tu altura (m): "))
        imc = calcular_imc(peso, altura)
        
        print(obtener_mensaje(calorias, imc, sexo))
        
        continuar = input("¿Deseas realizar otra consulta? (Sí/No) ").lower()
        if continuar != "sí":
            print("Gracias por usar el programa.")
            break

# Llamada para iniciar el programa
ejecutar_programa()
