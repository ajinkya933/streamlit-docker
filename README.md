docker build -t streamlit_test3 .

docker container run -p 8501:8501 streamlit_test3

once done goto http://127.0.0.1:8501 to see your app running on localhost


References:
https://discuss.streamlit.io/t/how-to-use-streamlit-in-docker/1067/6

