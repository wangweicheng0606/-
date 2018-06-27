# 问题：1元钱买一瓶水，三个空瓶可以换一瓶水，初始n元最终可以喝到多少瓶水？

def bottle(n):
	if n<3:
		return n
	else:
		s = n//3
		return 3*s + bottle(n-2*s)

print([bottle(x) for x in [10,15,18]])
