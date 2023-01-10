n = int(input("кількість боксів: "))
k = int(input("кількість пасажирів: "))
if 3<=n<=1000:                                                                                      #Обмежуємо кількість боксів
    name_list = []                                                                                  #ліфти
    list_start = []
    list_start_sort = []
    list_finish = []
    list_finish_sort = []

    for i in range(k):                                                                              #Цим циклом ми змінюємо формат введених данних з 10:30 на float - 10.3
        data = input("введіть (Прізвище/Час здачі/Час звільнення) ").split()
        name_list.append(data[0])                                                                   #Закидаємо в ліфт по індексу введених значеннь
        list_start.append(float(data[1].split(":")[0])+float(data[1].split(":")[1])/100)            #Закидаємо час входу багажа при цьому змінюємо формат як описано вище
        list_start_sort.append(float(data[1].split(":")[0]) + float(data[1].split(":")[1]) / 100)   #Закидаємо час входу багажа при цьому змінюємо формат як описано вище в ліфт який ми будемо сортувати пізніше
        list_finish.append(float(data[2].split(":")[0])+float(data[2].split(":")[1])/100)           #Закидаємо час входу багажа при цьому змінюємо формат як описано вище
        list_finish_sort.append(float(data[2].split(":")[0]) + float(data[2].split(":")[1]) / 100)
    list_start_sort.sort()                                                                          #Сортуємо список
    list_finish_sort.sort()

    for i in range(len(name_list)):
        list_finish_sort.append(list_start[i])
        list_finish_sort.sort()
        if list_finish_sort.index(list_start[i]) != len(list_finish_sort)-1 and list_finish_sort.index(list_start[i]) != 0:
            print(name_list[i], list_finish_sort.index(list_start[i]))
        else:
            print(name_list[i], list_start_sort.index(list_start[i]) + 1)
        list_finish_sort.pop(list_finish_sort.index(list_start[i]))
