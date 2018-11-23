from gettweets import Twitter
from markov import Post_tweet


class Initialisation:
    def __init__(self, tweet_name, count):

        consumer_key, consumer_secret, access_key, access_secret = self.get_keys()
        # получаем корпус
        self.tweet = Twitter(
            tweet_name,
            consumer_key,
            consumer_secret,
            access_key,
            access_secret
        )
        # генерируем и постим твиты
        self.post = Post_tweet(
            consumer_key,
            consumer_secret,
            access_key,
            access_secret,
            count
        )

    # получаем ключи
    def get_keys(self):
        f = open('files/keys.txt', 'r',  encoding='utf8', errors='ignore')
        tokens = f.readline().split(";")
        return str(tokens[0]), str(tokens[1]), str(tokens[2]), str(tokens[3])


if __name__ == '__main__':
    tweet_name = "SU_HSE"
    #print("Введите имя твиттера донора")
    #tweet_name = input()
    print("Введите количество твитов")
    count = input()
    init = Initialisation(tweet_name, count)
    print(init.post.posting)
