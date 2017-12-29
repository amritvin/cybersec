import requests
import openpyxl
wb = openpyxl.load_workbook('efb.xlsx')
sheet = wb.get_sheet_by_name('---myfacebook---')
r = requests.get('http://localhost/FeedBack/addFeedback.php')
print r.status_code
lis=[]
for i in range (2,6):
        for j in range(1,5):
            temp=sheet.cell(row=i, column=j).value
            lis.append(temp)
        payload = {'fullname':lis[0],'email':lis[2],'teamname':lis[1],'descr':lis[3]}
        url = 'http://localhost/FeedBack/register.php'
        p=requests.post(url, data=payload)
        print p.text
        lis=[]
