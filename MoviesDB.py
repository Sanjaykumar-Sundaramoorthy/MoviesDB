from flask import Flask , render_template , request 
import requests

app = Flask(__name__)

def getSearchResults(query):
       r = requests.get(f'http://www.omdbapi.com/?apikey=f14d87bd&s={query}') 
       return r.json()["Search"]

@app.route("/",methods=['GET','POST'])
def home():
    if request.method == 'POST':
        query = request.form['movie']
        films = getSearchResults(query)
        return render_template('home.html' , movies = films , movie = query)
    return render_template('home.html')

def getdetails(movieid):
       r = requests.get(f'http://www.omdbapi.com/?apikey=f14d87bd&plot=full&i={movieid}') 
       return r.json()

@app.route("/details/<string:imdbID>",methods=['GET','POST'])
def moviedetails(imdbID):
    movie = getdetails(imdbID)
    return render_template('details.html',movie = movie,imdbID = imdbID)

if __name__ == '__main__':
    app.debug = True
    app.run()



