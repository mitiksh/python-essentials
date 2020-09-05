if __name__ == "__main__":
    number = 1042000
    total = 0
    while number<702648265:
        number_list = [int(x) for x in str(number)]
        length = len(number_list)
        for i in range(length):
            total = total + pow(number_list[i],length)
        if total == number:
            print(total)
            break
        else:
            number = number + 1
            total = 0












