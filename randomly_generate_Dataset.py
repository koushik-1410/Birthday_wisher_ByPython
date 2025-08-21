import pandas as pd
import random

from faker import Faker

fake=Faker()

data=[]
for _ in range(20):
    name=fake.first_name()
    birthday=fake.date_of_birth(minimum_age=10,maximum_age=40)
    phone = "+91" + str(random.randint(6000000000, 9999999999))
    data.append([name,birthday,phone])

df=pd.DataFrame(data,columns=["Names","Birthday","Phone"])

print(df)

df.to_csv("birthday_dataset.csv",index=False)