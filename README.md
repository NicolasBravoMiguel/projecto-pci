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
