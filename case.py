import shutil
import os

#  os.listdir(path=".") - список файлов и директорий в папке.
#  os.getcwd() - текущая рабочая директория.
#  os.chdir(path) - смена текущей директории.

def main():
    '''Основная программа, которая выводит путь к текущему каталогу и меню.
    Вызывает функцию выполнения команд.'''

    directory = 'C:\\'

    print(directory)
    print('1. Просмотр каталога \n2. На уровень вверх \n3. На уровень вниз\n4. Количество файлов и каталогов\n5. Размер текущего каталога(в байтах)\n6. Поиск файла\n7. Выход из программы')
    vibor = int(input('Выберите пункт меню: '))
    return runCommand(vibor)

def acceptCommand():
    '''Запрашивает номер команды и в случае ес-ли номер команды указан некорректно,
    вы-водит сообщение об ошибке. Запрос команд осуществляется до тех пор, пока не
    введен корректный номер команды. Возвращает корректный номер команды.'''

def runCommand(command):
    '''Определяет по номеру команды command, какую функцию следует выполнить.'''
    if command == 1:
        files = os.listdir(ПУТЬ К ФАЙЛУ)
        print(files) #выведет названия файлов из каталога
    elif command == 2:
        # нужно урезать текущий путь на имя текущего файла
    elif command == 3:
        # что вообще значит на уровень вниз? пусть выбирает куда идти..
        print(runCommand(1)) # выведем ему файлики из текущего каталога
        currentDir = int(input('Введите имя подкаталога: '))
        moveDown(currentDir)

    elif command == 4:
        print(countFiles(path))

    elif command == 5:
        # кому это вообще надо..

    elif command == 6:


    elif command == 7:
        exit() #ыхыхыхых


def moveUp():
    '''Делает текущим родительский каталог.'''

def moveDown(currentDir):
    '''Запрашивает имя подкаталога. Если имя указано корректно делает каталог находящийся
    в currentDir текущим, иначе выводит сообщение об ошибке.'''

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
    main()