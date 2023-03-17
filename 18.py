import random

 a= int(input("vvedite kolichestvo elementov v masive "))
 list = [random.randint(1, 20) for i in range(a)]
 print(list)
 x = int(input("vvedite iskomoe chislo"))
 index_element = 0
 min_element = abs(x - list[0])
 for i in range(1, a):
 buffer_element = abs(x -list[i])
 if buffer_element < min_element:
        min_element = buffer_element
        index_element = i
print("samoe blizkoe {list[index_element]}")
