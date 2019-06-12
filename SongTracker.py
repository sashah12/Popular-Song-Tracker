import tweepy
import praw
import billboard
from random import choices
import datetime
from keys import *
from prawfile import *


print('This is my sorting music Twitter Bot!')

#tweepy API authentication
#keys.py contains my personal information
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


#Reddit instance API
#prawfile contains my personal information

reddit = praw.Reddit(client_id = CLIENT_ID,
                     client_secret = CLIENT_SECRET,
                     password = PASSWORD,
                     user_agent = USER_AGENT,
                     username = USERNAME)



#takes the top most upvoted rap songs from r/hiphopheads/ from the day, randomizes them, and prints them. 

def post_link():
	song_titles = []
	links = []
	subreddit = reddit.subreddit('HipHopHeads')
	hot_sub = subreddit.hot(limit = 25)
	print('Reddit:')
	print(' ')
	for submission in hot_sub :
		if submission.title not in song_titles:
			if ' - ' in submission.title  and submission.ups > 200 :
				post_title = submission.title
				post_ups = submission.ups
				song_titles.append(post_title) 
				links.append(submission.url)
				print(post_title + ' : ' + submission.url)
			else:
				pass
		else:
			pass				 


#using billboard api, this function takes the top 100 songs, picks 3 randomized songs, and prints them.

def songChart():
	chart = billboard.ChartData('hot-100')
	counter = 0
	song_list = []
	tracks = chart[0: ]
	mixed_songs = choices(tracks, k = 3)
	print(' ')
	print('Billboard:')
	print(' ')
	for song in mixed_songs:
		if song.title not in song_list :
			print(song.title + ' by ' + song.artist)
			song_list.append(song.title)
				 

post_link()
songChart()

# when the time becomes 11:59, this function will run, where links for reddit and billboard will be posted to my twitter. 
#I have uploaded my files to pythonanywhere, a cloud platform which will keep this file running, and I don't have to keep 
#executing this file for it to post to my twitter.	

def tweetBot() :	
	x = datetime.datetime.now()
	if x.strftime("%H") == "23" and x.strftime("%M") == "59" : 
		api.update_status('Here are some of the top songs from Reddit from Today: ' + 'https://old.reddit.com/r/hiphopheads/') 
		api.update_status('Here are some of the top songs on the BillBoard 100 Chart from today: ' + 'https://www.billboard.com/charts/hot-100')
		u = 'Status Updated on Twitter'
		print(u)
	

tweetBot()


	
	
	





  	


