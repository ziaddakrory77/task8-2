import pandas as pd 
student_data = [['Alice' , 20 , 'A' , 85],
                ['Bob' , 22, 'B', 78 ],
                ['Charlie' , 19 , 'A' , 92],
                ['David' , 21 , 'C' , 65],
                ['Eva' , 20 , 'B' , 74]]
df=pd.DataFrame(student_data, columns=['Name','Age' , 'Grade', 'Mark'])
print(df.head(3))

print(df[['Name', 'Mark']])

successful_students= df[df['Grade']== 'A']

print(successful_students)