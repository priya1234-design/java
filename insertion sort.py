import time
import matplotlib.pyplot as plt
def insertionsort(array):
    n=len(array)
    for i in range(0,n):
        item=array[i]
        j=j-1
        while j>=0 and item<array[j]:
            array[j+1]=array[j]
            j=j-1
            array[j+1]=item
    return array
array=[]
start=time.time()
n=int(input("how many elements you want in your array"))
for i in range(n):
    array.append(int(input(f" enter %d number" %i)))
print(f" before swapping:{array}")
arrray=insertionsort(array)
print(f" after swapping:{array}")
end=time.time()
print("run time is",end-start)
x=list(range(1,10000))
plt.plot(x,[y*y for y in x])
plt.title("insertionsort-time complexity is O(n\u00b2)")
plt.xlabel("input")
plt.ylabel("time")
plt.show()
