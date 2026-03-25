# with open ("data.txt", "w") as f:
#   data = f.write("Hello, World!")


# with open ("data.txt", "r") as f:
#   data = f.read()
#   print(data)


# import os
# os.remove("data.txt")


# with open ("practice.txt", "w") as f:
#   data = f.write("Hi everyone,\n we are learning file I/0,\n using Java,\n I like programming in java")

# with open ("practice.txt", "r") as f:
#   data = f.read()
#   print (data)

# data = data.replace("java", "python")

# with open ("practice.txt", "w") as f:
#   data = f.write(data)


# with open ("practice.txt", "r") as f:
#   data = f.read()
#   if "learning" in data:
#     print("The word 'learning' is present in the file.")
#   else:
#     print("The word 'learning' is not present in the file.")


# def check_line():
#   word = "learning"
#   data = True
#   line_no = 1
#   with open ("practice.txt", "r") as f:
#     while data:
#       data = f.readline()
#       if word in data:
#         print(line_no)
#         return
#       line_no += 1
#   return -1

# check_line()


# with open ("numbers.txt", "w") as f:
#   f.write("")


# count = 0
# with open ("numbers.txt", "r") as f:
#   data = f.read()

#   nums = data.split(",")
#   print(nums)
#   for num in nums:
#     if (int(num) % 2 == 0):
#       count += 1
# print(count)





