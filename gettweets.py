
import tweepy
import codecs
import re


class Twitter:
    def __init__(self, tweet_name, consumer_key, consumer_secret, access_key, access_secret):
        self.get_all_tweets(
            tweet_name,
            consumer_key,
            consumer_secret,
            access_key,
            access_secret
        )
        return

    def get_all_tweets(self, screen_name, consumer_key, consumer_secret, access_key, access_secret):

        # авторизация
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)

        # лист для твитов
        alltweets = []

        # первые 200 твитов
        new_tweets = api.user_timeline(screen_name=screen_name, count=200)

        # кидаем твиты в список
        alltweets.extend(new_tweets)

        # получаем самый старый твит и отсекаем по нему по 200 шт и так можно спарсить только около 3000
        oldest = alltweets[-1].id - 1
        while len(new_tweets) > 0:

            new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)
            alltweets.extend(new_tweets)
            oldest = alltweets[-1].id - 1

        outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
        tweets = []
        # очистка от ссылок, упоминаний ников и хештегов
        for i in outtweets:
            textoftweet = re.sub("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
                                 '',
                                 str(i[2].decode('cp1251', 'ignore')))
            textoftweet = re.sub("@[A-Za-z0-9_]*", '', textoftweet)
            textoftweet = re.sub("#[A-Za-z0-9А-Яа-я_]*", '', textoftweet)

            tweets.append(textoftweet)
        f1 = codecs.open('files/corpus.txt', 'w', 'cp1251')
        for i in tweets:
            f1.write(i.encode('cp1251', errors='ignore').decode('cp1251', 'ignore'))





