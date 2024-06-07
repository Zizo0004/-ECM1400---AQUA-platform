def sum_list(numbers):
    #set variable to 0, acts as a counter
    total = 0

    #Iterating over the numbers in the list
    for number in numbers:
        #Check if the value is a numerical type
        if isinstance(number, (int, float)):
            # If the value is a number,then add it to the total
            total += number
        else:
            # If the value is not non-numerical type, raise an exception
            raise ValueError("Invalid! Your input must be either be a list or tuple")

    #returns the sum of values
    return total

def index_of_max(values):
    # Initialize the index and maximum value variables
    index = 0
    max_value = None

    # Iterate over the values in the list
    for i, value in enumerate(values):
        # Check if the value is a number
        if isinstance(value, (int, float)):
            # If the value is a number, check if it is the maximum value seen so far
            if max_value is None or value > max_value:
                # If the value is the maximum seen so far, update the index and maximum value variables
                index = i
                max_value = value
        else:
            # If the value is not a number, raise an exception
            raise ValueError("Invalid! Your input must be either be a list or tuple")

    # Return the index of the maximum value
    return index

def minvalue(values):
  # checks to see if the input is a list or array
  if not isinstance(values, (list, tuple)):
    raise TypeError('Invalid! Your input must be either be a list or tuple')

  # checks if the values contain are only numerical types int,float,etc
  for value in values:
    if not isinstance(v, (int, float)):
      raise ValueError('Input must contain only numerical values')

  # initialize the minimum value and its index
  min_value = float('inf')
  min_index = 0

  # loop through the list/array and find the minimum value and its index
  for i, v in enumerate(values):
    if v < min_value:
      min_value = v
      min_index = i

  # return the index of the minimum value
  return min_index

def meannvalue(values):
  # checks to see if the input is a list or array
  if not isinstance(values,(list, tuple)):
    raise TypeError('Invalid! Your input must be either be a list or tuple')

  # checks if the values contain are only numerical types int,float,etc
  for value in values:
    if not isinstance(value, (int, float)):
      raise ValueError('Invalid! Input must be either a integer,float or any other numercial type')

  #calculates the addition of all values in a given list/array
  sum_total = 0
  for value in values:
    sum_total += value

  # calculate the mean by dividing total by length of array/list
  average_value = sum_total / len(values)

  # return the mean value
  return average_value

def countvalue(values, x):
  # checks to see if the input is a list or array
  if not isinstance(values, (list, tuple)):
        
    raise TypeError('Invalid! Your input must be either be a list or tuple')

  #create a varibale that stores the occcurrences of x
  count = 0

  # iterate over list/array and count the number of occurrences of x
  for value in values:
    # in the case v == x
    if value == x:
    #increment count by 1
      count += 1

  # return number of times of x occured
  return count