from os import *
from os.path import join, exists
import cv2

video_path = '/media/abc/Program/人工智能-CBREN-main/datasets/hevc_cbr_low_mp4/D'
save_path = '/media/abc/Program/人工智能-CBREN-main/datasets/hevc_cbr_low_mp4/D'

for i in listdir(video_path):
    print(i)
    
    # 只处理 mp4 文件
    if i.endswith('.mp4'):
        full_video_name = i.split('.')
        video_name = full_video_name[0]

        cap = cv2.VideoCapture(join(video_path, f'{video_name}.mp4'))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # 获取视频的总帧数

        # 创建保存帧的文件夹
        current_save_path = join(save_path, video_name)
        if not exists(current_save_path):
            mkdir(current_save_path)

        for j in range(1, total_frames + 1):
            ret, frame = cap.read()
            if not ret:
                break

            # 保存每一帧
            print(f'Writing video [{video_name}] frame [{j}]')
            cv2.imwrite(join(current_save_path, f'{j:03d}.png'), frame)

        cap.release()

print('Finish extracting frames.')

