import facebook
#graph = facebook.GraphAPI(access_token="EAACEdEose0cBAOm1ptBJ5LR7gDOeZB5Oj2bOG0PQSmXJKS8WmR3SFyvucFCDUkdqDZCzaNUZBZBRD0wFVTzZABCu27QzCwBuRqIBdjdhUHT1ZBgsYqwjzXx1E1WG4u8XvZBYPioGCVIPgUhrJYu0ZAIcDV61NMqFGduUrPttwncsd5vappVxloNEAnSwLdbHd1oZD", version="2.11")
graph = facebook.GraphAPI("EAACEdEose0cBAOm1ptBJ5LR7gDOeZB5Oj2bOG0PQSmXJKS8WmR3SFyvucFCDUkdqDZCzaNUZBZBRD0wFVTzZABCu27QzCwBuRqIBdjdhUHT1ZBgsYqwjzXx1E1WG4u8XvZBYPioGCVIPgUhrJYu0ZAIcDV61NMqFGduUrPttwncsd5vappVxloNEAnSwLdbHd1oZD")
friends = graph.get_object("me/email")
print friends
