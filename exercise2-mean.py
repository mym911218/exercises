x = [ 1, 2, 3, 4, 5, 6]

def mean(x):
	sum= 0
	n=0 

	for i in range (0, 6):
		sum = sum + x[i]
		n=n+1

	average = sum*1.0 / n
	return average

xbar = mean (x)

print 'The mean of 1,2,3,4,5,6 is' , xbar
