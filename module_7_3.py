class WordsFinder:
    def __init__(self, *texts):
        self.texts = texts

    def get_all_words(self):
        combined_words = []
        for content in self.texts:
            content = content.lower()
            content = content.replace("'", "").replace(".", "").replace(",", "").replace("!", "").replace("?", "").replace(";", "").replace(":", "").replace("-", "")
            words = content.split()
            combined_words.extend(words)
        return {'test_file.txt': combined_words}

    def find(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        words = all_words['test_file.txt']
        if word in words:
            result['test_file.txt'] = words.index(word) + 1
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        words = all_words['test_file.txt']
        result['test_file.txt'] = words.count(word)
        return result

if __name__ == "__main__":
    finder2 = WordsFinder(
        "It's a text for task. Найти везде, используйте его для самопроверки. Успехов в решении задачи!",
        "Text text text."
    )

    print(finder2.get_all_words())
    print(finder2.find('text'))
    print(finder2.count('text'))
