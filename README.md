# Password Strength Calculator

Script for check how good or bad is your password

# How yo use

You need Python 3+ interpreter
You need write password, which you want to check, when script ask you for it.
Optionaly you can give script a path to file with bad passwords, that got rate 0 as argument. 
If you don't enter a path to file, script will try to find file black_list.txt in the same directory where you run script.
If default file won't be found, script will run, but it rate evident password (for example '11111' or 'password') like any other 

```bash
python password_strength.py 'path_to_black_list_file'

Please enter your password
```
Example of result:
```python
On scale of 1 to 10 your password got 'number_of_points'
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
