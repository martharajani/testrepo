square_num = lambda x: x ** 2

nums = [1,2,3,8,9,10,11,12,19,20,21,22,24,27,28,29]
def main():
    result = map(square_num, nums)
    print("Square the elements of the said list using map() function:")
    print(list(result))
if '__main__' == __name__:
    main()
