"""Case-study #11
Разработчики:
Bayanova A. 70%, Shmatov D. 60%
"""

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
    if vibor in [1,2,3,4,5,6,7]:
        return runCommand(vibor, directory)
    else:
        print('Вы ввели неверное значение.')
        main(os.getcwd())


def runCommand(command, directory):
    '''Определяет по номеру команды command, какую функцию следует выполнить.'''
    if command == 1:
        print(os.listdir(directory))
        main(directory)

    elif command == 2:
        os.chdir(os.getcwd()[:os.getcwd().rfind("\\")])
        print(os.getcwd())
        main(os.getcwd())

    elif command == 3:
        print(os.getcwd())
        print(os.listdir(directory))
        try:
            currentDir = str(input('Введите имя подкаталога: '))
            os.chdir(path = currentDir)
            main(os.chdir(os.getcwd()))
        except FileNotFoundError:
            print('Вы ввели неверное имя файла.')
            runCommand(3, directory)

    elif command == 4:
        print(countFiles(directory))
        main(os.getcwd())

    elif command == 5:
        print(countBytes(directory))
        main(os.getcwd())

    elif command == 6:
        target = input('Введите имя файла: ')
        if findFiles(target, directory):
            print(findFiles(target, directory))
            main(os.getcwd())
        else:
            print('Файлы с таким именем не найдены.')
            runCommand(6, directory)

    elif command == 7:
        exit()



def countFiles(path):
    '''
    Рекурсивная функция подсчитывающая количество файлов в указанном каталоге path.
    В подсчет включаются все файлы, находящиеся в подкаталогах. Возвращает количество файлов.'''
    a = []
    for top, dirs, files in os.walk(path):
        for nm in files:
            a.append(os.path.join(top, nm))
    print(len(a))


def countBytes(path):
    '''Рекурсивная функция подсчитывающая суммарный объем (в байтах) всех файлов в указанном каталоге path.
     В подсчет включаются все файлы, находящиеся в подкаталогах. Возвращает суммарное количество байт.'''

    m = 0
    for top, dirs, files in os.walk(os.getcwd()):
        for nm in files:
            m += os.path.getsize(os.path.join(top, nm))

    print(m)



def findFiles(name, path):
    for root, dirs, files in os.walk(path):
        if name in files or name in root or name in dirs:
            return os.path.join(root, name)


    '''Рекурсивная функция, формирующая список путей к файлам, в имени которых содержится target.
     В поиск включаются все подкаталоги каталога path. В случае если файлы не найдены, выводит
     соответствующее сообщение.'''

if __name__ == '__main__':
    main(os.getcwd())