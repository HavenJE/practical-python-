
current_movies = {
    "Matrix": "11:00pm",
    "The Accountant": "8:00am",
    "Secario": "11:00pm"
}

print("We are showing the current movies:")
for key in current_movies:
    print(key)

movie = input("What movie would you like the showtime for?\n")

# we want to pick that movie and show its show time 
showtime = current_movies.get(movie)

if showtime == None:
    print("The requested showtime is not playing!")
else: 
    print(movie, "is playing at:", showtime)
