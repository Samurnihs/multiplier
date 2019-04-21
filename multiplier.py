import sys
import cv2 as cv
import numpy as np
import os

def data_names(way): # функция, возвращающая массив с именами всех файлов в папке
    files = list() # массив с полными путями к файлам
    for (dirpath, dirnames, filenames) in os.walk(way): # считываем все имена файлов в папке и добавляем их в массив
        files.extend(filenames)
        break 
    return files


def mul_im(im_path1, im_path2): # функция, перемножающая изображения попиксельно
    pre = cv.cvtColor(cv.imread(im_path1), cv.COLOR_BGR2GRAY) # изначальное зелёное изображение
    ret, img1 = cv.threshold(pre, 100, 255, cv.THRESH_BINARY) # чтение изображения 1
    ret, img2 = cv.threshold(cv.cvtColor(cv.imread(im_path2), cv.COLOR_BGR2GRAY), 100, 255, cv.THRESH_BINARY) # чтение изображения 2
    out_mask = (img1 / 255) * (img2 / 255) * pre # перемножаем изображения
    return out_mask


input_fold1 = 'greenfold/' # папка, из которой берём зелёные картинки
input_fold2 = 'redfold/' # папка, из которой берём красные картинки
output_fold = 'result/' # папка, в которую сохраняем продукт

FileNamesGreen = data_names(input_fold1) # список имён зелёных файлов
FileNamesRed = data_names(input_fold2) # список имён красных файлов
InputFileWayGreen = list() # полные пути ко входным зелёным файлам
InputFileWayRed = list() # полные пути ко входным красным файлам
ResultFileWay = list() # полные пути к выходным файлам
for f in FileNamesGreen:
    InputFileWayGreen.append(input_fold1 + f)  # пути ко входным зелёным файлам
    ResultFileWay.append(output_fold + f) # пути к выходным файлам
for f in FileNamesRed:
    InputFileWayRed.append(input_fold2 + f) # пути ко входным красным файлам

for i in range(len(InputFileWayGreen)):
    cv.imwrite(ResultFileWay[0], mul_im(InputFileWayGreen[i], InputFileWayRed[i]))