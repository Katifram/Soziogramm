# Soziogramm

Creates a sociogram for pupils with green arrows for given likes and red arrows for given unlikes.

## Installation
In order to test the script please run the following commands:
```sh
pip install numpy
pip install pandas
pip install pydot
pip install IPython
pip install dataclasses
```

## Input Data
In the same Directory as main.py, create a file (already here) named InputData.csv __Delimiter ";"!!!__

The first row needs to contain exactly: name;like;dislike  

Now the columns can be filled:  
* name: name of the pupil  
* like: likes given by the pupil. Can be none, one or more names
  * if more separate by ", " 
* dislike: dislikes given by the pupil. Can be none, one or more names
  * if more separate by ", "

Keep in mind that the inputs into like/dislike need to be exactly as given in name. Otherwise a new name will be created.
