#!/usr/bin/env python
# coding: utf-8

# In[11]:


def xml2csv(xml):
    import xml.etree.ElementTree as ET
    import numpy as np
    import pandas as pd
    import csv
    
    tree = ET.parse(xml)
    root = tree.getroot()
    
    X=[]
    for i in range(79):
        X.append(root[2][i].attrib)
    
    frame=[int(X[i]['frame']) for i in range(len(root[2]))]
    keyframe=[int(X[i]['keyframe']) for i in range(len(root[2]))]
    xtl=[float(X[i]['xtl']) for i in range(len(root[2]))]
    ytl=[float(X[i]['ytl']) for i in range(len(root[2]))]
    xbr=[float(X[i]['xbr']) for i in range(len(root[2]))]
    ybr=[float(X[i]['ybr']) for i in range(len(root[2]))]
    
    file=pd.DataFrame({"frameno":frame,"left":xtl,"top":ytl,"right":xbr,"bottom":ybr})
    
    file.to_csv("track.csv",index=False)
    return file


# In[ ]:




