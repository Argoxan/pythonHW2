
my_str = ['12', '123', '32', '32', '5', '1']
conv_list = []

def Greeter(func):
   def wrapper(*args):
    print(list)
    print("Hello, going to convert something")
    func(*args)
   return wrapper

@Greeter
def str_to_int(my_str):
    for i in range(len(my_str)):
        conv_list.append(int(my_str[i]))
    print(my_str)
    print(conv_list)
    print(f"Proof: From {type(my_str[0])} to {type(conv_list[0])}")

str_to_int(my_str)