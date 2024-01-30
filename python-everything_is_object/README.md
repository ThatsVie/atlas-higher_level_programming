# Paws and Python, A Pug Enthusiast’s Writing Assignment

By: Vie Paula	 January 23, 2024

![download](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/dcee4683-6d86-489b-9b86-02e8b3522296)

In my world of coding, where days are dedicated to crafting logic through lines of code, there's a parallel universe of joy and companionship: the realm of pugs. This week, as I begin learning the intricacies of Python, I share discoveries about object identity and mutability – the essence of Python - imbued with a generous dose of pug love.

## ID and Type: Unmasking Digital Paw-sonalities

Just as pugs boast unique paw-sonalities, every Python object possesses an individual identity, revealed through the id() function. The adorable_pug dictionary is assigned a unique identifier, an important step in understanding mutable and immutable entities. In Python, everything is an object and each object has a type. Python is a dynamically typed language meaning that the type of variable is determined at runtime. The type() function reveals the specific data type of the object, offering insights into its characteristics and behavior.

Creating a dictionary named adorable_pug with key value pairs representing pug characteristics

adorable_pug = {"wrinkles": "many", "playfulness": "endless"}

Printing the unique identifier (memory address) and type of adorable_pug dictionary

print("Adorable Pug Details:")

print("ID: {}".format(id(adorable_pug)))

print("Type: {}".format(type(adorable_pug)))

Output

Adorable Pug Details:

ID: <hexidecimal_number_that_will_be_assigned_to_adorable_pug_at_run_time>

Type: <class ‘dict’>


## Mutable Objects: Puggy Flexibility 

Mutable objects, such as lists and dictionaries, mimic the adaptable nature of pugs, allowing alterations post-creation. Similar to a pug's dynamic transformations, mutable objects, like pug_tricks_list, enable fluid changes, and their shared references propagate modifications to all aliases.

 Initializing  a list of pug tricks 
 
pug_tricks_list = ["snuggles", "zoomies", "naptime"]

 Sorting the original memory address of pug_tricks_list
 
original_id = id(pug_tricks_list)

 Appending the element ‘treats’ to pug_tricks_list
 
 pug_tricks_list.append("treats")
 
 Printing whether the memory address of pug_tricks_list has changed after the modification
 
print("Memory address of pug_tricks_list changed: {}".format(original_id == 

id(pug_tricks_list))) 

 Output: Memory address of pug_tricks_list changed: True

## Immutable Objects: Pillars of Com-pawsure

Immutable objects, exemplified by tuples and strings, echo the composure of pugs and remain unmodifiable once created. As with a pug's steadfast demeanor, immutability ensures stability, necessitating the creation of new objects for any desired alterations.

 Creating a string representing digital pug calmness with the value “Python”
 
digital_pug_calmness = "Python"

 Storing the original memory address of the digital_pug_calmness string
 
original_id = id(digital_pug_calmness)

 Attempting to modify the first character of the string from P to C (immutable operation) which raises a TypeError
 
 Note: Strings are immutable in Python, the following line will raise an error
 
digital_pug_calmness[0] = 'C' 

TypeError: ‘str’ object does not support item assignment

 Printing whether the memory address of digital_pug_calmness has changed after the attempted modification
 
print("Memory address of digital_pug_calmness changed: {}".format(original_id == 
id(digital_pug_calmness))) 

Output: Memory address of digital_pug_calmness changed: False


## Python's Handling: Mutable vs Immutable

In Python, mutable objects share references, causing changes to cascade across all aliases. On the other paw, immutable objects maintain their original state even when assigned to a new variable. The distinction reflects the interconnected dynamics between pugs and the coding world.

 Initializing a list of trick_repertoire
 
trick_repertoire = ["fetch", "sniff", "roll over"]

 Creating a new reference (paw_prints) to the same list
 
paw_prints = trick_repertoire

 Appending the element ‘belly rubs’ to the trick_repertoire list
 
trick_repertoire.append("belly rubs")

 Printing the contents of paw_print list which shares the same reference as trick_repertoire
 
print("Contents of paw_prints: {}".format(paw_prints))

Output: Contents of paw_prints: ["fetch", "sniff", "roll over", "belly rubs"]

## Function Arguments: Curly Tail-wagging Tech

Python's approach to function arguments, termed "call by object reference," unfolds with the adaptability of mutable objects mirroring a puggy's ever-expanding trick repertoire. Mutable objects within functions reflect external changes, while immutable objects retain their pristine state.

 Defining a function fetch_stick that takes a list of tricks as an argument and appends ‘catch’ 
 
def fetch_stick(tricks):

tricks.append("catch")

 Initializing a list of puggy_tricks
 
puggy_tricks = ["sit", "stay"]

 Calling the fetch_stick function with ‘puggy_tricks’ as an argument, modifying the list
 
fetch_stick(puggy_tricks)

 Printing the modified puggy_tricks list
 
print("Modified puggy_tricks: {}".format(puggy_tricks)) 

Output: Modified puggy_tricks: ["sit", "stay", "catch"]

## Insights: Merging Pug Adoration with Coding Proficiency

Mutable and immutable objects become metaphors for the adaptability and stability I cherish in pugs. This project not only deepened my coding understanding but also fortified my dreams of having a pug companion by my side, fostering an environment where coding and problem-solving intertwine seamlessly with puggy companionship. I dream of a future filled with the delightful presence of a loyal pug, a perfect companion for my coding process. Now, to convince my landlord.
