]# Mad_dev + init3
# Twitter deletion(killme) was taken from a user in an irc chat room, I cant remember his handle.    
#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
import tweepy
import sys
import time 
import codecs


CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
    


# Conky

if sys.argv[1]:
    command = sys.argv[1]
    
    # API Limit
    if command == "limit":
        lim = api.rate_limit_status()
	print lim
        re = lim['remaining_hits']
        print "Requests Left: ", re
    
    # Mentions of you    
    elif command == "mentions":
        time.sleep(30) # This is needed so you dont finish up all your permited requests
        # time.sleep(seconds)
        mentions = api.mentions()
        for mention in mentions:
            print mention.text
    # Timeline
    elif  command == "timeline":
        user_tweets = api.user_timeline("screen_name")
        # Put your screen name where it says "screen_name"
        # NOTE: you can put any user
        for tweet in user_tweets:
            print tweet.text, "\n"
                
    # Followers
    elif command == "followers":
        folo_name = [u.screen_name for u in api.followers("screen_name")] 
        # Put your screen name where it says "screen_name"
        # NOTE: you can put any user
        for folo in folo_name:
            print folo

   #Home timeline---> By init3
    elif command == "htimeline":
                pub_tweets = api.home_timeline()
                for ptweet in pub_tweets[:10]:
                        print ptweet.user.screen_name,":",ptweet.text.encode('utf8'), "\n"


        
# EOF Conky

# Command line client

    elif command == "tweet":
        print "usage: \n tm--->(timeline) \n @--->(mentions) \n ptime--->(public Timeline) \n Ufolo--->(followers) \n t--->(tweet) \n killme--->(AVOID AT ALL COST) \n trend"
        print "use 'kill' to exit"
        while 1:
            x=raw_input(">>: ")
            if  x=="tm":
                g = raw_input("Name of User: ")
                user_tweets = api.user_timeline(g)
                for tweet in user_tweets:
                    print tweet.text, '\n'
            
                        
            elif x=="@": 
                mentions = api.mentions()
                for mention in mentions:
                    print mention.text 
        
            elif x=="ptime":
                public_tweets = api.home_timeline()
                for ptweet in public_tweets:
                    print ptweet.text, '\n'      
                    
            elif x=="Ufolo":
                f = raw_input("ID: ")
                folo_name = [u.screen_name for u in api.followers(f)]
                for tfolo in folo_name:
                    print tfolo
                    
            elif x=="trend":
                t = api.trends_location(1)
                tr = "\n".join(i["name"] for i in t[0]["trends"])
                print tr
            
            elif x == "killme":
                print "This will empty your tweets"
                pas = raw_input("Password: ")
                if pas == "1":
                    user_timeline_threshold = 0
                    retweeted_by_me_threshold = 0
                    favorites_threshold = 0
                    direct_messages_threshold = 0
                    sent_direct_messages_threshold = 0

                    print "authenticated user:", api.me().screen_name

                    print "deleting statuses, keeping", user_timeline_threshold
                    user_timeline = tweepy.Cursor(api.user_timeline).items()
                    for status in itertools.islice(user_timeline, user_timeline_threshold, None):
                        api.destroy_status(status.id)
                        print "deleted:", status.id

                    print "deleting retweets, keeping", retweeted_by_me_threshold
                    retweeted_by_me = tweepy.Cursor(api.retweeted_by_me).items()
                    for status in itertools.islice(retweeted_by_me, retweeted_by_me_threshold, None):
                        api.destroy_status(status.id)
                        print "deleted:", status.id

                    print "deleting favorites, keeping", favorites_threshold
                    favorites = tweepy.Cursor(api.favorites).items()
                    for status in itertools.islice(favorites, favorites_threshold, None):
                        api.destroy_favorite(status.id)
                        print "deleted:", status.id

                    print "deleting direct messages, keeping", direct_messages_threshold
                    direct_messages = tweepy.Cursor(api.direct_messages).items()
                    for direct_message in itertools.islice(direct_messages, direct_messages_threshold, None):
                        api.destroy_direct_message(direct_message.id)
                        print "deleted:", direct_message.id

                    print "deleting sent direct messages, keeping", sent_direct_messages_threshold
                    sent_direct_messages = tweepy.Cursor(api.sent_direct_messages).items()
                    for direct_message in itertools.islice(sent_direct_messages, sent_direct_messages_threshold, None):
                        api.destroy_direct_message(direct_message.id)
                        print "deleted:", direct_message.id
                
                else: 
                    print "wrong...."
                    break
    
            elif x=="t":
                y = raw_input("Tweet: ")
                tweet = api.update_status(y)        
                print "your tweet was sent"
                    
                
                
            elif x=="kill":
                print "goodbye..."
                break
            else:
                print "usage: \n tm--->(timeline) \n @--->(mentions) \n ptime--->(public Timeline) \n Ufolo--->(followers) \n t--->(tweet) \n killme--->(AVOID AT ALL COST) \n trend"
                print "use 'kill' to exit"
    
    else:
        print "...!#"
