import os,shutil as s

audio=['.wav','.mp3','.wma']
images =['.jpeg','.jpg','.png','.tiff']
software =['.exe','.msi']
zips =['.gz','.zip','.rar']
videos =['.mp4','.avi',]
gifs  = ['.gif']
docs =['.doc','.docx','.pdf']
ppt =['.ppt','.pptx']
move_path = input('enter the path: ')
files=os.listdir(move_path)
user_path=os.path.join('c:\\','users','shurt')
'''
os.mkdir(path+"\\"+"audio")
os.mkdir(path+"\\"+"images")
os.mkdir(path+"\\"+"software")
os.mkdir(path+"\\"+"zips")
os.mkdir(path+"\\"+"videos")
os.mkdir(path+"\\"+"gifs")
os.mkdir(path+"\\"+"missilaneous")
#os.makedirs(ppt_path)'''

#paths for destination
audio_path = os.path.join(user_path,'Music')
videos_path = os.path.join(user_path,'Videos')
images_path = os.path.join(user_path,'OneDrive','Pictures')
gifs_path = os.path.join(move_path,'gifs')
zips_path = os.path.join(move_path,'zips')
docs_path = os.path.join(user_path,'OneDrive','Documents')
software_path = os.path.join(move_path,'software')
missilaneous_path = os.path.join(move_path,'missilaneous')
ppt_path =os.path.join(user_path,'\OneDrive\Documents\ppt')


#move files
for file in files:
    name,ext=os.path.splitext(file)
    if ext in audio and not os.path.exists(audio_path+"\\"+file):
         s.move(move_path+'\\'+file,audio_path)
    elif ext in images and not os.path.exists(images_path+"\\"+file):
            s.move(move_path+'\\'+file,images_path)
    elif ext in software and not os.path.exists(software_path+"\\"+file):
            s.move(move_path+'\\'+file,software_path)
    elif ext in docs and not os.path.exists(docs_path+"\\"+file):
            s.move(move_path+'\\'+file,docs_path)
    elif ext in ppt and not os.path.exists(ppt_path+"\\"+file):
            s.move(move_path+'\\'+file,ppt_path)
    elif ext in videos and not os.path.exists(videos_path+"\\"+file):
            s.move(move_path+'\\'+file,videos_path)
    elif ext in zips and not os.path.exists(zips_path+"\\"+file):
            s.move(move_path+'\\'+file,zips_path)
    elif ext == "" and not os.path.exists(missilaneous_path+"\\"+file):
            pass
    else:
            s.move(move_path+'\\'+file,missilaneous_path)

   # except FileExistError as e:
  #      print(file,' file already exists in the directry')