import datetime
import glob
import os.path
import np
from PIL import Image

camera_folder = os.path.abspath("E:\\Timelapse\\Arquenay\\picam1\\")
date_folders = glob.glob(camera_folder + "/*")

for date_folder in date_folders:
    splited = date_folder.split("\\")
    date = splited[-1]

    imgs_list = []
    imgs_names = []

    stacked = "E:\\Timelapse\\stacked\\" + date + ".png"

    if not os.path.isfile(stacked):

        filenames = glob.glob(date_folder + '\\*.jpg')
        filenames.sort()

        for image in filenames:
            hour = image.split("\\")[-1].split("_")[1].split("-")[0]
            if int(hour) > 12:
                imgs_list.append(Image.open(image))
                imgs_names.append(image)

        nex_date = datetime.datetime.strptime(date, '%Y-%m-%d') + datetime.timedelta(days=1)
        next_day_folder = date_folder.replace(date, nex_date.strftime('%Y-%m-%d'))

        filenames = glob.glob(next_day_folder + '\\*.jpg')
        filenames.sort()

        for image in filenames:
            hour = image.split("\\")[-1].split("_")[1].split("-")[0]
            if int(hour) < 12:
                imgs_list.append(Image.open(image))
                imgs_names.append(image)

        mean = 0
        high_max = 10

        means = {}
        for name in imgs_names:
            means[name] = np.mean(Image.open(name), axis=(0, 1, 2))

        success = False
        imgs_selected = []
        while high_max < 100 and not success:
            imgs_selected = []
            for name in imgs_names:
                if means[name] < high_max:
                    imgs_selected.append(Image.open(name))
            if len(imgs_selected) < 50:
                high_max += 2
            else:
                success = True

        if success:
            image_max = np.max(imgs_selected, axis=0).astype(np.uint8)
            image = Image.fromarray(image_max)

            image.save(stacked)

            print("Stacked {} with nb={}  max at {}".format(stacked, len(imgs_selected), high_max))

        else:
            image_med = np.median(imgs_selected, axis=0).astype(np.uint8)
            image = Image.fromarray(image_med)
            image.save(stacked)

            print("Stacked {} with all median".format(stacked, len(imgs_selected), high_max))
