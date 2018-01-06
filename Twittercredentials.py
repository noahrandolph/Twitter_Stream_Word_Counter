import tweepy

#consumer_key = "YourConsumerkey";
consumer_key = "rsrc3pWTrCelRnRjpqfmR15Mr";

#consumer_secret = "YourConsumerSecret";
consumer_secret = "TsZ5lSlYRAqQowYGMYIZZj0feEwGatTDNMmt6LTK9IdXarhYeV";

#access_token = "YourAcessToken";
access_token = "248482599-OIrbHg6Y065vqzol5qkmrK4AA0ibyUnRB66XMkYS";

#access_token_secret = "YourTokenSecret";
access_token_secret = "NzioO3Y2Y4h0ZvAetzlBD9JbqcCeXiLgG3PTyoYp8jxPb";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
