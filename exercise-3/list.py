def main():

    array_list = ["goiaba"]
    array_list_fruits = ["banana", "maca", "uva", "morango"]
    array_list_numbers = [1, 2, 3, 4]

    print("Lista sem Append!")
    print(array_list)

    for item in array_list_fruits:
        array_list.append(item)
        # print(item)

    print("Lista com Append!")
    print(array_list)

if __name__ == "__main__":
    main()
