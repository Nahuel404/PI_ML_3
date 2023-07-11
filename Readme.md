# Mlops (Sistema de recomendacion)

Machine Learning Operations (MLOps)

## Descripción

Este proyecto se enfoca en el tratamiento de un Dataset de películas y el despliegue de distintos endpoints, incluyendo un modelo de recomendación de películas.

## Características principales

- **FastAPI**: un framework de desarrollo web de alto rendimiento para construir los endpoints del proyecto ([enlace](https://fastapi.tiangolo.com)).
- **Render**: una plataforma de alojamiento y despliegue de aplicaciones web, para implementar y alojar el proyecto ([enlace](https://render.com)).
- **Datasets**: Se hace uso de los Datasets disponibles en el siguiente enlace: [Datasets](https://drive.google.com/drive/folders/1dBGCF1gq3cink9Kna7Iz3nn-JkLsxEeZ?usp=sharing) para el análisis y entrenamiento del modelo de recomendación de películas.
- **Diccionario de datos**: El diccionario de datos utilizado se encuentra disponible en el siguiente enlace: [Diccionario de datos](https://docs.google.com/spreadsheets/d/1QkHH5er-74Bpk122tJxy_0D49pJMIwKLurByOfmxzho/edit#gid=0) y proporciona información sobre las variables y su significado en el Dataset **movies_dataset**.

## Requisitos

- Tener Python 3.x instalado en tu sistema.
- Ejecutar el siguiente comando en la terminal para instalar las bibliotecas requeridas:

  ```bash
  pip install -r requirements.txt
  ```
<div style="display:flex; align-items:center;">
  <div style="width:50%; padding-right:20px;">
    <h2>Herramientas Utilizadas</h2>
    <ul style="text-align: justify;">
      <li><b>📊Scikit Learn</b>: Utilizado para vectorizar, tokenizar y calcular la similitud coseno.</li>
      <li><b>🐍Python</b>: Lenguaje de programación principal utilizado en el desarrollo del proyecto.</li>
      <li><b>💻Numpy</b>: Utilizado para realizar operaciones numéricas y manipulación de datos.</li>
      <li><b>🐼Pandas</b>: Utilizado para la manipulación y análisis de datos estructurados.</li>
      <li><b>📈Matplotlib</b>: Utilizado para la visualización de datos y generación de gráficos.</li>
      <li><b>📳FastAPI</b>: Utilizado para crear la interfaz de la aplicación y procesar los parámetros de funciones.</li>
      <li><b>🦄Uvicorn</b>: Servidor ASGI utilizado para ejecutar la aplicación FastAPI.</li>
      <li><b>🌐Render</b>: Plataforma utilizada para el despliegue del modelo y la aplicación.</li>
    </ul>
  </div>
</div>
Asegúrate de estar ubicado en el directorio del proyecto donde se encuentra el archivo requirements.txt.

Este comando instalará automáticamente todas las bibliotecas necesarias en tu entorno virtual.

Si aún no tienes Python instalado, puedes descargarlo e instalarlo desde el sitio oficial de Python: https://www.python.org.
## Introducción:

En este proyecto de Machine Learning, asumiré el rol de un Data Engineer y ML Operations y llevaré a cabo todos los procesos necesarios, desde el tratamiento y recolección de datos hasta el entrenamiento y despliegue del modelo de ML. El objetivo principal es desarrollar un sistema de recomendación de películas basado en técnicas de similitud y algoritmos de Machine Learning.

## Objetivos del proyecto:
---
1. **Generación de API´s que procesan funciones que responden a consultas acerca de características de películas**

2. **Deployment de un modelo de clasificación para un sistema de recomendación de películas**

---
## Resumen del proyecto:
---
### 1. Proceso de Extracción, Transformación, Carga ( _enlace:_ [ETL ](https://github.com/EmilianoEmanuelSosa/PI_ML_OPS_Individual_Project/blob/main/ETL.ipynb))

En el archivo **ETL.py**, se llevó a cabo el proceso de extracción de datos de dos fuentes, la transformación de los datos para su limpieza y preprocesamiento, y finalmente la carga de los datos en un formato adecuado (archivo **ds_clean.csv**) para su posterior análisis y entrenamiento del modelo. (tambien ver **data_dictionary.md**)


### 2. Implementación de API´s ( _enlace:_ [main.py ](https://github.com/EmilianoEmanuelSosa/PI_ML_OPS_Individual_Project/blob/main/main.py))

En el archivo **main.py**, se creará una interfaz utilizando la biblioteca **FastAPI y Uvicorn**. Esta interfaz permitirá a los usuarios interactuar con el modelo de Machine Learning, proporcionando los datos de entrada necesarios y obteniendo las predicciones correspondientes.


### 3. Análisis Exploratorio de Datos ( _enlace:_ [EDA ](https://github.com/EmilianoEmanuelSosa/PI_ML_OPS_Individual_Project/blob/main/EDA.ipynb))

En el notebook **EDA.ipynb**, se realizará un **`INFORME`** de Análisis exhaustivo de los datos y la factiblidad de modelos de clasificación para el caso en estudio. Esto incluirá la visualización de los datos, reducción de dimensionalidad, tratamiento de valores atípicos y la generación de conclusiones relevantes entorno a las variables y la elección del modelo.


### 4. Desarrollo del Modelo de Machine Learning ( _enlace:_ [model.py ](https://github.com/EmilianoEmanuelSosa/PI_ML_OPS_Individual_Project/blob/main/main.py))

En el archivo **model.py**, se implementará un modelo de Machine Learning utilizando **Similitud de cosenos**. Este modelo se entrenó utilizando los datos preprocesados y preparados durante el EDA (archivo **Data_movies_merged.csv**).Finalmente se realizó el deployemnt de la aplicación usando [RENDER ](https://pi-mlops-emiliano-sosa.onrender.com/docs).


URL: https://pi-mlops-emiliano-sosa.onrender.com/{nombre_director}
Método: GET
Parámetros:
nombre_director: El nombre del director que deseas obtener información.
Ejemplo de uso: https://pi-mlops-emiliano-sosa.onrender.com/get_director/Steven Spielberg
API: recomendacion
Esta API devuelve una lista de 5 películas similares al título especificado, en forma de recomendación.

URL: https://movies-repository.onrender.com/recomendacion/{titulo}
Método: GET

### API: `peliculas_idioma`

Esta API devuelve la cantidad de películas en el idioma especificado.

- **URL**: `https://pi-mlops-emiliano-sosa.onrender.com/peliculas_idioma/{idioma}`
- **Método**: GET
- **Parámetros**:
  - `idioma`: El idioma de la cantidad de películas que deseas obtener.
- **Ejemplo de uso**: `https://pi-mlops-emiliano-sosa.onrender.com/peliculas_idioma/en`

### API: `peliculas_duracion`

Esta API devuelve el nombre, su duración en minutos y el año de estreno de una película específica.

- **URL**: `https://pi-mlops-emiliano-sosa.onrender.com/peliculas_duracion/{pelicula}`
- **Método**: GET
- **Parámetros**:
  - `pelicula`: El nombre de la película para la cual deseas obtener la duración.
- **Ejemplo de uso**: `https://pi-mlops-emiliano-sosa.onrender.com/peliculas_duracion/Jumanji`

### API: `franquicia`

Esta API devuelve información sobre una franquicia de películas, su nombre, cantidad de películas, ganancias totales y ganancias promedio.

- **URL**: `https://pi-mlops-emiliano-sosa.onrender.com/franquicia/{franquicia}`
- **Método**: GET
- **Parámetros**:
  - `franquicia`: El nombre de la franquicia de películas que deseas obtener información. Todas estas franquicias terminan con **Collection**.
- **Ejemplo de uso**: `https://pi-mlops-emiliano-sosa.onrender.com/franquicia/Toy Story Collection`

### API: `peliculas_pais`

Esta API devuelve la cantidad de películas producidas en el pais especificado.

- **URL**: `https://pi-mlops-emiliano-sosa.onrender.com/peliculas_pais/{pais}`
- **Método**: GET
- **Parámetros**:
  - `pais`: El nombre del país para el cual deseas obtener la cantidad de películas producidas.
- **Ejemplo de uso**: `https://pi-mlops-emiliano-sosa.onrender.com/peliculas_pais/United States of America`

### API: `productoras_exitosas`

Esta API devuelve información sobre una productora, su nombre, ganancias totales y la cantidad de peliculas producidas.

- **URL**: `https://pi-mlops-emiliano-sosa.onrender.com/productoras_exitosas/{productora}`
- **Método**: GET
- **Parámetros**:
  - `productora`: El nombre de la productora de películas que deseas obtener información.
- **Ejemplo de uso**: `https://pi-mlops-emiliano-sosa.onrender.com/productoras_exitosas/Pixar Animation Studios`

### API: `get_director`

Esta API devuelve información sobre un director de películas, su nombre, el retorno total en sus peliculas y un diccionario con informacion de sus peliculas.

- **URL**: `[https://movies-repository.onrender.com](https://pi-mlops-emiliano-sosa.onrender.com)/get_director/{nombre_director}`
- **Método**: GET
- **Parámetros**:
  - `nombre_director`: El nombre del director que deseas obtener información.
- **Ejemplo de uso**: `https://pi-mlops-emiliano-sosa.onrender.com/get_director/Steven Spielberg`

### API: `recomendacion`

Esta API devuelve una lista de 5 películas similares al título especificado, en forma de recomendación.

- **URL**: `https://pi-mlops-emiliano-sosa.onrender.com/recomendacion/{titulo}`
- **Método**: GET
- **Parámetros**:
  - `titulo`: El título de la película para la cual deseas obtener recomendaciones.
- **Ejemplo de uso**: `https://pi-mlops-emiliano-sosa.onrender.com/Toy Story`

---


Parámetros:
titulo: El título de la película para la cual deseas obtener recomendaciones.
Ejemplo de uso: https://movies-repository.onrender.com/recomendacion/Toy Story
Copy code
