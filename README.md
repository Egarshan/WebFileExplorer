WebFileExplorer

с: Здравствуйте!


Инструментарий:
	- язык программирования Python
	- Framework Django
	- Sublime Text 3
	- BootStrap

Описание методов:
	.Вывод списка файлов и папок из хранилища:
		- file_list		//	происходит проверка всех файлов и папок из хранилища, добавление их в базу данных

	.Управление папками:
		- folder_create	//	создание пустой папки
		- folder_remove	//	удаление папки (не пустой тоже)
	
	.Управление файлами:
		- file_upload 	//	загрузка файла с устройства
		- file_remove	//	удаление файла

	! Фиксация файлов и обращение к ним реализовано с помощью моделей и форм !


URLS:
	http://127.0.0.1:8000/start_page/		//стартовая страница
	http://127.0.0.1:8000/new_file/
	http://127.0.0.1:8000/new_folder/

# ЗАПУСК #
	Запустить launcher.bat
	
# ОШИБКИ И БАГИ #
	*Решение проблем можно найти в папке problems_fix
	*Если лаунчер успешно запустил сервер и открыл страницу, но браузер пишет "This site can’t be reached"  - необходимо обновить страницу. //страница загрузилась быстрее сервера ;)
	