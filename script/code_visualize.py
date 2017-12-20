import os,cv2

annotation_folder = "/media/minhkv/Data/HocTap/DaiHoc/MasterI/datasets_mica/Annotation_dataset"
video_folder = "/media/minhkv/Data/HocTap/DaiHoc/MasterI/datasets_mica/compressed_dataset"

list_annotation = sorted(os.listdir(annotation_folder))
file_id = 0
annotation_path = os.path.join(annotation_folder, list_annotation[file_id])
video_path = os.path.join(video_folder, os.path.splitext(list_annotation[file_id])[0], 'kinect_3.avi')

f=open(annotation_path,'rt')
lines=f.read().strip().split('\n')
lines = [s.replace('\xef\xbb\xbf', '') for s in lines]
print lines

vid=cv2.VideoCapture(video_path)
count=0
gt=[]
for i in xrange(10000):
	gt.append('')

for l in lines:
	a= l.split(';')
	for r in range(int(a[1]),int(a[2])):
		gt[r]=a[0]


count=0

while True:
	ret,img=vid.read()
	ret,img=vid.read()
	cv2.putText(img,gt[count],(10,100), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,255,0),8)#,cv2.LINE_AA)
	img=cv2.resize(img,(1080,800))
	cv2.imshow('',img)

	ret=cv2.waitKey(1)
	count+=2
	
	if ret==27:
		break
