#!/usr/bin/env python
# coding: utf-8

# In[8]:


#py

import glob
from PIL import Image

class GifConverter :
    def __init__(self, path_in=None, path_out=None, resize=(320,240)) : 
        """
        path_in : 원본 여러 이미지 경로(ex: images/*.png)
        path_out : 결과 이미지 경로(ex: output/filename.gif)
        resize : 리사이징크기((320,240))
        """
        
        self.path_in = path_in or './*.png'
        self.path_out= path_out or './output.gif'
        self.resize=resize
        
    def convert_gif(self):
        """
        giif 이미지 변환 기능 수행
        """
        
        print(self.path_in, self.path_out, self.resize)
        
        img, *images =         [Image.open(f).resize(self.resize, Image.ANTIALIAS) for f in sorted(glob.glob(self.path_in))]

        try:
            img.save(
                fp = self.path_out,
                format='GIF',
                append_images = images,
                save_all = True,
                duration=500,
                loop=0
            )
        except IOError:
            print('cannnot convert!', img)
            
if __name__== '__main__' :             
    #test
    c = GifConverter('./project/images/*.png', './project/image_out/result.gif', (400,400))
    c.convert_gif()


# In[ ]:



