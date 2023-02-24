from flask import Flask, render_template, request, redirect, url_for 
 
app = Flask(__name__) 
 
class Movie(): 
    def __init__(self, id, title, seen): 
        self.id = id 
        self.title = title 
        self.seen = seen 
 
movies = [ 
    Movie(1, "Coco", True), 
    Movie(2, "Titanic", True), 
    Movie(3, "Врятувати рядового Раяна", False) 
] 
 
@app.route("/") 
def index(): 
    return render_template("index.html", movies=movies) 
 
@app.route("/add", methods=["POST"]) 
def add(): 
    title = request.form.get("title") 
    max_id = 0 
    for movie in movies: 
        if movie.id > max_id: 
            max_id = movie.id 
    movie = Movie(max_id + 1, title, False) 
    movies.append(movie) 
    for movie in movies: 
        print(movie.id) 
    return redirect(url_for("index")) 
 
@app.route("/update/<int:id>") 
def update(id: int): 
    for movie in movies: 
        if movie.id == id: 
            movie.seen = not movie.seen 
            break 
    return redirect(url_for("index")) 
 
@app.route("/delete/<int:id>") 
def delete(id: int): 
    for index, movie in enumerate(movies): 
        if movie.id == id: 
            del movies[index] 
            break 
    return redirect("/") 
 
app.run(debug=True)