import markovify
import tweepy
import re

class Post_tweet:
    def __init__(self,
                 consumer_key,
                 consumer_secret,
                 access_key,
                 access_secret,
                 count
                 ):

        self.posting = self.post(
            consumer_key,
            consumer_secret,
            access_key,
            access_secret,
            count
        )

    def post(self,
             consumer_key,
             consumer_secret,
             access_key,
             access_secret,
             count
             ):
        # пробуем запостить, иначе сообщаем об ошибке
        try:

            with open("files/corpus.txt", encoding='utf8', errors='ignore') as f:
                text = f.read()
            text = re.sub("[^\s]*…", '', text)
            text = re.sub("[,—)*/(:]{1}", '', text.lower())
            
            text_model = markovify.Text(text, state_size=2)

            for i in range(int(count)):
                print("{0} - процентов".format((i+1) / int(count) * 100 ))
                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                auth.set_access_token(access_key, access_secret)
                api = tweepy.API(auth)

                api.update_status(text_model.make_short_sentence(280))
            return "Done"
        except:

            return "Wrong"




