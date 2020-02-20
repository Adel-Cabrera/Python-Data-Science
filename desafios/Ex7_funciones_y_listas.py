from functools import reduce

# Map, Filter, Reduce => Functional operations in arrays

# map_array = map(lambda i: i* 2, array)
# list(map_array)

# filter_array = filter(lambda x: x % 2 == 0, array)
# list(filter_array)

def promedio(array):
  average = reduce(lambda iterator,acumulator: iterator + acumulator, array)
  return average

def all_mean(array):
  counter = 0

  mean_one = []
  acumulator_one = 0

  mean_two = []
  acumulator_two = 0

  mean_three = []
  acumulator_three = 0

  for element in array:
    mean_one.append(array[counter][1])
    mean_two.append(array[counter][2])
    mean_three.append(array[counter][4])

    acumulator_one += array[counter][1]
    acumulator_two += array[counter][2]
    acumulator_three += array[counter][4]

    counter += 1

  average_one = acumulator_one/len(array)
  average_two = acumulator_two/len(array)
  average_three = acumulator_three/len(array)

  average_list = [average_one, average_two, average_three]

  return average_list


def average_velocity(array):
  acumulator = 0
  counter = 0
  float_velocity = []

  for element in array:
    float_velocity.append(array[counter][1])
    acumulator += array[counter][1]
    counter += 1

  average = acumulator/len(array)

  average_filter = filter(lambda x: x > average, float_velocity)
  
  return list(average_filter)


def filter_bool_car(array):
  filtered_array = filter(lambda x: x[3] == True, array)
  array_true = list(filtered_array)
  map_names = map(lambda x: x[0], array_true)

  # print(list(filtered_array))
  return list(map_names)

def float_car(array):
  counter = 0

  mean_one = []
  acumulator_one = 0

  for element in array:
    mean_one.append(array[counter][1])
    acumulator_one += array[counter][1]
    counter += 1

  average_one = acumulator_one/len(array)

  average_filter = filter(lambda x: x > average_one, mean_one)

  return list(average_filter)


# 2 

def zip_vel_dis(array_one, array_two):
  
  vel = reduce(lambda iterator, acumulator: iterator + acumulator, array_one) # 770
  dis = reduce(lambda iterator, acumulator: iterator + acumulator, array_two) # 2149
  
  vel_avg = vel/len(array_one) # 15.4
  dis_avg = dis/len(array_two) # 42.98

  

  low_vel = []
  low_vel_over_dis = []
  over_vel = []
  over_vel_over_dis = []

  for element in zip(array_one, array_two):
    total_zip.append(element)
  
  print(total_zip)
  
