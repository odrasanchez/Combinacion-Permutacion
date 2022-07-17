# Combinaciones y permutaciones

_Calculadora de combinaciones ordinarias, permutaciones ordinarias con repetición y permutaciones ordinarias sin repetición. Basadas en fórmulas matemática que se revisan en el ámbito académico._

### Situación de repositorio
<img src="https://img.shields.io/badge/Coverage-100%25-dbc9f1?style=for-the-badge" /> <img src="https://img.shields.io/github/stars/0draS0/PY-CalcuCombinaciones?color=dbc9f1&style=for-the-badge" /> <img src="https://img.shields.io/badge/Version-1.0-dbc9f1?style=for-the-badge" />

### Tecnologías utilizadas 🔨
  - Spyder (Python 3.9)

### Notas importantes ⚠
  - Ambas calculadoras cuentan con lineas de restricción de datos, esto por solicitud de la fórmula matemática.
  - Ambos códigos se encuentran comentados.
  - No requiere de ninguna instalación extra, los programas cuentan con las librerías necesarias para ejecutarse sin problema.


## Calculadora con uso de cadena  (Calculadora 1)
El programa cuenta con un menú de selección, donde el usuario puede ingresar a partir del teclado con que operación desea trabajar:

```
Bienvenido, seleccione la operacion a trabajar: 
1. Combinacion ordinaria
2. Permutacion SIN REPETICION
3. Permutacion CON REPETICION
```

Caso 1:
  - La **combinación ordinaria***, se requiere el dato _n_ (el número de combinaciones de los elementos) y _m_ (grupos de estos elementos que se toman sin reemplazo).

Caso 2:
  - La permutación **ordinaria sin repetición** requiere el dato _n_ (el número de permutaciones de los elementos) y _m_ (grupos de estos elementos que se toman sin reemplazo).

Caso 3:
  -  La permutación **ordinaria con repetición** requiere el dato _r_ (el número de repeticiones de los elementos) y una _cadena_ (números, letras o caracteres SIN ESPACIOS NI USO DE ,). Un ejemplo es:

```
Bienvenido, seleccione la operacion a trabajar: 
1. Combinacion ordinaria
2. Permutacion SIN REPETICION
3. Permutacion CON REPETICION

3

Ingrese el valor de repeticion:2
Ingrese la cadena a usar, sin espacios ni coma:abc
Cantidad de permutaciones: 9
[('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'b'), ('b', 'c'), ('c', 'a'), ('c', 'b'), ('c', 'c')]
```

## Calculadora simple (Calculadora 2)
El programa cuenta con un menú de selección, donde el usuario puede ingresar a partir del teclado con que operación desea trabajar:

```
Bienvenido, seleccione la operacion a trabajar: 
1. Combinacion ordinaria
2. Permutacion SIN REPETICION
3. Permutacion CON REPETICION
```

Caso 1:
  - La **combinación ordinaria***, se requiere el dato _n_ (el número de combinaciones de los elementos) y _m_ (grupos de estos elementos que se toman sin reemplazo).

Caso 2:
  - La permutación **ordinaria sin repetición** requiere el dato _n_ (el número de permutaciones de los elementos) y _k_ (grupos de estos elementos que se toman sin reemplazo).

Caso 3:
  - Este caso, utiliza la fórmula ordinaria. La permutación **ordinaria con repetición** requiere el dato _n_ (el número de permutaciones de los elementos) y _r_ (grupos de estos elementos que se toman). Un ejemplo es:

```
Bienvenido, seleccione la operacion a trabajar: 
1. Combinacion ordinaria
2. Permutacion SIN REPETICION
3. Permutacion CON REPETICION

3

Ingrese el valor total de elementos:5
Ingrese el valor de elementos tomados:2
Ingrese el valor 0: 1
Ingrese el valor 1: 2

              5     5!
          PR  2 = ------ = 60.0
                     2!
```


## LICENCIA
Este proyecto fue una recopilación de información sobre uso de librerías en PY con fines académicos. Te agradecería mucho si:
  - Comentas sobre este proyecto 📢
  - Lo utilizas con fines educativos y aprendizaje 📖


### Bye 🖐
