import numpy
model_vals = []
target = [1,2,3,4,5,6,7,8,9,10]
totals = []
def model(t,w,b):
    return (w*t) + b

# p = prediction from model and t = target from data
def cost (p , t):
    return (p - t) ** 2
    
    
w = 0.95
b = 1

for i in range (len(target)):
    model_index = model(target[i],w,b)
    model_vals.append(model_index)

for j in range (10):
    value = cost(model_vals[j], target[j])
    totals.append(value)

print (sum(totals))
print ("target values: ", target)
print ("predicted values: ",model_vals)
print ('cost values: ', totals)
