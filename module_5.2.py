import datetime
print(datetime.datetime.now())

from datetime import datetime,date,time
ekhon=datetime.now()
print(ekhon.year)
print(ekhon.date())
print(ekhon.time())

# set (year, month,date)
from datetime import date
blabla=date(year=2007,month=7,day=2)
print(blabla)

# date,month,year set
print(ekhon.strftime("%B %d,%Y"))


#timedelta method
from datetime import datetime,timedelta
ekhon=datetime.now()
dob=datetime(2004,5,25,0,0,0)
diff=ekhon-dob
print(diff)

#ekhon theke 5 din porer time dekhbo 
from datetime import datetime
ekhon=datetime.now()
print(ekhon +timedelta(days=5,minutes=15))



#Building JSON Module
import json
from datetime import datetime
student={ 
    "name":"Borna Rani",
    "Result":[2.5,3.6,5,4.5],
    "vorti_hoiche": datetime.now().strftime("%B %d,%Y")

}
#python theke json e convert korte 
j_student=json.dumps(student)
print(type(j_student))

#json theke python e convart korte 
p_student=json.loads(j_student)
print(type(p_student))

# Request API(jsonplaceholder)
import requests
res=requests.get('https://jsonplaceholder.typicode.com/posts')
final=res.text

import json
xyz=json.loads(final)
print(xyz[0])

ress=requests.get("https://jsonplaceholder.typicode.com/posts/1")
abc=ress.json()
print(abc['body'])