#input
import requests
import random
age = int(input("Enter age: "))
genre = input("Enter genre: ").lower()

if age < 12:
    age_group = "children"
else:
    age_group = ""  

url = f"https://openlibrary.org/subjects/{genre}.json?limit=20"
response = requests.get(url).json()
books = response.get("works", [])
random.shuffle(books) 

count = 0
for book in response.get("works", []):
    subjects = [s.lower() for s in book.get("subject", [])]
    
   
    if age_group == "children" and "children" not in subjects:
        continue
    if genre not in subjects:
        continue

    #output
    
    print("\nTitle:", book.get("title", "No title"))
    authors = book.get("authors", [])
    author_names = [a["name"] for a in authors]
    print("Author(s):", ", ".join(author_names) if author_names else "Unknown")
    
    count += 1
    if count == 10:  
        break
