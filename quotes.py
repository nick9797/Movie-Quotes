#This program takes a number and prints a movie and or its quote based on the number the user inputs.

import random
from random import randint

def loadDatabase():
	global movie_quotes
	infile=open("movie_quotes.txt", 'r')
	infile_string=infile.readline()
	movie_quotes=dict()
	for line in infile:
		line=line.lstrip(" ")
		line=line.rstrip('\n')
		line=line.split("--")
		movie_quotes[line[0]]=line[1]

def printMovies():
	for title in movie_quotes.keys():
		print(title)
	

def printQuotes():
	for quote in movie_quotes.values():
		print(quote)

def printAll():
	for title in movie_quotes.keys():
		print(title, movie_quotes[title])

def printTheQuote():
	answer=input("Enter movie title (Also add 1 space before movie input): ")
	if answer in movie_quotes.keys():
		print(movie_quotes[answer])
	else:
		print("That movie is not in the application.")

def AddQuote():
	global movie_quotes
	movie=input("Enter new movie: ")
	quote=input("Enter new quote: ")
	movie_quotes[movie]=quote

def displayRandomQuote():
	global movie_quotes
	radical=random.randint(0,len(movie_quotes))
	i=list(movie_quotes.values())
	print(i[radical])

def removeMovie():
	global movie_quotes
	gone=input("What movie do you want to remove?: ")
	del movie_quotes[gone]

def quit():
	print("Shutting down")

def main():
	loadDatabase()
	i=1
	while i==1:
		print("Welcome to the best movie quotes app!")
		print("1: Print all the movies in the app.")
		print("2: Print all the quotes in the app.")
		print("3: Print both all the movies and the quotes in the app.")
		print("4: Print a quote on the movie you pick.")
		print("5: Add a movie and its quote to the app.")
		print("6: Print a random movie quote.")
		print("7: Remove a quote from the app.")
		print("8: Quit the app.")
		that=eval(input("Pick a number on the screen depending on what you want to do: "))
		if that==1:
			printMovies()
		elif that==2:
			printQuotes()
		elif that==3:
			printAll()
		elif that==4:
			printTheQuote()
		elif that==5:
			AddQuote()
		elif that==6:
			displayRandomQuote()
		elif that==7:
			removeMovie()
		elif that==8:
			quit()
			i=0
		else:
			print("You did not print a number on the screen.")
main()

