# PyEasyDownloader
Отслеживайте процесс загрузки файла.

<a href="REAME.md" ><img src="https://emojio.ru/images/twitter-64/1f1fa-1f1f8.png" width="30" height="30"></img>Read in English</a>

## <a href="https://pypi.org/project/PyEasyDownloader/">Установка </a>:

```Python
pip install PyEasyDownloader
```
</br>

## Использование:
```Python
from PyEasyDownloader import *
from time import sleep

file = Downloader(link)
print(file.size_str())

file.download("download.zip")
while file.finished != True:
	print("Downloaded: " + file.downloaded_str() + " | " + str(file.percents) + "% | Speed: " + file.speed_str())
	sleep(1)
print("Download time: " + str(file.time_str()) + " | Average speed: " + file.speed_str())
```
</br>

## Результат консоли:
```
34.3 MB
Downloaded: 5.81 MB  |  16%  |  Speed: 6.3 MB/sec
...
Download time: 6.03sec  |  Average speed: 5.7 MB/sec
```
</br></br></br>


## Давайте посмотрим детали

### Изменение языка
Это позволяет отображать единицы измерения на вашем языке. </br>
Поддерживаемые языки: </br>
Английский - **EN** </br>
Русский - **RU** </br>
```Python
set_lang("RU")
```
</br></br>

### Укажите ссылку на файл
```Python
file = Downloader("https://example.zip")
```
</br></br>

### Получите размер файла
```Python
print(file.size_str()) # автоматическое определение единицы измерения (Рекомендуется)

print(file.size) # в байтах
print(file.size_KB) # в килобайтах
print(file.size_MB) # в мегабайтах
print(file.size_GB) # в гигабайтах
```
</br></br>

### Начните загрузку
Два режима загрузки: </br>
<ul>
<li>Супер режим (Пока файл загружается, вы можете видеть фактический прогресс) </li>
<li>Обычный режим (Пока файл не будет загружен, программа не продолжит работу) </li>
</ul></br>

Пример Супер режима:

```Python
file.download("download.zip")
while file.finished != True:
  #делать что-нибудь
```

Пример Обычного режима:
```Python
file.download("download.zip", thread=False)
```
</br>

Что можно использовать в Супер режиме?

```Python
# Скорость
file.speed_str() # автоматическое определение единицы измерения (Рекомендуется)
file.speed # байты в секунду

# Загружено
file.downloaded_str() # автоматическое определение единицы измерения (Рекомендуется)
file.downloaded # в байтах

# Загружено процентов
file.percents # 

# Шкала прогресса
file.progress_bar()
```
</br>

#### Шкала прогресса
Принимает значения:</br>
**step** — *default 5* (можно не указывать)
```Python
file.progress_bar(step=int_value)
```
Пример:

```
[----------         ]
```
</br></br>

### Отображение статистики после завершения загрузки

```Python
# Время скачивания
file.time_str() # автоматическое определение единицы измерения (Рекомендуется)
file.time() # в секундах

file.speed_str() # Средняя скорость
```
