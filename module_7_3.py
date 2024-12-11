class WordsFinder:
    def __init__(self, *namefiles):
        self.file_names = []
        for i in namefiles:
            self.file_names.append(i)

    def get_all_words(self):
        all_words ={}
        for i in self.file_names: # i- файлы
            with open(i,encoding='utf-8') as file:
                string_ = file.read().lower() # текст файла i
            for j in ',.=!?;:' :
                string_ = string_.replace(j,'')
            string_ = string_.replace(' - ',' ')
            all_words.update({i:string_.split()})
        return all_words

    def find(self,word):
        isk_words = {}
        for name, words in self.get_all_words().items():
            isk_words.update( {name : words.index(word.lower())+1} )
        return isk_words

    def count(self,word):
        nomb_words = {}
        for name, words in self.get_all_words().items():
            nomb_words.update( {name : words.count(word.lower())} )
        return nomb_words

finder2 = WordsFinder('test_file.txt')#,'sample.txt'
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))