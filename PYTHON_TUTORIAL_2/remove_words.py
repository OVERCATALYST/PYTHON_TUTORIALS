def remove_words(text, words_to_remove):
    words=text.split()
    result=[word for word in words if word not in words_to_remove]
    return " ".join(result)

text=input("Enter a sentence: ")
words_to_remove=input("Enter words to remove (separated by spaces): ").split()

print("Modified sentence:",remove_words(text,words_to_remove))
