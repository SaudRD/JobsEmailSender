import tweepy
import time
import random
import smtplib
import logging
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

logger = logging.getLogger()
mail_from = 'Put Your Email'
mail_to = 'Put Your Email'
mail_pw = 'PutUr Password here'

#Write your API keys down
def startUp():
    consumer_key = ''
    consumer_secret = ''
    key = ''
    secret = ''

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(key, secret)
    api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
    try:
        api.verify_credentials()
    except tweepy.TweepError as e:
        logger.error("Check credentials!!!", exc_info=True)
        raise e
    logger.info("Started")
    return api
def send_mail(text):
    msg = MIMEText(text)
    msg['From'] = mail_from
    msg['To'] = mail_to
    msg['Subject'] = 'وظيفة تقنية جديدة'

    smtp_server_name = 'smtp-mail.outlook.com'

    server = smtplib.SMTP('{}:{}'.format(smtp_server_name, 587))
    server.starttls()

    server.login(mail_from, mail_pw)
    server.send_message(msg)
    server.close()
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
            keywords = ['تقنية', 'Software', 'Cyber', 'Information', 'Data', 'نظم']
            # this function will return only tweets of particalar user
            if any(tweet in status.text.lower() for tweet in keywords) and status.user.id_str == 'user Id here':
                # send e-mail
                print("Sending Email now with : "+ status.text)
                send_mail(f"اي وظيفة غرد وظيفة تقنية جديدة : {status.text}  -   on  {time.ctime()}")

def main():
    api = startUp()
    elon_tweet_listener = tweepy.Stream(auth=api.auth, listener=MyStreamListener())
    elon_tweet_listener.filter(follow=['same Id user here'], is_async=True)



if __name__ == "__main__":
    print("-----------------------")
    print("---Waitting for Jobs---")
    print("-----------------------")

    main()
    