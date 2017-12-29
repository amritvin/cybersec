import facebook
import json

token = 'EAACEdEose0cBAIZBrDXhwm9vuHbiHpGAZC8LhLK0Q4NiP6xf5knQ0zcw4twRPN8oXGwaac54m6ZCKPk0RkgBwIPh5ANbXqnNOkQzHZBc51YdB45rITwP7qzT7rUMw3JemjwY4AFS8m2IAqKyGc1uWgZBQGtZBjG5ZCA7utr6LGrOdqsZCUZArh8YUGORdQB1LaBWlTu2PtZBfRbgZDZD'

graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
print "----------------------MY FACE-BOOK-------------------"
friends = graph.get_connections("me", "friends")
friend_list = [friend['name'] for friend in friends['data']]
print "list :",friend_list
print profile
fb = graph.request("me?fields=id,name,birthday,friends{birthday,name}")
# while graph.request("me/friends") works well
"""
urls= 'https://graph.facebook.com/'+friendid
response = urllib2.urlopen(urls)
html = response.read()
print html
#"me?fields=id,name,birthday,address,friends{birthday,friendlists{name},name}"
"""
print fb['birthday']
