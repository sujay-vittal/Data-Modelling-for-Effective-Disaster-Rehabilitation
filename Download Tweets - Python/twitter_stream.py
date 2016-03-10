#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
consumer_key = 'doPnpOSCxZemudH6B0KdhUMR5'
consumer_secret = 'iocE6O66lLi822wRdylohD7LJMc12vjhR8jJnZkkgAGoLdWp5z'
access_token = '1201081159-ByvD4c1lIdAUdZ7b7XjWZFZdfnAlNb764lbFgBU' #Sujay's twitter account
access_token_secret = 'XUk6FLVqv6TOmYkQtNRtATP8oG1CWl0rVoM0CjqxCWm8E'


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'Chennai', 'Rains', 'Floods'
    stream.filter(track=['Chennai', 'Rains', 'Floods'])