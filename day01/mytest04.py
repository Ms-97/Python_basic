a = input("첫수를 입력하세요")
b = input("끝수를 입력하세요")

aa = int(a)
bb = int(b)
#arr = range(aa,bb+1)

idx = 0
for i in range(aa,bb+1):
    idx+=i
print(a+"에서 "+b+"까지의 합",idx,"입니다.")    