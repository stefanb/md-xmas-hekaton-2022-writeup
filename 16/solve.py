
input=[1,1,1,1,1,1,1,0,0,0,1,0,1,1,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,0,0,0,1,1,0,0,0,0,0,1,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0,0,1,0,1,1,1,1,1,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,0,1,0,1,1,0,1,0,0,0,0,0,0,1,1,1,0,1,0,0,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,1,0,1,1,0,1,0,0,0,0,1,1,1,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,1,1,1,1,0,1,0,0,1,1,0,1,0,1,0,1,0,0,0,1,0,1,1,0,1,0,0,0,1,0,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,0,1,0,0,0,1,0,1,0,1,1,1,1,0,1,0,1,1,1,0,1,1,1,0,0,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,0,0,1,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,1,0,1,0,1,0,1,1,1,0,1,0,0,0,0,1,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,0,0,0,0,1,1,0,1,1,1,0,1,0,0,1,0,1,1,0,1,1,1,1,1,0,0,1,0,1,0,1,1,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,1,0,1,1,0,0,1,0,1,0,1,1,0,1,1,1,0,0,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,1,1,0,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,1,1,0,0,0,1,1,0,1,0,1,0,1,0,0,1,1,0,1,0,1,1,1,0,0,1,1,0,0,0,0,0,1,1,0,0,1,1,1,0,1,0,0,0,1,0,1,1,1,1,1,0,0,1,1,0,0,0,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,1,0,0,1,1,1,0,1,0,1,0,0,1,0,1,1,1,1,0,0,1,0,0,1,1,0,1,0,0,0,1,1,0,0,1,0,0,1,1,0,0,0,0,0,1]

# empty matrix, with dots to see if we're filling it correctly
result=[
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
]

def putAt(x, y, char):
    result[x][y]=char

# Spiral in from edge to center of 25x35 matrix 
# To possibly get a QR code
# Adapted from https://www.techiedelight.com/print-matrix-spiral-order/
top = left = 0
bottom = 24
right = 24
count=-1
while True:
    if left > right:
        break
    # print top row
    for i in range(left, right + 1):
        count+=1
        putAt(top, i, input[count])
    top = top + 1

    if top > bottom:
        break

    # print right column
    for i in range(top, bottom + 1):
        count+=1
        putAt(i, right, input[count])
    right = right - 1

    if left > right:
        break

    # print bottom row
    for i in range(right, left - 1, -1):
        count+=1
        putAt(bottom, i, input[count])
    bottom = bottom - 1

    if top > bottom:
        break

    # print left column
    for i in range(bottom, top - 1, -1):
        count+=1
        putAt(i, left, input[count])
    left = left + 1

# test:
# putAt(24,24, 1)
# putAt(24,22, 0)

# QR quiet zone :)
print()
print()
print()

# print resulting matrix:
for row in result:
    for col in row:
        if col==1:
            col="??????"
        elif col==0:
            col="  "
        print(col, end =""),
    print()

print()
print()
print()
