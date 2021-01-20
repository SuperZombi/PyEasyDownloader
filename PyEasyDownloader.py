import requests
import time
import threading
import sys
import os

def set_lang(LANG):
	if LANG in Downloader.languages_code:
		Downloader.lang = LANG
	else:
		print("The language is incorrect or does not exist.")

class Downloader:
	lang = "EN"

	languages_code = ["EN", "RU"]
	__languages = {
		"EN" : {"speed_KB" : " KB/sec",
				"speed_MB" : " MB/sec",

				"bytes" : " bytes",
				"KB" : " KB",
				"MB" : " MB",

				"min" : "min",
				"sec" : "sec"
				},

		"RU" : {"speed_KB" : " КБ/сек",
				"speed_MB" : " МБ/сек",

				"bytes" : " байт",
				"KB" : " КБ",
				"MB" : " МБ",

				"min" : "мин",
				"sec" : "сек"
				}
	}

	downloaded = 0
	speed = 0
	percents = 0
	finished = False
	time = None
	pause = False
	__cancel = False

	def __init__(self, link):
		self.link = link
		try:
			self.__response = requests.get(self.link, stream=True)
		except requests.exceptions.ConnectionError:
			print("Connection Error\n")
			sys.exit(0)

		self.size = int(self.__response.headers.get('content-length')) # in bytes
		self.size_KB = int(self.size/1024) # in kilobytes
		self.size_MB = round(self.size/1048576, 2) # in megabytes
		self.size_GB = round(self.size/1073741824, 2) # in gigabytes


	def size_str(self):
		if self.size > 399999:
			return str(round(self.size/1048576, 2)) + self.__languages[self.lang]["MB"]
		elif self.size > 999:
			return str(int(self.size/1024)) + self.__languages[self.lang]["KB"]
		else:
			return str(self.size) + self.__languages[self.lang]["bytes"]

	def speed_str(self):
		if self.speed > 524287:
			speed_txt = str(round(self.speed/1048576, 1)) + self.__languages[self.lang]["speed_MB"]
		else:
			speed_txt = str(self.speed//1024) + self.__languages[self.lang]["speed_KB"]
		return speed_txt

	def downloaded_str(self):
		if self.downloaded > 399999:
			return str(round(self.downloaded/1048576, 2)) + self.__languages[self.lang]["MB"]
		elif self.downloaded > 9999:
			return str(int(self.downloaded/1024)) + self.__languages[self.lang]["KB"]
		else:
			return str(self.downloaded) + self.__languages[self.lang]["bytes"]

	def time_str(self):
		if self.time != None:
			if self.time > 60:
				return str(int(self.time // 60)) + self.__languages[self.lang]["min"] + str(int(self.time % 60)) + self.__languages[self.lang]["sec"]
			else:
				return str(self.time) + self.__languages[self.lang]["sec"]

	def progress_bar(self, step=5):
		bar = "["
		i = step
		x = self.percents
		while i < 100:
			if x >= i:
				bar += "="
			else:
				bar += " "
			i+=step
		bar+="]"
		return bar


	def cancel(self, delete=True):
		self.__cancel = True
		if delete:
			if self.finished:
				try:
					os.remove(self.file_name)	
				except:
					pass



	def __downloading(self):
		with open(self.file_name, "wb") as f:
			self.__curent1 = 0
			self.__now1 = self.__start = time.time()

			for data in self.__response.iter_content(chunk_size=4096):
				if self.__cancel:
					break
				if self.pause:
					while self.pause:
						self.__start += 0.1
						time.sleep(0.1)

				self.downloaded += len(data)
				self.percents = int(self.downloaded * 100 / self.size)
				f.write(data)

				self.__now2 = time.time()
				if self.__now2 - self.__now1 > 0.5:
					self.speed = (self.downloaded - self.__curent1)*2
					self.__now1 = self.__now2
					self.__curent1 = self.downloaded


			self.finished = True
			self.__now = time.time()
			self.time = round(self.__now - self.__start, 2)
			self.speed = self.downloaded/self.time


	def download(self, file_name, thread=True):
		self.file_name = file_name
		if thread == True:
			threading.Thread(target=self.__downloading, daemon=True).start()
		else:
			self.__downloading()
