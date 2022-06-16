square_num = lambda x: x ** 2

nums = [1,2,3, 4, 5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print("Original List: ",nums)
def main():
    result = map(square_num, nums)
    print("Square the elements of the said list using map():")
    print(list(result))
if '__main__' == __name__:
    main()
