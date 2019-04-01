
#Suppose you have a stack S containing n elements and a queue Q that is initially empty. 
#Write function that use Q to scan S to see if it contains a certain element x, 
#with the additional constraint that your algorithm must return the elements back to S in their 
#original order. You may use S, Q and a constant number of other variables.

import stack1 as s
import queue1 as q



def scan(key):
	c = 0 
	for ch in range(S.stacklength()):
		if (S.stackpeek() == key):
			while not Q.isqEmpty():
				c +=1
				S.stackpush(Q.qdequeue())
			while c != 0:
				Q.qenqueue(S.stackpop())
				c -= 1
			while not Q.isqEmpty():
				
				S.stackpush(Q.qdequeue())
			return True

		else:
			Q.qenqueue(S.stackpop())
		


if __name__ == '__main__':
	
	S = s.LimitedStack()
	Q = q.flexiqueue()
	S.stackpush(10)
	S.stackpush(9)
	S.stackpush(40)
	S.stackpush(60)
	S.stackpush(80)
	S.stackpush(20)
	S.stackpush(13)
	S.stackpush(14)
	S.stackpush(15)
	S.stackpush(16)

	key = int(input("enter element to be searched: "))

	print(scan(key))
	S.displaystack()