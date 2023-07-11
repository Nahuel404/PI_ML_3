from fastapi import FastAPI
from starlette import responses
import pandas as pd


df_completo = pd.read_html('https://drive.google.com/file/d/1jzqQznmdmHMZaHsc-Fv9SmTdsn8MAwLy/view?usp=drive_link')
df_credits = pd.read_html('https://drive.google.com/file/d/1-4fVvqGqfwZDffMQYEcHC9kv68meN8RC/view?usp=drive_link')

app = FastAPI()

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

@app.get('/productoras_exitosas/{productora}')
def productoras_exitosas(productora:str):
    df_companias = df_completo[df_completo['companies']==productora]
    df_companias = df_companias.drop_duplicates(subset=['id'])

    total = int(df_companias['revenue'].sum())
    cantidad = int(df_companias['companies'].value_counts())

    return {'productora': productora,
            'revenue_total': total,
            'cantidad': cantidad}

@app.get('/get_director/{nombre_director}')
def get_director(nombre_director:str):
    df_director = df_credits[df_credits['job'] == "Director"]
    df_director = df_director.drop_duplicates(subset = ['id'])
    df_director = df_director[['id', 'job', 'name_y']]
    df_director = pd.merge(df_completo, df_director, on='id', how='inner')
    df_director = df_director.drop_duplicates(subset=['id'])
    df_director = df_director[df_director['name_y']==nombre_director]
    df_director['release_date']=pd.to_datetime(df_director['release_date'])


    total = df_director['return'].sum()
    peliculas = list(df_director['title'])
    fecha = list(df_director['release_date'].dt.year)
    retorno_pelicula = list(df_director['return'])
    budget_pelicula = list(df_director['budget'])
    revenue_pelicula = list(df_director['revenue'])

    return {'director': nombre_director,
            'retorno_total_director': total,
            'peliculas': peliculas,
            'anio': fecha,
            'retorno_pelicula': retorno_pelicula,
            'budget_pelicula': budget_pelicula,
            'revenue_pelicula': revenue_pelicula}

@app.get('/recomendacion/{pelicula}')
def recomendacion(pelicula):
    from modelo_de_recomendacion import recomendar
    respuesta = recomendar(pelicula)

    return respuesta

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)