from fastapi import FastApi
from starlette import responses
from typing import Optional
import pandas as pd

df_completo = pd.read_csv('../datasets/dataset_completo.csv')
df_credits = pd.read_csv('../datasets/dataset_credits.csv')

app = FastApi()

@app.get("/")
def home():
    from lib import leer_html
    
    html = leer_html('home.html')
    return responses.HTMLResponse(content=html, status_code=200)

@app.get('/peliculas_idioma/{idioma}')
def peliculas_idioma(idioma:str):
    mask = df_completo['full_language']==idioma
    
    df_filtrado = df_completo[mask]
    df_filtrado = df_filtrado.drop_duplicates(subset=['id'])

    respuesta = dict(df_filtrado['full_language'].value_counts())
    respuesta = respuesta[idioma]
    
    return {'idioma': idioma,
            'cantidad': respuesta}

@app.get('/peliculas_duracion/{pelicula}')
def peliculas_duracion(pelicula:str):
    df_completo['release_date']=pd.to_datetime(df_completo['release_date'])

    df_pelicula = df_completo[df_completo['title']==pelicula]
    df_pelicula = df_pelicula.drop_duplicates(subset=['id'])

    duracion = float(df_pelicula['runtime'])
    fecha = int(df_pelicula['release_date'].dt.year)

    return {'pelicula': pelicula,
            'duracion': duracion,
            'anio': fecha}

@app.get("/franquicia/{franquicia}")
def franquicia(franquicia:str):
    df_franquicia = df_completo[df_completo['name_franquicia']==franquicia]
    df_franquicia = df_franquicia.drop_duplicates(subset = ['title'])

    cantidad = int(df_franquicia['id_franquicia'].value_counts())
    total = df_franquicia['revenue'].sum()
    promedio = total/cantidad

    return {'franquicia': franquicia,
            'cantidad': cantidad,
            'ganancia_total': total,
            'ganancia_promedio': promedio}

@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais:str):
    df_pais = df_completo[df_completo['full_country']==pais]
    df_pais = df_pais.drop_duplicates(subset = ['id'])

    cantidad = int(df_pais['full_country'].value_counts())

    return {'pais': pais,
            'cantidad': cantidad}


