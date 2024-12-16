# Домашнее задание по конфигурационному управлению
## Павлов Никита ИКБО-50-23
## Общие этапы сборки проектов репозитория
1. Загрузить репозиторий на компьютер
```
git clone https://github.com/n1kpavlov/Shell_Emulator
cd Shell_Emulator
```
2. Создать в корне репозитория виртуальную среду python и активировать её.
```
python3 -m venv venv
source venv/bin/activate
```
## Задание
### Описание
Эмулятор для языка оболочки ОС, похож на сеанс shell в UNIX-подобной ОС. Имеет свой GUI. Рядом с программой находится файл config.xml, в котором указаны путь до стартового скрипта и .tar архив с файловой системой.

### Функции
- Эмуляция команд: ls, cd, exit, uname, pwd, tree;
- Исполнение стартового скрипта при запуске эмулятора.
## Старт проекта
Запустить Console.py
```
python Console.py
```

## Примеры работы программы
![image](https://github.com/user-attachments/assets/03a47e32-71b2-4723-923b-27f39a396235)
![image](https://github.com/user-attachments/assets/eefd36b5-5e44-465f-a131-db4e7405449d)
![image](https://github.com/user-attachments/assets/27d219b4-0080-430a-a307-dd901ec74e50)

## Тестирование
### Тест комады ls
```
def test_ls(self):
  self.assertEqual(self.file_system.ls(), ['boot', 'dev', 'home', 'readme.txt', 'usr', 'var'])
  self.file_system.cd('usr')
  self.assertEqual(self.file_system.ls(), ['Anton', 'Artem', 'Nikita', 'Yaroslav'])
```
### Тест комады cd
```
def test_cd(self):
  self.file_system.cd('home')
  self.assertEqual(self.file_system.current_dir, 'virtual_fs/home')
  self.file_system.cd('..')
  self.assertEqual(self.file_system.current_dir, 'virtual_fs')
```
### Тест комады uname
```
def test_uname(self):
  self.assertEqual(self.file_system.uname(), 'Linux')
  self.file_system.cd('usr')
  self.assertEqual(self.file_system.uname(), 'Linux')
```
### Тест комады pwd
```
def test_pwd(self):
  self.assertEqual(self.file_system.pwd(), 'virtual_fs')
  self.file_system.cd('home')
  self.assertEqual(self.file_system.pwd(), 'virtual_fs/home')
```
### Тест комады tree
```
def test_tree(self):
  self.assertEqual(self.file_system.tree(), 'boot/\ndev/\nhome/\n  secrets/\n    dont open.txt\nreadme.txt\nusr/\n  Anton/\n  Artem/\n  Nikita/\n  Yaroslav/\nvar/\n')
  self.file_system.cd('home')
  self.assertEqual(self.file_system.tree(), 'secrets/\n  dont open.txt\n')
```
### Тест загрузки конфига
```
def test_load_config(self):
  config = Config('config.xml')
  self.assertEqual(config.tar_path, 'virtual_fs.tar')
  self.assertEqual(config.start_script_path, 'start.sh')
```
![image](https://github.com/user-attachments/assets/3e4b0c85-d490-44bd-bd1f-f7730fe838d8)
