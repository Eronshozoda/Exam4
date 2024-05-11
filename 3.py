from datetime import datetime , timedelta
today=datetime.strptime(input(),"%d %m %Y") 
res=today-timedelta(days=5)
print(res)