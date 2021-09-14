# acronyms = {
#     'LOL': 'laugh out loud',
#     'IDK': "I don't know",
#     'TBH': 'to be honest'}

# # this is a dictionary, not an object

# print(acronyms['LOL'])

current_movies = {
    'The Grinch':'11:00am',
    'Rudolph':'1:00pm',
    'Frosty the Snowman': '3:00pm',
    'Christmas Vacation': '5:00pm'}

print('\nWe currently have the following movies:\n')

for key, time in current_movies.items():
    print(key, 'is playing at', time, "today.")

movie = input("\nWhich movie would you like to see? ")
showtime = current_movies.get(movie)

if showtime:
    print(movie, "has a showtime at", showtime, end = '\n\n')
else:
    print(movie, "is not an option. Try again.")