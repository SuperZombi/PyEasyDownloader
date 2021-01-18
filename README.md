# PyEasyDownloader
Track the file download process.

<a href="README_RU.md" ><img src="https://emojio.ru/images/twitter-64/1f1f7-1f1fa.png" width="30" height="30"></img>Читать на Русском</a>

## <a href="https://pypi.org/project/PyEasyDownloader/">Installation </a>:

```Python
pip install PyEasyDownloader
```
</br>

## Usage:
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

## Console result:
```
34.3 MB
Downloaded: 5.81 MB  |  16%  |  Speed: 6.3 MB/sec
...
Download time: 6.03sec  |  Average speed: 5.7 MB/sec
```
</br></br></br>


## Let's see the details

### Change the language
This allows the units of measurement to be displayed in your language. </br>
Supported languages: </br>
English - **EN** </br>
Russian - **RU** </br>
```Python
set_lang("RU")
```
</br></br>

### Indicate a link to the file
```Python
file = Downloader("https://example.zip")
```
</br></br>

### Get file size
```Python
print(file.size_str()) # auto size (Recommended)

print(file.size) # in bytes
print(file.size_KB) # in kilobytes
print(file.size_MB) # in megabytes
print(file.size_GB) # in gigabytes
```
</br></br>

### Start download
Two download modes: </br>
<ul>
<li>Super mode (While the file is downloading, you can receive actual progress) </li>
<li>Standard mode (Until the file is downloaded, the program will not continue) </li>
</ul></br>

Super mode example:

```Python
file.download("download.zip")
while file.finished != True:
  #do something
```

Standard mode example:
```Python
file.download("download.zip", thread=False)
```
</br>

What can be used in Super Mode?

```Python
file.speed_str() # auto (Recommended)
file.speed # bytes per second

file.downloaded_str() # auto (Recommended)
file.downloaded # bytes

file.percents

file.progress_bar()
```
</br>

#### Progress bar
Takes values:</br>
**step** — *default 5* (optional to indicate)
```Python
file.progress_bar(step=int_value)
```
Example:

```
[==========         ]
```
</br></br>

### Display statistics after download is complete

```Python
file.time_str() # auto (Recommended)
file.time() # in seconds

file.speed_str() # average speed
```
