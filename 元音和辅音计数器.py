vowels = "aeiou"

ip_str = "Hello, have you tried our tutorial section yet?"

# 统计元音和辅音的数量
vowel_count = 0
consonant_count = 0

for char in ip_str:
    if char in vowels:
        vowel_count += 1
    else:
        consonant_count += 1

print("元音数量:", vowel_count)
print("辅音数量:", consonant_count)