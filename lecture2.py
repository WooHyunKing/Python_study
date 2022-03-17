#jocoding python lecture2
from copy import copy

#튜플은 리스트와 다르게 변하지 않는다, 즉 고정되어 있다 !
t1=(1,2,'a','b')
t2=(3,4)
#del t1[0] -> X, 튜플은 값 추가 및 수정 불가능(고정)

print(t1[0:2])
print(t1+t2)
print("\n")

#딕셔너리란 연관 배열/해시 라고 불리며 Key를 통해 Value를 얻는다
#딕셔너리의 핵심은 Key와 Value로 이루어져 있다는 것이다 !
dic={'name':'King','age':24}
print("My name is "+dic['name'])
print("My age is %d" % dic['age'])
print("\n")

a={1:'a'}
a['name']="익명"
print(a)

del a[1]
print(a)
print("\n")

a={1:'ㄱ',2:'ㄴ',3:'ㄷ'}
print(a.keys())
print(a.values())
print(a.items())

for k in a.keys():
    print(k)
for k in a.values():
    print(k)
for k,v in a.items():
    print("키는: "+str(k))
    print("벨류는: "+v)

a.clear()
print(a)
print("\n")

a={1:'ㄱ',2:'ㄴ',3:'ㄷ'}
print(a[1])
print(a.get(1)) 
print(a.get(4,'없음')) #get은 없는 Key를 호출하면 None을 반환
print(4 in a)
print(1 in a)
print("\n")

#집합 자료형이란 집합에 관련된 것들을 쉽게 처리하기 위해 만들어진 자료형
#집합의 핵심은 중복된 요소를 가질 수 없다, 즉 원소가 고유하다 !
#순서가 없다(Unordered).
s1=set([1,2,3]) #s1={1,2,3}
print(s1)
print(type(s1))
print("\n")

l=[1,2,2,3,3]
newList=list(set(l))
print(newList)
print("\n")

s1=set("Hello")
print(s1)
print("\n")

s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])
print(s1&s2)
print(s1.intersection(s2))
print(s1|s2)
print(s1.union(s2))
print(s1-s2)
print(s1.difference(s2))

s1.add(7)
print(s1)
s1.update([8,9,10])
print(s1)
s1.remove(1)
print(s1)
print("\n")

#불 자료형은 True와 False로 이루어져 있다.
#문자열/리스트/튜플/딕셔너리 자료형에 값이 있으면 참, 비어있으면 거짓
#참은 1, 0과 None은 거짓

a= "안녕"
if a:
    print(a)

a=[1,2,3,4]
while a:
    a.pop()
    print(a)
print("\n")

#파이썬에서 사용하는 변수는 객체(자료형)를 가리키는 것
#변수는 메모리의 주소를 가지고 있는 것이다.

a=[1,2,3]
b=a
a[1]=4
print(a)
print(b)
print(id(a))
print(id(b))
print(a is b) #두 변수가 같은 주소를 가지고 있는가? 같은 주소를 가리키고 있는가?
print("\n")

a=[1,2,3]
b=a[:] #슬라이싱해서 새로운 리스트를 만들어 넘겨준다(복사)
a[1]=4
print(a)
print(b)
print(id(a))
print(id(b))
print(a is b)
print("\n")

a=[1,2,3]
b=copy(a)
a[1]=4
print(a)
print(b)
print(id(a))
print(id(b))
print(a is b)
print("\n")

(a,b)=('python','life')
print(a)
print(b)

[a,b]=['python','life']
print(a)
print(b)

a=b='hello'
print(a)
print(b)

a=3
b=5
a,b = b,a
print(a)
print(b)
