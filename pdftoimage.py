from pdf2image import convert_from_path
import cv2
import pathlib
from PIL import Image
import numpy as np
import cv2
import tensorflow as tf

from pathlib import Path
path="D:/pdf"
pdf="judgement.pdf"
pages = convert_from_path(pdf)
count = 0
pathlib.Path(path).mkdir(parents=True, exist_ok=True)
for page in pages:
     count +=1

     page.save('file-'+str(count)+'.jpg', 'JPEG')
     img = cv2.imread('file-'+str(count)+'.jpg')
     shape = img.shape
     print(shape)
