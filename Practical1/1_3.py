sentence = input().split()

longest = sentence[0]

for word in sentence:
    if len(word) > len(longest):
        longest = word

print(longest)
print(len(longest))