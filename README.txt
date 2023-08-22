This assignment is on C++.

Compilation and Execution
--------------------------
You can compile the entire project in Linux or Unix or using Windows sub-system for Linux (wsl: https://learn.microsoft.com/en-us/windows/wsl/) using the 
Makefile. Open a terminal in the folder containing the assignment. Use the following command in the terminal to compile:

make

To clean up the object files and executables type in the following at terminal:

make clean

For Visual Studio compiler, add in all the files and compile under debug or release mode. I would suggest to unit test on debug mode and for timing use release mode for faster performance.

To execute the unit testing, type in following:
./test_algorithm.o

To execute the timing results, type in following at terminal:
./timing.o

File Description
------------------
sort.h - It contains all the algorithm implementation for sorting any sequence. Modify the functions indicated as TODO to implement your sorting algorithm. An implementation of bubble sort is provided for reference on how to use iterators and templates. 

test_algorithm.cpp - Contains the unit testing algorithms to test your implementation of slow sort and quick sort on two different data-types: integers and strings. You can add additional test algorithm functions and call them in test() function to be included in the testing sequence. 

unit_test.h - Contains the basic structure to perform any unit testing on any program based on protocol of setup, testing, and teardown. DO NOT modify this file. 

timing.cpp - Contains the code to extract execution time for various input types and input sizes. Examples of random sequences sorting are provided as example function. You need to create similar function for each sorting algorithm on sorted sequence and reverse sorted sequence as input. Call the respective function in main() with varied input sizes to get the detailed execution time report. Do not modify any function. You can add your own functions and call them respectively in main.
