# tuple

n = int(input())
integer_list = map(int, input().split())

t = tuple(integer_list)

result = hash(t)

print(result)