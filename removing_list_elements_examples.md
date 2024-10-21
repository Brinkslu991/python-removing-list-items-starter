## Python: Removing List Elements

You can remove elements from a Python list in several ways:

- Use a `del` (delete) statement
- Use the `remove( )` method
- Use the `pop()` method

### The `DEL` Statement

- You can no longer access the value you removed from the list after the `del` statement is used

```python
# Create a list of superheroes
superheroes = ["Batman", "Superman", "Wonder Woman", "Wolverine", "Iron Man"]

# Enter the index number of the list element you wish to remove
# Enclose the index number in [] square brackets
del superheroes[1] # Remove Superman from the superheroes list
print(superheroes)

# Output (Updated list)
["Batman", "Wonder Woman", "Wolverine", "Iron Man"]
```

### The `remove()` Method
- You can remove an element from a list with the `remove()` method if you don't know the element's index number
```python
# Define a list of fruits
fruits = ["apple", "banana", "orange", "grape", "strawberry"]

# Remove the orange from the list
fruits.remove('orange')

# Output (Updated list)
["apple", "banana", "grape", "strawberry"]
```

### The `pop()` Method (with and without using index numbers)
- The `pop()` method removes the last element from a list
- You can remove an element from any position in the list if you use the `pop()` method with 
an index number

```python
# Example 1
# Define a list of European capital cities
capitals = ['Paris', 'Berlin', 'Brussels', 'London', 'Madrid']

# Remove the LAST list element using the pop() method only
last_capital = capitals.pop()

# Print updated list of European capitals
print(capitals)

# Output
['Paris', 'Berlin', 'Brussels', 'London']

# Example 2
# Remove a list element using the pop() method with the element's index number
# Minnesota has an index number of 3
# Ohio has an index number of 0 (computers start counting at zero, not one)
states = ['Ohio', 'Alabama', 'Texas', 'Minnesota', 'Wyoming']
index_number = 3 # Index number for Minnesota
deleted_state = states.pop(index_number)

# Print the name of the deleted U.S. state
print(f'The state just deleted from the states list was: {deleted_state}')

# Output
The state just deleted from the states list was: Minnesota


# Example 3
# Sample list of movie titles
movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight", "Parasite"]

# Index of the movie to remove
index_to_remove = 1  # This will remove "The Matrix"

# Remove the movie and store the movie's title if needed
removed_movie = movies.pop(index_to_remove)

# Display the modified list and the removed movie using f-strings
print(f"Modified Movie List: {movies}")         # Output: ["Inception", "Interstellar", "The Dark Knight", "Parasite"]
print(f"Removed Movie: {removed_movie}")        # Output: "The Matrix"

```
