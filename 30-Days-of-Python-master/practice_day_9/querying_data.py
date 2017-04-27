from alpha_day_9.alpha import messageUser

obj=messageUser()
obj.add_user("AMIT","B.Com.")
print(obj.make_message())


if __name__=="__main__":
	messageUser()

## Reason for the __name__=="__main__" call
# # file one.py
# def func():
#     print("func() in one.py")

# print("top-level in one.py")

# if __name__ == "__main__":
#     print("one.py is being run directly")
# else:
#     print("one.py is being imported into another module")

# # file two.py
# import one

# print("top-level in two.py")
# one.func()

# if __name__ == "__main__":
#     print("two.py is being run directly")
# else:
#     print("two.py is being imported into another module")