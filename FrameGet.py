""""
Name: Thijs Ermens
Date: 5-11-2021
Function: This script is for extracting frames from a video every 5 minutes
"""
import cv2
import os


def frame_maker(videos):
    """
    With this function the list of videos can be split into frames.
    25 frames per second (7500 is 5 min, 1500 is 1 min, 750 is 30 sec)
    :param videos: list of videonames that have to split into frames
    :return:
    """
    path = 'frames'
    for video in videos:
        framecount = -1
        cap = cv2.VideoCapture(os.path.join((os.path.join(os.getcwd())),
                                            video))
        jump = 11250
        while cap.isOpened():
            ret, frame = cap.read()
            cap.set(cv2.CAP_PROP_POS_FRAMES, framecount)
            if not ret:
                break
            if framecount % jump == 0:
                name = name_maker(video, framecount, jump)
                cv2.imwrite(os.path.join(path, name), frame)
                framecount += jump
            elif framecount == -1:
                framecount = jump
        cap.release()
        cv2.destroyAllWindows()


def name_maker(x, frame, jump):
    """
    This function makes the names of the files of the images to prevent
    duplicates. For video footage that starts with HB as well as the videos
    that start with NVR
    :param x: String with the name of the file where the frame will be get from
    :param frame: Integer with the framenumber of the image from the video
    :return: name: String of the name the image will get
    """
    name = str

    # This if statement makes the name of the file of the image to prevent
    # duplicates
    if x[0:2] == 'HB':

        starttime = x[22:24] + '.' + x[24:26] + '.' + x[26:28]
        endtime = x[37:39] + '.' + x[39:41] + '.' + x[41:43]
        day = x[14:18] + '-' + x[18:20] + '-' + x[20:22]
        name = 'HB2_' + x[7] + '_' + day + '_' + starttime + '-' + endtime + \
               'fr' + str(frame) + '.jpg'

        hour = int(x[22:24])
        minute = int(x[24:26])
        second = int(x[26:28])
        print(hour, minute, second)
        print(frame)
        time0 = (frame - jump) / 25 / 60
        if time0 / 60 > 1:
            print('integer' + int(time0 / 60))
        time = str(hour) + '-' + str(minute) + '-' + str(int(second + time0))
        print(time)

    elif x[0:2] == 'NV':
        starttime = x[21:23] + '.' + x[23:25] + '.' + x[25:27]
        endtime = x[36:38] + '.' + x[38:40] + '.' + x[40:42]
        day = x[13:17] + '-' + x[17:19] + '-' + x[19:21]
        print(starttime, endtime, day)
        name = 'NVR_' + x[6] + '_' + day + '_' + starttime + '-' + endtime + \
               'fr' \
               + str(
            frame) + '.jpg'
    return name


if __name__ == '__main__':
    # This code can get videos from the directory of videos and can only pick
    # out the files that end with .mp4
    video_folder = os.path.join(os.getcwd())
    # video_folder = os.path.join('videos')
    video_files = [_ for _ in os.listdir(video_folder) if _.endswith('.mp4')]

    frame_maker(video_files)
