from DataCapture import DataCapture, is_positive_int

# create an object
capture = DataCapture()

capture.build_stats() # cannot build_stats because no positive integers added 👎

capture.add(3) # adds 3 👍
capture.add(9) # adds 9 👍
capture.add(3) # adds 3 👍
capture.add(4) # adds 4 👍
capture.add(6) # adds 6 👍

capture.add(-5) # does not add because param is a negative integer 👎
capture.add('abc') # does not add because param is a string 👎
capture.add([1,'2a','xy']) # does not add becaue param is a list 👎

capture.build_stats() # build stats 👍

print(capture.less(4)) # returns 2 (only two values 3, 3 are less than 4) 👍
print(capture.between(3,6)) # returns 4 (3, 3, 4 and 6 are between 3 and 6) 👍
print(capture.between(4,4)) # returns 1 (only one itm within the range, 4) 👍
print(capture.greater(4)) # returns 2 (6 and 9 are the only two values greater than 4) 👍


print(capture.less('a')) # returns a value error message 👎
print(capture.greater('11a')) # returns a value error message 👎
print(capture.between(6,3)) # returns an error message because n > m 👎
print(capture.less('a')) 

