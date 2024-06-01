import tkinter as tk
import pandas as pd



def find():

  # Read the CSV file into a DataFrame
  ratings = pd.read_csv('Netflix_Dataset_Rating.csv')
  movies=pd.read_csv('Netflix_Dataset_Movie.csv')

  # Assuming 'df' is your dataframe
  sample_size = 1000  # Set the desired sample size

  text = entry1.get()



  # Sample the dataset

  movie_ratings=pd.merge(movies,ratings)
  #movie_ratings = movie_ratings.sample(n=sample_size, random_state=42)


  movie_ratings = movie_ratings.pivot_table(index=['User_ID'], columns=['Name'], values='Rating')

  # Get the user input (assuming entry1 is an Entry widget)


  # Select the specified movie column
  similar_movie = movie_ratings[text]

  # Calculate correlation with other movies
  similar_movies = movie_ratings.corrwith(similar_movie)
  similar_movies = similar_movies.dropna()
  similar_movies = similar_movies.sort_values(ascending=False)  # Sort in descending order

  # Print the top 5 similar movies
  top_similar_movies = similar_movies.head(5)
  print(top_similar_movies)
  label2.config(text=similar_movies)




 

def search():
  movies = pd.read_csv('Netflix_Dataset_Movie.csv')
  text = entry1.get()
  print(text)
  #mark located string as red
  listofmovies = ""
  listofmovies = movies['Name'][movies['Name'].str.contains(text)]
  label2.config(text=listofmovies)
  print(listofmovies['Name'])
  label2.config(text=listofmovies)


window = tk.Tk()

window.title(" Movie Recommender System")
window.geometry("1200x1200")
window.configure(bg="blue")


# Label for the title
title_label = tk.Label(window, text=" Movie Recommender System", bg="blue", fg="white", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)


label1 = tk.Label(text="Search if the movie exist?" ,bg="blue", fg="white")
label1.pack()

entry1 = tk.Entry()
entry1.pack()
entry1.focus_set()

button = tk.Button(text="Search for movie!", command=search)
button.pack()

button = tk.Button(text="Find Simillar movies", command=find)
button.pack()

#text box in root window
label2 = tk.Label(text="Result here!",bg="blue", fg="white")
label2.pack()

tk.mainloop()