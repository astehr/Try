import random

class File_maker():
    """Создает новый файл с выбранными строками"""
    def __init__(self, file_path, len_new_file=10):
        self.old_file = open(file_path).readlines()
        self.len_new_file = len_new_file
        self.len_old_file = len(self.old_file)

    def connecting_func(self):
        """Соединят два следующих метода"""
        file_index = self.random_index()
        self.file_creator(file_index)

    def file_creator(self, file_index):
        """Создает новый файл со случайными строками из исходного"""
        with open(OLD_FILE_PATH.rsplit('.', 1)[0] + '_res.txt', 'w') as res:
            res.writelines(self.old_file[0])
            for i in file_index:
                res.writelines(self.old_file[i])

    def random_index(self):
        """Генерирует список с рандомными индексами строк"""
        rand_index = [random.randint(1, self.len_old_file - 1) for i in range(self.len_new_file)]
        rand_index.sort()
        i = int(0)
        while i != len(rand_index):
            if rand_index[i] == rand_index[i - 1]:
                rand_index.pop(i)
                rand_index.append(random.randint(1, self.len_old_file) - 1)
                rand_index.sort()
                i = -1
            i += 1
        return rand_index

OLD_FILE_PATH = 'File_dir/old.txt'


