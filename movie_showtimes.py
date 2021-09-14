current_movies = {
    "The Grinch":'11:00am',
    'Rudolph':'1:00pm',
    "Frosty the Snowman": '3:00pm',
    'Christmas Vacation': '5:00pm'}

print('\nWe currently have the following movies:\n')

for key in current_movies:
    print(key)

movie = input("\nWhich movie would you like to see? ")
showtime = current_movies.get(movie)

if showtime:
    print(movie, "has a showtime at", showtime, end = '\n\n')
else:
    print(movie, "is not an option. Try again.")