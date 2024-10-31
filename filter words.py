words = ["selftaught",
"code", "sit", "eat", "programming", "dinner", "one", "two", "coding",
"a", "tech"]

filter_words = [word for word in words if len(word) < 4]
print(filter_words)