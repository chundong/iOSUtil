__author__ = 'feihu'
#svg 转换为png，这里调用了convert 命令，原因是mac下面下载不了cairo，就先这样做了
#svg的图片可以http://icomoon.io/app/ 下载
import xml.etree.ElementTree as ET
import os
import subprocess

for path, dirs, files in os.walk('路径'):
    #print root
    for file in files:
        #print file
        if file.endswith('.svg'):
            print 'find svg'
            doc = ET.parse(path+'/'+file)
            root = doc.getroot();
            print root.tag
            print root.attrib['fill']
            #设置填充颜色
            root.set('fill','#ff0000')
            print root.attrib['fill']
            doc.write(path+'/'+file)
            df = path+'/'+file
            sf = path+'/'+file+'.png'
            t = ['convert ',df,sf]
            print t
            os.environ['PATH'] += os.pathsep + '/opt/local/bin'
            os.system('convert '+ df+ ' ' + sf)
            #subprocess.call(t )