import facebook
#graph = facebook.GraphAPI(access_token="your_token", version="2.11")
graph = facebook.GraphAPI(access_token)
friends = graph.get_object("me/friends")
print friends
