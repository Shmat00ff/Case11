import os

#  os.listdir(path=".") - список файлов и директорий в папке.
#  os.getcwd() - текущая рабочая директория.
#  os.chdir(path) - смена текущей директории.

def main(directory):
    '''Основная программа, которая выводит путь к текущему каталогу и меню.
    Вызывает функцию выполнения команд.'''

    directory = os.getcwd()

    print(directory)
    print('1. Просмотр каталога \n2. На уровень вверх \n3. На уровень вниз\n4. Количество файлов и каталогов\n5. Размер текущего каталога(в байтах)\n6. Поиск файла\n7. Выход из программы')
    vibor = int(input('Выберите пункт меню: '))
    return runCommand(vibor, directory)


def runCommand(command, directory):
    '''Определяет по номеру команды command, какую функцию следует выполнить.'''
    if command == 1:
        print(os.listdir(directory))
        #выведет названия файлов из каталога

    elif command == 2:
        os.chdir(os.getcwd()[:os.getcwd().rfind("\\")])
        print(os.getcwd())
        main(os.getcwd())

    elif command == 3:
        print(os.getcwd())
        runCommand(1, directory)
        currentDir = str(input('Введите имя подкаталога: '))
        os.chdir(path = currentDir)
        main(os.chdir(path = currentDir))

    elif command == 4:
        print(countFiles(path))

    elif command == 5:
        # кому это вообще надо..
        print(countBytes(path))




def countFiles(path):
    '''
    Рекурсивная функция подсчитывающая количество файлов в указанном каталоге path.
    В подсчет включаются все файлы, находящиеся в подкаталогах. Возвращает количество файлов.'''

    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


    onlyfiles = next(os.walk(dir))[2]  # dir is your directory path as string
    print
    len(onlyfiles)

    for root, dirs, files in os.walk("/mydir"):
        for file in files:
            if file.endswith(".txt"):
                print(os.path.join(root, file))

def countBytes(path):
    '''Рекурсивная функция подсчитывающая суммарный объем (в байтах) всех файлов в указанном каталоге path.
     В подсчет включаются все файлы, находящиеся в подкаталогах. Возвращает суммарное количество байт.'''

    def get_size(start_path='.'):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size



def findFiles(target, path):
    '''Рекурсивная функция, формирующая список путей к файлам, в имени которых содержится target.
     В поиск включаются все подкаталоги каталога path. В случае если файлы не найдены, выводит
     соответствующее сообщение.'''

if __name__ == '__main__':
    main(os.getcwd())