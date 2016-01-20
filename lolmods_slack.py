import praw
import OAuth2Util
import warnings
from slacker import Slacker
slack = Slacker('your-slack-api-key')

warnings.filterwarnings("ignore")

r = praw.Reddit("LoLMods to Slack Crosspot Script")
r.login('user','password',disable_warning=True)
submission_stream = praw.helpers.submission_stream(r, 'mod-subreddit', limit=1, verbosity=1)
try:
	while True:
		submission = next(submission_stream)
		print(submission)
		slack.chat.post_message('#general','_'+str(submission.title)+'_ has been posted in /r/subreddit by ' + str(submission.author) + '.\n' 
			+ str(submission.permalink))
except:
	print("SHITS DOWN M8")


