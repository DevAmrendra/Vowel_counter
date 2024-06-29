word = list(input("Enter Your Word or Sentence ").lower())
vowel = ["a","e","i","o","u"]
vowel_counter = 0
for i in word:
    if i in vowel:
        vowel_counter+=1

print(f"Vowel: {vowel_counter}")
print(f"Spaces : {word.count(" ")}")
print(f"Consonant : {len(word)-word.count(" ")-vowel_counter}")