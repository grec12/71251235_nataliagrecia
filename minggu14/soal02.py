def demonstrasi_konversi():
    data_list = [1, 2, 3, 4, 5]

    data_set = set(data_list)
    print("List menjadi Set:", data_set)

    data_list_dari_set = list(data_set)
    print("Set menjadi List:", data_list_dari_set)

    data_tuple = tuple(data_list)
    print("List menjadi Tuple:", data_tuple)

    data_tuple_dari_set = tuple(data_set)
    print("Set menjadi Tuple:", data_tuple_dari_set)

demonstrasi_konversi()

