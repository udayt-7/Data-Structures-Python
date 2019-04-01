import queue1

buy=queue1.flexiqueue()
total=0
def buy1(x,y):
	buy.enqueue([x,y])

def sell(x,y):
	if not buy.isempty():
		sum=0
		l=buy.dequeue()
		if l[0]<x:
			while(x!=0):
				x=x-l[0]
				if x>=0:
					sum=sum+l[0]*(y-l[1])
					l=buy.dequeue()
				else:
					x=l[0]+x
					sum=sum+x*(y-l[1])
					l[0]=l[0]-x
					buy.enqueue(l)
					x=0

				

		else:
			sum=sum+x*(y-l[1])
			l[0]=l[0]-x
			if l[0]!=0:
				buy.enqueue([l[0],l[1]])

		length=buy.length()

		for i in range(length-1):
			buy.enqueue(buy.dequeue())	
		buy.display()

		return sum





while True:
	print("1.buy,2.sell,3.exit")
	ch=int(input(("enter choice")))
	if ch==1:
		x=int(input("enter number of share(s)"))
		y=int(input("enter price for share(s)"))
		buy1(x,y)
	elif ch==2:
		x=int(input("enter number of share(s)"))
		y=int(input("enter price for share(s)"))
		total=total+sell(x,y)
		print("gain/loss of whole transaction is:",total)
	else:
		break




