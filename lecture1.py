#jocoding python lecture1

print("hello, world!\n")

a="I eat %d apples." % 3
# "I eat" + str(3) + "apples."

number=10
day="three"

b="I ate %d apples. So I was sick for %s days.\n" % (number,day)

print(a)
print(b)

a= "aasdf asdfasd fasdf {} asdfdasdf\n".format("안녕")
b= "My age is {age} and my name is {name}.\n".format(name="킹우현",age=24)

print(a)
print(b)

a="hobby"
print(a.count('b'))
print(a.find('b'))
print(a.index('b'))
print("\n")

a=",".join("abcd") #문자열 삽입
b=",".join(["a","b","c"])
print(a)
print(b)
print("\n")

a="hi"
b="HI"
c="   Hi   "
print(a.upper()) #대문자 변환
print(b.lower()) #소문자 변환
print(c.strip()) #공백 지우기
print("\n")

a="Life is too short"
print(a.replace("Life","Your leg")) #문자열 교체
print(a.split()) #문자열을 기준에 따라 잘라서 리스트에 삽입
print("\n")

a=[1,2,"int",["킹우현","퀸"]]
b=[1,2,3]
c=[4,5,6]

print(a[3][1])
print(a[0:3])
print(b+c)
print(b*3)

b[0:2]=[5,4]
print(b)

c[0:2]=[]
print(c)

del b[0]
print(b)

b.append(2)
print(b)

b.sort()
print(b)

b.reverse()
print(b)
print(b.index(3))

b.insert(0,5)
b.insert(0,5)
print(b)

b.remove(5)
print(b)

print(b.pop())
print(b)

b.insert(0,5)
print(b)
print(b.count(5))

b.extend([2,1])
print(b)
