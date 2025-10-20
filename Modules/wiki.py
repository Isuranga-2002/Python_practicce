import wikipedia

# Search for a topic
search_term = "Python (programming language)"
result = wikipedia.summary(search_term, sentences=3)

print(f"Summary for '{search_term}':\n")
print(result)


