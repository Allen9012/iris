name = "James"
height = 181.18
# 使用 + 运算符
str_1 = name + " has a height of " + str(height) + " cm."
print(str_1)
# 使用 %
str_2 = "%s has a height of %.3f cm." % (name, height)
print(str_2)
# 使用 str.format()
str_3 = "{} has a height of {:.3f} cm.".format(name, height)
print(str_3)
# 使用f-strings
str_4 = f"{name} has a height of {height:.3f} cm."
print(str_4)
