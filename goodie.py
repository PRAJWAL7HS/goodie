import sys;
# Let's say the HR team of a company has goodies set of size N each with a different price tag for each goodie.
# Now the HR team has to distribute the goodies among the M employees in the company such that one employee receives one goodie.
# Goodies the HR team can distribute so that the difference between the low price goodie and the high price goodie selected is minimum.
# m is number of Employees.
# Returns minimum difference between maximum and minimum values of distribution.
def findMinDiff(goddie_prices, n, m):
 
    # If there are no  number of Employees then it is is 0
    if (m==0 or n==0):
        return 0
    # Sort the given prices
    arr=list(goddie_prices.values())
    arr.sort()
    # Number of Employees cannot be more than number of Goodies
    if (n < m):
        return -1
    # Largest number of Price
    min_diff = sys.maxsize
 
    '''Find the subarray of size m such that difference between last (maximum in case of sorted) and 
    first (minimum in case of sorted) elements of subarray is minimum.'''
    i=0
    while(i+m-1<n ):
        diff = arr[i+m-1] - arr[i]
        if (diff < min_diff):
            min_diff = diff
            low=i
            high=i+m-1
        i+=1
    b=[]
    godd={}
    b.append(arr[low:high+1])
    key_list = list(goddie_prices.keys())
    val_list = list(goddie_prices.values())
    # Finding the difference between the low price goodie and the high price goodie selected which is minimum with its key pair
    for ind in b:
        for i in ind:
            key=key_list[val_list.index(i)]
            godd[key]=i
    # Retrives the Goodies and prices which having the minimum difference.
    print(godd)
    return min_diff
# Driver Code
if __name__ == "__main__":
    goodie=['fitbit plus','ipods','mi bands','cult pass','mac book pro','digital camera','alexa','sandwich','microwave oven','Scale']
    prices=[7980,22349,999,2799,229900,11101,9999,2195,9800,4999]
    m = int(input("Number of Employees : "))
    n = len(prices)
    goodie_prices=dict(zip(goodie,prices))
    d=findMinDiff(goodie_prices, n, m)
    print("Minimum difference is",d)
