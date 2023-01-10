n = int(input("кількість боксів: "))
k = int(input("кількість пасажирів: "))
if 3<=n<=1000:                                                                                      #Обмежуємо кількість боксів
    name_list = []                                                                                  #ліфти
    list_start = []
    list_start_sort = []
    list_finish = []

    for i in range(k):                                                                              #Цим циклом ми змінюємо формат введених данних з 10:30 на float - 10.3
        data = input("введіть (Прізвище/Час здачі/Час звільнення) ").split()
        name_list.append(data[0])                                                                   #Закидаємо в ліфт по індексу введених значеннь
        list_start.append(float(data[1].split(":")[0])+float(data[1].split(":")[1])/100)            #Закидаємо час входу багажа при цьому змінюємо формат як описано вище
        list_start_sort.append(float(data[1].split(":")[0]) + float(data[1].split(":")[1]) / 100)   #Закидаємо час входу багажа при цьому змінюємо формат як описано вище в ліфт який ми будемо сортувати пізніше
        list_finish.append(float(data[2].split(":")[0])+float(data[2].split(":")[1])/100)           #Закидаємо час входу багажа при цьому змінюємо формат як описано вище
    list_start_sort.sort()                                                                          #Сортуємо список

    for i in range(len(name_list)):                                                                 #Цикл для виставлення номерів
        num = 0                                                                                     #змінна номеру 0
        for b in range(len(name_list)):                                                             #цикл по кількості значеннь прізвища
            if list_start[i] < list_finish[b] and list_finish[i] > list_start[b]:                   #Умова, яка визначає перехрещування відрізків часу
                num += 1                                                                            #якщо у мова виконалась до до номеру +1
                if list_start[i] < list_start[b]:                                                   #умова яка дає, багажу що надійшов найраніше отримати найперший номер
                    num = 1
        print(name_list[i], num)                                                                    #Прінтуємо прізвище і номер
