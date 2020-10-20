import pandas as pd
from sklearn import linear_model
import csv  
with open('mydata.csv') as csv_file:
  a = [{k: float(v) for k, v in row.items()}
    for row in csv.DictReader( csv_file, skipinitialspace=True)]
df = pd.DataFrame(a,columns=['distance_to_citycenter','distance_to_airport','distance_to_station','year_built','num_room','num_bed','num_bath','living_area','askprice']) 
X = df[['distance_to_citycenter','distance_to_airport','distance_to_station','year_built','num_room','num_bed','num_bath','living_area']].astype(float) 
Y = df['askprice'].astype(float)
regr = linear_model.LinearRegression()
regr.fit(X, Y)
Ketqua= regr.intercept_
dauVao=[]
dauVao.append(input("Khoang cach den trung tam thanh pho : "))
dauVao.append(input("Khoang cach den san bay : "))
dauVao.append(input("Khoang cach den tau dien ngam : "))
dauVao.append(input("Nam xay dung : "))
dauVao.append(input("So phong : "))
dauVao.append(input("So phong ngu : "))
dauVao.append(input("So phong tam : "))
dauVao.append(input("Dien tich : "))
for i in range(8) :
	Ketqua=Ketqua+regr.coef_[i]*float(dauVao[i])
print("Gia tien du doan",Ketqua)
print("Do chinh xac : ",regr.score(X, Y)*100)






