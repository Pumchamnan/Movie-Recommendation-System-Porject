import streamlit as st
import pickle
import requests
import streamlit.components.v1 as components


def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
     data=requests.get(url)
     data=data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
     return full_path


movie = pickle.load(open('movie_list.pkl','rb'))
simmilarity = pickle.load(open('simmilarity.pkl','rb'))
movie_list = movie['title'].values

st.header("Movie Recommender System")

selectvalue = st.selectbox("Select Movie from dropdown", movie_list)


####
def recommander(movies):
  index = movie[movie['title'] == movies].index[0]
  distance = sorted(list(enumerate(simmilarity[index])), reverse=True, key=lambda vector:vector[1])
  recommend_movie = []
  recommend_poster = []
  for i in distance[1:6]:
   movie_id = movie.iloc[i[0]].id
   # print(movie.iloc[i[0]].title)
   recommend_movie.append(movie.iloc[i[0]].title)
   recommend_poster.append(fetch_poster(movie_id))
  return recommend_movie, recommend_poster


if st.button("show recommend"):
  movie_name , movie_poster= recommander(selectvalue)
  col1, col2, col3, col4, col5 = st.columns(5)
  with col1:
    st.text(movie_name[0])
    st.image(movie_poster[0])
  with col2:
    st.text(movie_name[1])
    st.image(movie_poster[1])
  with col3:
    st.text(movie_name[2])
    st.image(movie_poster[2])
  with col4:
    st.text(movie_name[3])
    st.image(movie_poster[3])
  with col5:
    st.text(movie_name[4])
    st.image(movie_poster[4])