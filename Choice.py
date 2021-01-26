from FileUtils import OLD_FILE_PATH as PATH

def person():
    """Решение человека отностельно количества строк"""
    str_file = open(PATH).readlines()
    anwser = input('Выберите число строк: ')

    try:
        anwser = int(anwser)
    except ValueError:
        print("Это не число ...")

    if type(anwser) == int:
        if 1 <= anwser <= len(str_file):
            print("Отлично, будет сделано")
        elif anwser >= len(str_file):
            print('В вашем файле нет столько строк, давайте число меньше %s' % len(str_file))
            person()
        else:
            print('Вы выбрали странное число, попробуйте другое')
            person()
    else:
        print("Ладно, не буду Вас мучать, стандартное число строк - 10")
    return anwser
