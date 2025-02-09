def count_words(filename):
  try:
    with open(filename, 'r', encoding='utf-8') as f:  
      text = f.read()
      words = text.split() 
      return len(words)
  except FileNotFoundError:
    print(f"Ошибка: Файл '{filename}' не найден.")
    return None

if __name__ == "__main__":
  filename = "C:/Users/Nikit/source/repos/Compiler/Git.txt" 
  word_count = count_words(filename)
  if word_count is not None:
    print(f"Количество слов в файле '{filename}': {word_count}")