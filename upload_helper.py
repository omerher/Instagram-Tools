import pyautogui
import keyboard
import os
import time

class Uploader:
    def __init__(self):
        self.create_post_btn = (111, 182)
        self.instagram_feed_btn = (121, 227)
        self.caption_location = (1245, 334)
    
    def click(self, cords):
        x = cords[0]
        y = cords[1]
        pyautogui.click(x, y)
    
    def new_tab(self):
        # open new tab
        url = "https://business.facebook.com/creatorstudio?tab=instagram_content_posts&mode=instagram&collection_id=all_pages&content_table=INSTAGRAM_POSTS"
        os.startfile(url)

        # wait and then click Create Post
        time.sleep(5)
        self.click(self.create_post_btn)

        # wait and then click Instagram Feed
        time.sleep(1)
        self.click(self.instagram_feed_btn)

        # wait and then enter caption
        time.sleep(2)
        self.click(self.caption_location)
        time.sleep(0.5)
        keyboard.press_and_release('ctrl+v')
        
        # go to the bottom of the caption for easier hashtags copy
        time.sleep(0.6)
        for i in range(1):
            keyboard.press('down')

    def calculate_time(self, num):
        seconds = 5 + 11.1*num
        if seconds > 120:
            minutes = round(seconds // 60)
            seconds = round(seconds - minutes*60)
            print(f"Task will take {minutes} minutes and {seconds} seconds.")
        else:
            print(f"Task will take {seconds} seconds.")


def upload_helper(num_posts):
    uploader = Uploader()

    uploader.calculate_time(num_posts)

    time.sleep(5)

    for i in range(num_posts):
        uploader.new_tab()
        time.sleep(2)


if __name__ == "__main__":
    num_posts = int(input("How many tab to open? "))

    upload_helper(num_posts)
