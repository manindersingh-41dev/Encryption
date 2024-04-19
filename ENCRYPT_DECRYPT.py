

def encrypt(a,c):	
	str=''
	b=("ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]")
	if c>=81:
		print("keycode must be less than or equal to 81")
	for i in a:
		for j in b:
			if i==j:
				ind=b.index(j)
				# print("ind ",ind)
				# val1=b[ind]
				val2=b[ind+c]
				# val1,val2=val2,val1
				str1 = str.join(val2)
				# print(str)
				j=val2
				print(j,end="")
				break
	# print(str)
	


def decrypt(a,c):
	b=("ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]ABC+D@EF=G!HI%JKL_MN|OP<Q$RS>TU/V{W^XY} Z[a&b1c*d(e2)fg\h3i`j~k4l-m?n5o'pq6rs7:t;uv8w,xy9z0]")
	for i in a:
		for j in b:
			if i==j:
				ind=b.index(j)
				val1=b[ind]
				val2=b[ind-c]
				val1,val2=val2,val1
				j=val1
				print(j,end="")
				break

				
ask='null'
while ask!='!':
	ask=input("Do you want to encrypt or decrypt (E/D)  :  ")
	a=input("Enter :")
	print()
	c=int(input("Enter key : "))
	print()
	
	print()
	print()

	if ask.lower()=="e":
		encrypt(a,c)
	if ask.lower()=="d":
		decrypt(a,c)

	
	print()
	print()
	print("***********************************************")
	print()
	print("    			IK WAARI HOR...")
	print()

