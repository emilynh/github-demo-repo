def Square(x):
    return x**2

a=float(input("Enter a\n"))
print("Binh phuong cua so",a,"la",Square(a))


if __name__ == '__main__':
    print(Square(-2)) # 4
    print(Square(5)) # 25
    print(Square(0)) # 0