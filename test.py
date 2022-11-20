import glob
import cv2
import os
targets = {"1": 0, "2": 0, "3": 1, "4": 1, "5": 2, "6": 2, "7": 3, "8": 3, "HR_1": 0, "HR_2": 1, "HR_3": 2, "HR_4": 3}

#model = load_model('./converted_keras/keras_mode.h5')

def test_video(path):
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

                image_path = f'./images/test/{y}/{person_path}/{vector_path}.jpg'
                if not os.path.isdir(f'./images/test/{y}/{person_path}'):
                    os.makedirs(f'./images/test/{y}/{person_path}')
                print(image_path)
                try:
                    cv2.imwrite(image_path,frame)
                except:
                    continue


files = glob.glob(f'videos/test_release/**/*.avi', recursive=True)
for f in files:
    r = test_video(f)