import math
# 1.1
# input: a list[a1,a2,...,an] of integers n>=2 integers with a single peak
# output: the index of the peak


# 1.2.a
# add -infinity at the end of the list
# set the index to 0
# run a while loop where the loop stops if the value in the list of given
# index is less than the next one
# add 1 to the index at every iteration
# if the peak is at the beginning, the program will not run the while loop and return 0
# if the peak is at the end, the program will run through the whole list before comparing
# the last integer to -infinity which will break the loop and return the index at that time
# if the peak is in the middle, the program will run through the list until the peak and return
# the peak




# 1.2.b

s1=list(range(100))
s2=s1[::-1]
s3=s1[:-1]+s2


def peak_index(s):
    s.append(-math.inf)
    i=0
    while s[i]<s[i+1]:
        i+=1
    return(i)
print(peak_index(s1),s1)
print(peak_index(s2),s2)
print(peak_index(s3),s3)

# 1.2.c
# the algorithm will use minimum 1 and maximum n-1 comparisons


# 1.3.a

# this algorithm first check if there is only a single element in the lisr, if so it
# returns its index
# this algorithm compares the value of this middle integer to the value of the integer
# immediately before it, if the first it bigger, it performs itself again on the list
# ending at the integer before the middle integer, if not, it returns the rest of the list



# 1.3.b

s1=[i for i in range(100)]
s2=s1[::-1]
s3=s1[:-1]+s2

def peak_rec(s):
    i=len(s)//2
    if i==0:
        return(i)
    elif s[i-1]>s[i]:
        return (peak_rec(s[:i]))
    else:
        return(i+peak_rec(s[i:]))
print(peak_rec(s1),s1)
print(peak_rec(s2),s2)
print(peak_rec(s3),s3)

# T(n)=T(n/2)+1
# T(n)=T(n/4)+1+1
# T(n)=T(n/(2^k))+k
# if n=2^k
# T(n)=T(1)+k=k+1
# n=2^k
# log(n)=k*log(2)
# log2(n)=k
# T(n)=log2(n)+1


# if T(n)=T(n/2)+m
# T(n)=mlog2(n)+m