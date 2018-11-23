# take data from customers.txt and display details in the sorted order of name
import re

f = open("customers.txt","rt")
customers = []
for line in f:
    regexp = r"([A-Za-z. ]+)( +)(\d{10})( +)(\w+@\w+)"
    match = re.match(regexp,line)
    if not match is None:
         customers.append( match.groups())   # add tuple returned by groups() method  to list


for cust in  sorted(customers):  # Sorts tuples by first element 
    print(f"{cust[0]:20s}  {cust[2]:10s}  {cust[4]}")


input file - customers.txt
==========================
Mr. James 3939349333   james@yahoo.com
Andy Hills   3838348383    andy@gmail.com
Scott   38383833 scott@gmail.com
Stephens   3939393911  stephens@microsoft.com
Mr. Richards 3838838388 richards@microsoft.com
Larry larry@google.com


Output of the program
=====================
Andy Hills            3838348383  andy@gmail
Mr. James             3939349333  james@yahoo
Mr. Richards          3838838388  richards@microsoft
Stephens              3939393911  stephens@microsoft

