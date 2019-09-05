a = int(input("Enter an integer: "))
b = int(input("Enter another integer: "))

exec(open("math_lib.py").read());

div_result = div(a, b)
add_result = add(a, b)

print("a/b = ", div_result)
print("a+b = ", add_result)