text_to_count = "Статья рассказывает о последних научных статья об открытиях в области исследования космоса и опять статья. Интересно, что исследователи утверждают, что космическое время может быть относительным, а может быть статья."
search_word = 'статья'

count = 0

first_entry = text_to_count.lower().find(search_word)
while first_entry != -1:
    count += 1
    first_entry = text_to_count.lower().find(search_word, first_entry+1)

print(count)