boxes = list(map(int, input().split()))
length = len(boxes)
gravity = [0 for _ in range(length)]

for i in range(length - 1):
    for j in range(i+1, length):
        if boxes[i] >= boxes[j]:
            gravity[i] = j - i
print(max(gravity))
