# foodChart

This is a simple demonstration of web scraping with python. It uses the requests library and BeautifulSoup4 to retrieve food charts from "mashie.com". The program is intended for educational purposes only.

Usage
-------------------

1. Run the installer.py by typing ``python installer.py``
2. Second - Use the ``get_food()`` method inside food.py to retrieve the food charts. The file also includes documentation of usage

Example
-------------------

1. Run the installer.py file
2. Put the food.py in your project folder
3. Make a python file in that folder
4. Type this in your python file

```python
from food import get_food
from food import print_array

s, v = get_food() #s recieves the standard food and v recieves the vegetarian food

print('\nStandard\n')
print_array(s)

print('\nVegetarian\n')
print_array(v)

```
