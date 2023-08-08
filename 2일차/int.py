print(int(12.9))
print(int(11.30))
print(float(2))
print(float(3))
print(bool(0))
print(bool(1130))
print(bool(13.10))
print(str(3.24))
print("3+4")
print("""안녕하세요
반갑습니다
""")
print("안녕하세요\n반갑습니다")
hello = "Hello World"
print(hello[3])
print(hello[8])
print(hello[0:3])
print(len(hello))
a = 2
a = a+2
print(a)
a+=2
print(a)
a-=3
print(a)
x=10
y=10
x+=1
y*=2
print(f"x={x},y={y}")
x=3.14
y=3
v=x*y*y
print(v)
x=int(input())
y=int(input())
print(f"x==y의 결과값:{x==y}")
print(f"x!=y의 결과값:{x!=y}")
year=int(input())
if (year%4==0 and year%100!=0) or year%400==0:
    print("윤년입니다")