from voc_eval import voc_eval
import os
FindPath = '/home/asus/project/darknet/results/'
FileNames = os.listdir(FindPath)
#for file_name in FileNames:
i = 0
SAP = 0
for file in FileNames:
    i = i +1
    file_name = file.split('.')[0]
    print 'file_name: ',file_name
    rec, prec, ap = voc_eval('/home/asus/project/darknet/results/{}.txt', '/home/asus/project/darknet/VOCdevkit/VOC2007/Annotations/{}.xml', '/home/asus/project/darknet/VOCdevkit/VOC2007/ImageSets/Main/test.txt', file_name, '.')
    print 'ap: ',ap
    SAP = SAP + ap
mAP = SAP / i
print "*****result*********"
print "mAP: ",mAP
