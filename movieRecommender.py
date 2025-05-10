#Create a program that asks the user for their top 3 favorite movies and their ratings. 
# Store the data in a dictionary, where the movie titles are the keys and the ratings are the values.
#Print the dictionary.
#Ask the user for a movie title and check if it exists in the dictionary. If it does, print the rating; if not, print "Movie not found!".
#Use a loop to print each movie title and its rating in the format "Movie: [Rating]".
#Calculate and print the average rating of all the movie

num_movies = 3
movies = {} #initializes an empty dictionary
total_rating = 0

#use a loop to ask for user input
for i in range(num_movies):
    movie_name = input(f"Enter the movie name {i+1}/{num_movies} ").lower()
    rating = float(input(f"enter the rating for the movie {movie_name} ")) #converts the input from string to float
    movies[movie_name] = rating
    total_rating += rating

print("These are the movies you entered and their ratings")
for movie, rating in movies.items():
    print(f"{movie}: {rating}")

search_movie = input("enter your movie choice: ").strip().lower()
if search_movie in movies:
    print(rating)
else:
    print("movie not found")

average_rating = total_rating / num_movies 
print(f"the average rating is {average_rating}")