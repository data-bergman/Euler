import psycopg2
import pandas
import numpy
import math
import pandas.io.sql as sqlio


conn = psycopg2.connect("dbname=hackathon user=postgres password=erwan10507")


student = pandas.read_sql_query('SELECT * FROM storm_student',conn)
baseuser = pandas.read_sql_query('SELECT * FROM storm_baseuser',conn)
business = pandas.read_sql_query('SELECT * FROM storm_business',conn)
review = pandas.read_sql_query('SELECT * FROM storm_review',conn)
stint = pandas.read_sql_query('SELECT * FROM storm_stint',conn)
studentavailability = pandas.read_sql_query('SELECT * FROM storm_studentavailability',conn)
university = pandas.read_sql_query('SELECT * FROM storm_university',conn)

a=[student,studentavailability,stint,baseuser,business,review,university]
b=["student","studentavailability","stint","baseuser","business","review","university"]
#print([["student"+ str(t),student.columns[t]","type(t) ]for t in student.iloc[0]])
#print("studentavailability",studentavailability.columns,[type(t) for t in studentavailability.iloc[0]])
#print(business)

#print(student.iloc[0],[type(t) for t in student.iloc[0]])


for p in range(len(a)):
    print(b[p],[[a[p].columns[t],type(a[p].iloc[0][t])]for t in range (len(a[p].columns))])
c=["Runner","Cleaning","Customer Service","Waiting","Bar Back","Door Person","Waiter/Waitress","Kitchen Porter","Other","Leafleting","Cashier","Errands","Cloakroom"]
print(numpy.mean(review.grade))
print(review.grade)