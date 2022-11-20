import glob
import cv2
import numpy as np

IMAGE_SIZE = 12

NUM_FRAMES_PER_VIDEO = 16
targets = {"1": 0, "2": 0, "3": 1, "4": 1, "5": 2, "6": 2, "7": 3, "8": 3, "HR_1": 0, "HR_2": 1, "HR_3": 2, "HR_4": 3}

def extract_frames(path):
    #cap = cv2.VideoCapture("/home/fabo/Downloads/CASIA_faceAntisp/train_release/1/8.avi")
    cap = cv2.VideoCapture(path)
    frames = []
    is_there_frame = True
    num_total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    num_frames_captured = 16
    resampling_rate = int(num_total_frames / num_frames_captured)
    i = 0
    while is_there_frame:
        i = i + 1
        is_there_frame, frame = cap.read()
        if i % resampling_rate == 0:
                frames.append(frame)
                name = path+'_'+str(i)
                vector_path = path.split("/")
                y = targets[vector_path[-1][:-4]]
                vector_path = name.split("/")[3]
                person_path = name.split("/")[2]

                image_path = f'./images/{y}/{person_path}_{vector_path}.jpg'
                try:
                    print(image_path,path)
                    cv2.imwrite(image_path,frame)
                except:
                    continue
    return frames

def load_casia_dataset():
    num_folders = 1
    dataset_x = []
    dataset_y = []
    files = glob.glob(f'videos/train_release/**/*.avi', recursive=True)
    for f in files:
        frames = extract_frames(f)
        '''
        dataset_x = [*dataset_x, *frames]
        dataset_x = np.array(dataset_x)
        vector_path = f.split("/")
        tmp = [targets[vector_path[-1][:-4]]]*NUM_FRAMES_PER_VIDEO
        dataset_y = [*dataset_y, *tmp]
        print(dataset_y)
        '''
        
        #cv2.imwrite(f,)

    #return dataset_x, dataset_y

load_casia_dataset()