import FileUtils as fl
import Choice as ch

len_new_file = ch.person()

if type(len_new_file) == int:
    first_file = fl.File_maker(fl.OLD_FILE_PATH, len_new_file)
else:
    first_file = fl.File_maker(fl.OLD_FILE_PATH)

first_file.connecting_func()
