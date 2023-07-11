from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import numpy as np


def recomendar(pelicula):
    # Obtén el título de la película de entrada del usuario
    nombre_pelicula = pelicula

    # Encuentra la película de entrada en el conjunto de datos
    pelicula_seleccionada = df[df['title'] == nombre_pelicula]

    # Verifica si la película de entrada existe en el conjunto de datos
    if len(pelicula_seleccionada) == 0:
        print("La película no se encuentra en el conjunto de datos.")
    else:
        # Obtén las características relevantes de las películas
        features = ['title', 'overview', 'genres', 'cast', 'crew']

        # Crea un nuevo DataFrame solo con las características relevantes
        df_selected = df[features]

        # Elimina las filas con valores faltantes
        df_selected = df_selected.dropna()

        # Combina las columnas 'cast' y 'crew' en una nueva columna llamada 'cast_crew'
        df_selected['cast_crew'] = df_selected['cast'] + ' ' + df_selected['crew']

        # Crea una matriz TF-IDF para representar los textos de las películas y elenco/equipo
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(df_selected['overview'] + ' ' + df_selected['cast_crew'])

        # Definir el tamaño del lote y calcular el número de lotes
    batch_size = 5000  # Tamaño del lote para el cálculo de similitud
    num_movies = len(df_selected)
    num_batches = (num_movies // batch_size) + 1

    cosine_similarities = None

    # Iterar a través de los lotes de películas
    for batch_index in range(num_batches):
        start_index = batch_index * batch_size
        end_index = min(start_index + batch_size, num_movies)

        # Obtener el subconjunto de películas para el lote actual
        movies_subset = range(start_index, end_index)

        # Crear una matriz TF-IDF solo con las películas del lote actual
        tfidf_matrix_subset = tfidf_matrix[movies_subset]

        # Calcular la similitud coseno entre las películas del lote actual
        batch_cosine_similarities = linear_kernel(tfidf_matrix_subset, tfidf_matrix_subset)

    if cosine_similarities is None:
        cosine_similarities = batch_cosine_similarities
    else:
        # Ajustar la dimensión del último lote si es necesario
        if batch_cosine_similarities.shape[0] < batch_size:
            batch_cosine_similarities = np.pad(batch_cosine_similarities, ((0, batch_size - batch_cosine_similarities.shape[0]), (0, 0)), mode='constant')
        elif batch_cosine_similarities.shape[0] > batch_size:
            batch_cosine_similarities = batch_cosine_similarities[:batch_size]

        # Ajustar la dimensión de cosine_similarities si es necesario
        if cosine_similarities.shape[1] < batch_cosine_similarities.shape[1]:
            cosine_similarities = np.pad(cosine_similarities, ((0, 0), (0, batch_cosine_similarities.shape[1] - cosine_similarities.shape[1])), mode='constant')
        elif cosine_similarities.shape[1] > batch_cosine_similarities.shape[1]:
            batch_cosine_similarities = np.pad(batch_cosine_similarities, ((0, 0), (0, cosine_similarities.shape[1] - batch_cosine_similarities.shape[1])), mode='constant')

        # Combinar los resultados del lote actual con los resultados anteriores
        cosine_similarities = np.concatenate((cosine_similarities, batch_cosine_similarities), axis=0)


    # Obtén el índice de la película seleccionada
    idx = df_selected[df_selected['title'] == nombre_pelicula].index[0]

    # Obtén las puntuaciones de similitud de la película seleccionada con todas las demás películas
    similarity_scores = list(enumerate(cosine_similarities[idx]))

    # Ordena las películas según su similitud
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Muestra las 5 películas más similares
    similar_movies = similarity_scores[1:6]  # Excluye la película de entrada
    respuesta = []
    for movie in similar_movies:
        similar_movie_title = df_selected.iloc[movie[0]]['title']
        respuesta.append(similar_movie_title)

    return {'Lista recomendada': respuesta}