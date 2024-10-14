import tweepy

# 4tpZlO6kZij7kCW53zwUL0GxZ
# 7BeX9Rd9v86vXsp5h1Dz9ee2RL6YDQ1h6tN9nVAK4gZtLBb6nd

# AAAAAAAAAAAAAAAAAAAAAP%2FswAEAAAAAbRVW1guukgcCCcho0rPUJGVS8MY%3DATAG36j3s8OuibKzmNV4gL5JZ52BUTlopthPALdr6EFNASMeYO token beaerer
auth = tweepy.OAuthHandler('4tpZlO6kZij7kCW53zwUL0GxZ',
                           '7BeX9Rd9v86vXsp5h1Dz9ee2RL6YDQ1h6tN9nVAK4gZtLBb6nd')
auth.set_access_token('843231377264926720-DeYPA4LHyBnpIjRuAe2abJLPyJt2ouq',
                      'ZCU7GK56N3OxdRa5KS4Tyf597gKqYKl2R9RCmTER5S8Fm')

api = tweepy.API(auth)
user = api.me()

print(user)
