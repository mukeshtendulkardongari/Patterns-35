# 1. solid square pattern

n=int(input("Enter n value:"))

for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()

# output:
# Enter n value:5
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * *

# 2. solid rectangle


n=int(input("Enter n value:"))
m=int(input("Enter m value:"))
for i in range(1,n+1):
    for j in range(1,m+1):
        print("*",end=" ")
    print()

# output:
# Enter n value:3
# Enter m value:6
# * * * * * * 
# * * * * * *
# * * * * * *

# 3. Left aligned right-angled triangle:

n=int(input("Enter n value:"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

# output:

# Enter n value:5
# *
# * *
# * * *
# * * * *
# * * * * *

# 4.Right aligned hill pattern: and decreasing hill ,left hill

n=int(input("Enter n value:"))

for i in range(1,n+1):
    for space in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()

# output:
# Enter n value:5
#         * 
#       * *
#     * * *
#   * * * *
# * * * * *

#5. Hollow Left aligned right-angled triangle:

n=int(input("Enter n value:"))

for i in range(1,n+1):
    for j in range(1,i+1):
        if i==j or i==n or j==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# output:
# Enter n value:5
# * 
# * *
# *   *
# *     *
# * * * * *


# 6. Inverted Left aligned right-angled triangle:

n=int(input("Enter n value:"))

for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

# output:
# Enter n value:5
# * * * * * 
# * * * *
# * * *
# * *
# *

# 7.Inverted Left aligned right-angled triangle:

n=int(input("Enter n value:"))

for i in range(n,0,-1):
    for j in range(1,i+1):
        if i==j or i==n or j==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# output:
# Enter n value:5
# * * * * * 
# *     *
# *   *
# * *
# *

# 8.Right aligned right-angle triangle:

n=int(input("Enter n value:"))

for i in range(1,n+1):
    for space in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()

# output:
# Enter n value:5
#         * 
#       * *
#     * * *
#   * * * *
# * * * * *

# 9.Hollow Right aligned right-angle triangle:

n=int(input("Enter n value:"))

for i in range(1,n+1):
    for space in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        if i==j or i==n or j==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# output:
# Enter n value:5
#         * 
#       * *
#     *   *
#   *     *
# * * * * *

# 10.inverted Right aligned rigth-angled triangle:

n=int(input("Enter n value:"))

for i in range(n,0,-1):
    for space in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()

# output:
# Enter n value:5
# * * * * * 
#   * * * *
#     * * *
#       * *
#         *


# 11.Hollow inverted right aligned right-angle triangle:

n=int(input("Enter n value:"))

for i in range(n,0,-1):
    for space in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        if i==j or i==n or j==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# output:
# Enter n value:5
# * * * * * 
#   *     *
#     *   *
#       * *
#         *

# 12.Centered pyramid

n=int(input("Enter n value:"))

for i in range(1,n+1):
    for space in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1): # odd 1,3,5,7...
        print("*",end=" ")
    print()

# output:
# Enter n value:5
#         * 
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

# 13.Hollow centered pyramid:

n=int(input("Enter n value:"))

for i in range(1,n+1):
    for space in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        if j==0 or i==n or j==2*i-2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# output:
# Enter n value:5
#         * 
#       *   *
#     *       *
#   *           *
# * * * * * * * * *

# 14.Inverted centered pyramid:

n=int(input("Enter n value:"))

for i in range(n,0,-1):
    for space in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1): # odd 1,3,5,7...
        print("*",end=" ")
    print()

# output:
# Enter n value:5
# * * * * * * * * * 
#   * * * * * * * 
#     * * * * * 
#       * * * 
#         *

# 15.Hollow inverted Centered pyramid:

n=int(input("Enter n value:"))

for i in range(n,0,-1):
    for space in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        if j==0 or i==n or j==2*i-2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# output:
# Enter n value:5
# * * * * * * * * * 
#   *           *
#     *       *
#       *   *
#         *

# 16.Diamond 

n=int(input("Enter n value:"))

for i in range(1,n):
    for space in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1): # odd 1,3,5,7...
        print("*",end=" ")
    print()
for i in range(n,0,-1):
    for space in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()

# output:
# Enter n value:5
#         * 
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

# 17.right half diamond

n=int(input("Enter n value:"))

for i in range(1,n):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

# output:
# Enter n value:5
# * 
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# 18.left half diamond:

n=int(input("Enter n value:"))

for i in range(1,n):
    for space in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(n,0,-1):
    for space in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()

# output:
# Enter n value:5
#         * 
#       * *
#     * * *
#   * * * *
# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# 19.Hollow diamond:

n=int(input("Enter n value:"))

for i in range(1,n):
    for space in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        if j==0 or j==2*i-2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(n,0,-1):
    for space in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        if j==0 or j==2*i-2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# output:
# Enter n value:5
#         * 
#       *   *
#     *       *
#   *           *
# *               *
#   *           *
#     *       *
#       *   *
#         *


# 20.Butterfly 

n=int(input("Enter n value:"))
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    for spaces in range(n-i):
        print(" ",end=" ")
    for spaces in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(n,0,-1): 
    for j in range(i):
        print("*",end=" ")
    for spaces in range(n-i):
        print(" ",end=" ")

    for spaces in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

# output:
# Enter n value:5
# *                 * 
# * *             * *
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * *     * * * *
# * * *         * * *
# * *             * *
# *                 *

# 21. Hollow butterfly

n=int(input("Enter n value:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        if j==1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for space in range(n-i):
        print(" ",end=" ")

    for space in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        if j==1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n,0,-1):
    for j in range(1,i+1):
        if j==1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for space in range(n-i):
        print(" ",end=" ")

    for space in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        if j==1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# output:
# Enter n value:4
# *             * 
# * *         * *
# *   *     *   *
# *     * *     *
# *     * *     *
# *   *     *   *
# * *         * *
# *             *


# 22. hollow hourglass

n=int(input("Enter n value:"))

for i in range(n,0,-1):
    for space in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        if i==n or j==0 or j==2*i-2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(2,n+1):
    for space in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        if i==n or j==0 or j==2*i-2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# output:
# Enter n value:5
# * * * * * * * * * 
#   *           *
#     *       *
#       *   *
#         *
#       *   *
#     *       *
#   *           *
# * * * * * * * * *

# 23. sandglass right

n=int(input("Enter n value:"))

for i in range(n,0,-1):
    for space in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(1,n+1):
    for space in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()

# output:
# Enter n value:5
# * * * * * 
#   * * * *
#     * * *
#       * *
#         *
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

# 24. hollow square

n=int(input("Enter n value:"))

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==n or i==1 or j==n or j==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# output:
# Enter n value:5
# * * * * * 
# *       *
# *       *
# *       *
# * * * * *

# 25. hollow rectangle

n=int(input("Enter n value:"))
m=int(input("Enter m value:"))
for i in range(1,n+1):
    for j in range(1,m+1):
        if i==n or i==1 or j==m or j==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# output:
# Enter n value:3
# Enter m value:6
# * * * * * * 
# *         *
# * * * * * *

# 26. Increasing Number Triangle

n=int(input("Enter n value:"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

# output:
# Enter n value:5
# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# 27.repeating row number triangle

n=int(input("Enter n value:"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

# output:
# Enter n value:5
# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5


# 28.Continuous Number Triangle

n=int(input("Enter n value:"))
c=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(c,end=" ")
        c+=1
    print()

# output:
# Enter n value:5
# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15


# 29.Reverse Row Number Triangle

n=int(input("Enter n value:"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(i-j+1,end=" ")
    print()

# output:
# Enter n value:5
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

# 30.Inverted Number Triangle

n=int(input("Enter n value:"))

for i in range(n,0,-1):
    for j in range(1,i+1):
        print(i-j+1,end=" ")
    print()

# output:
# Enter n value:5
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1
# 1


# 31.Right-Aligned Number Triangle

n=int(input("Enter n value:"))

for i in range(1,n+1):
    for space in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()

# output:
# Enter n value:5
#         1 
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5

# 32.Pyramid Number Pattern

n=int(input("Enter n value:"))

for i in range(1,n+1):
    for space in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i-1,0,-1): 
        print(j,end=" ")
    print()

# output:
# Enter n value:5
#         1 
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1

# 33.Even Number Triangle

n=int(input("enter n value:"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(2*j,end=" ")
    print()

# output:
# enter n value:6
# 2 
# 2 4
# 2 4 6
# 2 4 6 8
# 2 4 6 8 10
# 2 4 6 8 10 12

# 34.Odd Number Triangle

n=int(input("enter n value:"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(2*j-1,end=" ")
    print()

# output:
# enter n value:5
# 1 
# 1 3
# 1 3 5
# 1 3 5 7
# 1 3 5 7 9

# 35.Pascal’s Triangle

n=int(input("Enter n value:"))

for i in range(n):
    num=1
    for j in range(i+1):
        print(num,end=" ")
        num=num*(i-j)//(j+1)
    print()

# output:
# Enter n value:6
# 1 
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1