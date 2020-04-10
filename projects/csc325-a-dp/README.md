# Using Git and Github
You got to this page by clicking on the link i sent you by email.

1. Click on clone or download button then click on the right of the link to copy it
1. Open GitHub desktop and log in using your username/password
1. Select File->clone repository
1. Select your github repository and set the local directory
1. Open visual studio and select continue without code (bottom right)
1. Select File->New->Project from existing code. In the project file location select the directory
where you have clone the github repository.
1. Type a project name then next
1. Project type select console application

Now you can make the necessary changes to the code (see below). When you are done use
github Desktop to PUSH the changes back to the server.

# csc325-a-dp
This is the code for subset sum and sequence alignment. In both cases the code gives the optimal "values".
Add two functions to obtain the **ACTUAL** solution. 
1. in the case of subset sum you need to write a function
  ```vector<int> ss_sol()```
  which returns the subset of numbers in a C++
  ```vector<int>```  
1. in the case of sequence alignment you need to write a function
 ```vector<string> sa_sol()``` 
 where the first and second elements of the vector are the modified X and Y (i.e. with gaps included)
