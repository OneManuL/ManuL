# **Hidden camera at the airport**
![](https://www.skladovka.ua/wp-content/uploads/2018/06/Kamera-hraneniya-Kiev.jpg)
## ***If hideout 1 is vacated, then another person can occupy that exact hideout at that time, if not, then take the free one***
___
### :ok_hand: we will ask the user for information
python
```
n = int(input("count boxes: "))
k = int(input("count pasangers: "))
```
___
### We check the quantity
>if 3<=n<=1000:
>>name_list = [] 
>>list_start_sort = []   
>>list_finish = []
___
### :ok_hand: Here we convert the time format (00:00:00) to float format and append get info to leasts.
python
```
for i in range(k):
``` 
1. *get info from user*   
python
```
    data = input("enter(Surname/time enter/time out) ").split()
    name_list.append(data[0])
```
2. *enter time*
python
```
    list_start.append(float(data[1].split(":") [0])+float(data[1].split(":")[1])/100)
    list_start_sort.append(float(data[1].split(":")[0]) + float(data[1].split(":")[1]) / 100)
```

3. *out time*
>>>list_finish.append(float(data[2].split(":")[0])+float(data[2].split(":")[1])/100)
4. *list`s sort*
>> list_start_sort.sort() 
___
### :ok_hand: We assign the numbers of the cache cameras based on the information in the letters
python
```
    for i in range(len(name_list)):
        num = 0
        for b in range(len(name_list)):
            if list_start[i] < list_finish[b] and list_finish[i] > list_start[b]:
```
- *if done, num +1*
python
````
            num += 1              
                if list_start[i] < list_start[b]:
                    num = 1
````
- *We display the names and numbers of their cells*
python
```
    print(name_list[i], num)
```
![]()