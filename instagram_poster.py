import time
import os
import shutil
import subprocess
import random
import json

'''
Moves new downloaded file from Instagram into the appropriate folder and copies caption to clipboard
'''


def instagram_poster(niche):
    downloads = ""  # enter path to downloads folder (replace \ with /). For example: downloads = "C:/Users/User/Downloads"

    # enter the niche and folder name of the account. For example: .../Instagram/instagramusername/...,
    # you would have accounts_dict = {"Cars": "PicsOfSportCars", "Luxury": "WealthyMasters"} 
    accounts_dict = {"NICHE": "FOLDERNAME"}  
    account = accounts_dict[niche]

    # enter the path to the folder that you configured previously. For example: account_path = f"C:/Users/User/Documents/Instagram/{account}" 
    account_path = f"PATH_TO_FOLDER_HERE/{account}" 

    # runs for 30 minutes (288 x 5 seconds)
    for i in range(288):
        # iterates through all the files in downloads
        for filename in os.listdir(downloads):
            path = os.path.join(downloads, filename)
            # gets the file time
            file_time = round(os.path.getmtime(path))

            current_time = time.time()
            # if file was created in the last 5 minutes
            if current_time - file_time <= 300:
                # if the file is an instagram download and a video, move to videos folder
                if filename.endswith("_n.mp4"):
                    new_path = os.path.join(account_path+ "/2_Videos", filename)
                    shutil.move(path, new_path)
                # if the file is an Instagram download and a picture, move to pictures folder
                if filename.endswith("_n.jpg"):
                    new_path = os.path.join(account_path + "/1_Pictures", filename)
                    shutil.move(path, new_path)
                time.sleep(0.5)
                # create the caption - see comment at line 50
                # caption(account)

        time.sleep(5)


# removed as it is complicated to setup, if you want to set it up on your own uncomment line 45
def get_hashtags(acc):
    path = os.path.join("Instagram", f"{acc}_hashtags.json")
    tiers = ["bottom", "middle", "top"]
    num_hashtags = {"NICHE":
                        {"bottom": 18, "middle": 5, "top": 0},
                    "NICHE2":
                        {"bottom": 5, "middle": 5, "top": 10}
                    }

    hashtag_str = ""

    # opens the file and gets all the hashtags
    with open(path, "r") as f:
        json_f = json.load(f)
        for tier in tiers:
            hashtags = json_f[tier].replace("#", "").split()  # gets the hashtags from tier and converts to list
            scoped_hashtags = []
            while len(scoped_hashtags) <= num_hashtags[acc][tier]:  # gets number of hashtags for each tier for the acc
                choice = random.choice(hashtags)
                if choice not in scoped_hashtags:
                    scoped_hashtags.append(choice)
            hashtag_str += " #" + " #".join(scoped_hashtags)

        return hashtag_str


def caption(acc):
    # gets hashtags from file and removes duplicates

    hashtags = get_hashtags(acc)

    subprocess.run(['clip.exe'], input=str_caption.encode('utf-16'), check=True)


if __name__ == "__main__":
    instagram_poster()