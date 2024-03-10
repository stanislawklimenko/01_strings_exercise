# 1 Fill missing pieces
original = " Python strings are COOL! "
lower_cased = original.lower()
stripped = original.strip()
stripped_lower_cased = original.lower().strip()

# 2  Fill missing pieces
ugly = " tiTle of MY new Book\n\n"
pretty = ugly.lower().title().strip()

# 3 Format string based on existing variables
verb = "is"
language = "Python"
punctuation = "!"
# Your implementation:
sentence = f"Learning {language} {verb} fun{punctuation}"