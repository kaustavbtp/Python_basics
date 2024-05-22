
# # here x, y, z are parameter
# def calculations(x, y, z):
#     print(x, z)
#     calc = (x + y * z)
#     return calc
#     # print(calc)

# # here x, y, z are argument # positional arguments
# final_calc = calculations(2, 3, 5)   
# print(final_calc)

# # here x, y, z are argument # keyword arguments
# final_calc = calculations(2, z=3, y=5)  
# print(final_calc)



# here x, y, z are parameter
def calculations(*args, **kwargs):
    print(args, kwargs)


# here x, y, z are argument # keyword arguments
# kwargs can take keyword arguments  and  args can take positional arguments 
final_calc = calculations(2, z=3, y=5)  
final_calc1 = calculations(2, 3, y=5)  
final_calc2 = calculations(2, 3, y=5, a = "nexgen")  