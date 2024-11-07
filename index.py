# Sample lyrics (replace this with the lyrics you want to analyze)
lyrics = """
Your lyrics go here.
You can replace this text with any song lyrics.
"""

# Function to count words
def count_words(lyrics):
    words = lyrics.split()
    return len(words)

# Function to count unique words
def count_unique_words(lyrics):
    words = lyrics.lower().split()
    unique_words = set(words)
    return len(unique_words)

# Output results
total_words = count_words(lyrics)
unique_words = count_unique_words(lyrics)

print(f"Total words: {total_words}")
print(f"Unique words: {unique_words}")
