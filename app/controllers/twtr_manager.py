import sqlite3
import datetime
from app.controllers import db_manager
from app.controllers.db_manager import DatabaseManager

__author__ = 'Jen Mart'
import tweepy, time, sys, json
from tweepy import OAuthHandler



class twtrManager:
    def __init__(self):
        self.db_manager = DatabaseManager(self)
        self.main()

    def main(self):
        ckey = 'rlee33vXmHIlmR5tQljIX0ucD'
        csecret = 'cUiIFESIXSSin9YJHYwLnVwnHpS64Ytj7csY9yFqshvAlkcaPg'
        atoken = '2836017980-DxYDsgHqGMyRIq1yH3Uf3Ar63eYCFhqawJAWGOw'
        asecret = 'SruNXYjh0BpY4GQhiflXaxbB2XUhrCMslBrmrH2ViULnu'

        auth = tweepy.OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)
        api = tweepy.API(auth)
        auth = OAuthHandler(ckey, csecret)
    def homeTimeline(self):
        while True:
            ckey = 'rlee33vXmHIlmR5tQljIX0ucD'
            csecret = 'cUiIFESIXSSin9YJHYwLnVwnHpS64Ytj7csY9yFqshvAlkcaPg'
            atoken = '2836017980-DxYDsgHqGMyRIq1yH3Uf3Ar63eYCFhqawJAWGOw'
            asecret = 'SruNXYjh0BpY4GQhiflXaxbB2XUhrCMslBrmrH2ViULnu'
            auth = tweepy.OAuthHandler(ckey, csecret)
            auth.set_access_token(atoken, asecret)
            api = tweepy.API(auth)
            auth = OAuthHandler(ckey, csecret)
            timeline=api.home_timeline(COUNT=0)
            try:
                for tweet in timeline:
                    user=tweet.user
                    name=tweet.user.name.encode('utf-8')
                    text=tweet.text.encode('utf-8')
                    date=tweet.created_at

                    if "@DunSuciRun" in text: #checks if special text in field
                        text = text[11:]
                        check = self.db_manager.checkTweets(name, text, date)
                        if (check): #If not, add to DB
                            self.db_manager.storeTweets(name, text, date)
                            return text
                            break
                        else:
                            print "wait a minute"
                            time.sleep(60)
                            pass

                    else:
                        print "nothing valid. Waiting"
                        time.sleep(60)
                        pass
            except Exception, e:
                print "not valid. Lets wait a minute!"
                time.sleep(60)
                pass
        return text
         # return text

        # self.mainMenu(ckey,csecret,atoken,asecret,auth,api)

        # self.db_manager.storeTweets(name, text, date)

    def printTweet(self,text): #Works perfectly!
        ckey = 'rlee33vXmHIlmR5tQljIX0ucD'
        csecret = 'cUiIFESIXSSin9YJHYwLnVwnHpS64Ytj7csY9yFqshvAlkcaPg'
        atoken = '2836017980-DxYDsgHqGMyRIq1yH3Uf3Ar63eYCFhqawJAWGOw'
        asecret = 'SruNXYjh0BpY4GQhiflXaxbB2XUhrCMslBrmrH2ViULnu'
        auth = tweepy.OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)

        # conn = sqlite3.connect('DunSuciRun.sqlite')
        # t = conn.cursor()
        # t.execute("DELETE FROM PLAYERS") #MAKE SURE TO REMOVE THSI AFTER TESTING!! -jm
        # t.execute("""SELECT * FROM PLAYERS""")
        # usr = t.fetchall()
        # usr = usr[0][0]
        # conn.commit()
        # conn.close()


        # api.update_status("@" + usr + " " + text)
        print "demo!"
        # print ("@" + usr + " " + text)
        print text
        return






