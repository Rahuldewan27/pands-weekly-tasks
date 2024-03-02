# lamdafunction.py
# more messing with functions
# author : rahul parvesh dewan

'''
x = lambda x : x**2

answer = x(4)
print(answer)

'''

'''
#businesstype = "standard"
businesstype = "reduced"

vatcalc = lambda amount : amount * .23

if businesstype == "reduced":
    vatcalc = lambda amount : amount * .135

cash = 10
print(vatcalc(cash))
'''

'''
#sort a list
numbers = [2,35,55,1,4]
sortednumbers = sorted(numbers)

print(f" {numbers} sorted are {sortednumbers}")
'''

# sort a dictionary

data = [{"name":"john", "YOB":1992},
        {"name":"paul", "YOB":1994}, 
        {"name":"george", "YOB":1995}]

sorteddata = sorted(data, key = lambda x : x["YOB"])
for item in sorteddata:
    print(item)
