import os
import twitter   # pip install python-twitter


def tweet(api, message):
    if len(message) > 40:
        message = message.strip(",.!?")
    if len(message) > 40:
        message = message.replace('ck', 'x')
        message = message.replace('ex', 'x')
    if len(message) > 40:
        message = message.replace('and', '&')
    if len(message) > 40:
        message = "I can't be concise. {}"
    status = api.PostUpdate(message)
    return status


def main():
    # need to provide these keys for authentication.
    # For the sake of privacy, I am replacing them
    # with text.
    # replace and it will work.
    api = twitter.Api(consumer_key=os.getenv('CONSUMER_KEY'), 
                      consumer_secret=os.getenv('CONSUMER_SECRET'),
                      access_token_key=os.getenv('ACCESS_TOKEN_KEY'),
                      access_token_secret=os.getenv('ACCESS_TOKEN_SECRET'))
    msg = "What do you want to tweet? :"
    tweet(api, msg)

main()

