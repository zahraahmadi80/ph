n = int(input())
names = input().split(",")
heights = input().split("|")
name = input()

for i in range(n):
    heights[i] = int(heights[i])
    
for i in range(n):
    for j in range(i + 1, n):
        if heights[i] < heights[j]:
            heights[i], heights[j] = heights[j], heights[i]
            names[i], names[j] = names[j], names[i]
            
i = 0

while names[i] != name:
    i = i + 1
    
print(i + 1)