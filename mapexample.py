square_num = lambda x: x ** 2

nums = [1,2,3,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
# print("Original List: ",nums)
def main():
    result = map(square_num, nums)
    print("Square the elements of the said list using map() function:")
    print(list(result))
if '__main__' == __name__:
    main()
