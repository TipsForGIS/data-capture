# data-capture

This is a Python module having a class for comuting some basic statistics on a collection of small positive integers.


- The module file is called DataCapture.py containing a class also called DataCapture 
- The file main.py illustrates how to use the DataCapture module.
- First we import DataCapture class from DataCapture module as:
### `from DataCapture import DataCapture`
- Then you can create a DataCapture objest as:
### `data_c = DataCapture()`
<br><br>


The following methods are implemented:

1. ### `add(int = n)`
<br>The `add` method is used basically to add or insert integers into a DataCapture object. The `add` method requires only one paramter of a positive integer. An example would be **→** `data_c.add(7)`<br><br>

2. ### `buid_stats()`
<br><br>The `build_stats` method can be used after adding integers into the DataCapture object. The `build_stats` method does not require any parameters and it should be used prior to using `less`, `greater`, or `between` methods. `build_stats` can be used as **→** `data_c.build_stats()`<br><br>

3. ### `less(int = n)`
<br><br>The `less` method basically returns the number of integers less than a given integer in the DataCapture object. For instance, if the numbers added are 2,4,3,5,1,2,6,3,5 and the given integer (parameter) is 4, then the `less` method will return 5 because there are 5 integers less than 4 which are 2,3,1,2,3. If there are no integers less than the given integer, the `less` method will return 0. This is how the `less` method can be used **→** `data_c.less(4)`<br><br>

4. ### `greater(int = n)`
<br><br>The `greater` method is the opposite of the `less` method. Using the same example if the numbers added to the DataCapture object are 2,4,3,5,1,2,6,3,5 and the given integer (parameter) is 4, the `greater` method will return 3 since there are 3 integers bigger than 4: 5,6,5. And this is how the `greater` method can be used **→** `data_c.greater(4)`<br><br>

5. ### `between(int = n, int = m)`
<br><br>The `between` method takes two parameters and returns all integers between the two parameters inclusively. Using the same example again of the added integers to the DataCapture object: 2,4,3,5,1,2,6,3,5 and passing 3 and 5, the return value will be 5: 4,3,5,3,5. In case one of the given parameters is not in the DataCapture object e.g. 5,9 then the function will return the values greater than 5. The `between` method can be used as **→** `data_c.between(3,5)`<br><br>
