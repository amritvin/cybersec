import facebook
import json
import openpyxl
wb = openpyxl.Workbook()
wb.get_sheet_names()
sheet = wb.get_active_sheet()
token = 'EAACEdEose0cBAIZBrDXhwm9vuHbiHpGAZC8LhLK0Q4NiP6xf5knQ0zcw4twRPN8oXGwaac54m6ZCKPk0RkgBwIPh5ANbXqnNOkQzHZBc51YdB45rITwP7qzT7rUMw3JemjwY4AFS8m2IAqKyGc1uWgZBQGtZBjG5ZCA7utr6LGrOdqsZCUZArh8YUGORdQB1LaBWlTu2PtZBfRbgZDZD'
graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
sheet.title = '---myfacebook---'
print "----------------------MY FACE-BOOK-------------------"
friends = graph.get_connections("me", "friends")
friend_list = [friend['name'] for friend in friends['data']]
print "list :",friend_list
print profile
fb = graph.request("me?fields=id,name,birthday,friends{birthday,name}")
fb1=graph.request("me/friends?fields=id,name,birthday")
# while graph.request("me/friends") works well
print fb1
c=2
sheet['A1'] = 'friendlist'
sheet['B1'] = 'birthday'
for e in fb1["data"]:
    if 'birthday' in e:
        x='A'+str(c)
        y='B'+str(c)
        sheet[x]=e['name']
        sheet[y]=e['birthday']
        c=c+1
    #else:
    #    print e['name'],e['birthday']
wb.save('efb.xlsx')
