import os
from os.path import isfile, join
from tkinter.tix import INTEGER
from PIL import Image

class Automation:

    def __init__(self):
        self.file_extensions = ('.jpg', '.png', '.jpeg')
        self.in_directory = f"{os.path.dirname(os.path.abspath(__file__))}\\{'pre_photos'}"
        self.out_directory = f"{os.path.dirname(os.path.abspath(__file__))}\\{'post_photos'}"
        self.sprite = Image.open('Template.png') #Name of file you want to add sprites too
        self.sprite_width = self.sprite.width
        self.sprite_height = self.sprite.height
        self.sprite_columns = 3
        self.sprite_column_names = ["Left", "Middle", "Right"]
        self.sprite_rows = 4
        self.sprite_row_names = ["Down", "Left", "Right", "Up"]
        self.rpg_height = 48
        self.rpg_width = 48

    def run (self):
        pictures = self.get_files_from_in_directory()
        self.put_each_file_on_tilesheet(pictures)
        keep_going = input("Would you like to continue y/yes n/no")
        while(keep_going.__contains__('y')):
            self.put_each_file_on_tilesheet(pictures)
            keep_going = input("Would you like to continue y/yes n/no")


    def get_files_from_in_directory(self):
        onlyfiles = [f for f in os.listdir(self.in_directory) if isfile(join(self.in_directory, f))]
        return [f for f in onlyfiles if f.endswith(self.file_extensions)]

    def put_each_file_on_tilesheet(self, pictures):
        for picture in pictures:
            self.set_spritesheet(picture)
    
    def set_spritesheet(self, picture):
        spritenumber =  int(input("You have " + picture + " which sprite are you hoping to put this in (1-8): "))
        while(spritenumber < 1 and spritenumber > 8):
            spritenumber = int(input("Please enter a valid number one thats between 1-8: "))
        height = self.sprite_height
        width = self.sprite_width 

        # statement goes to bottom right of an rpg maker mv character
        if(1 == spritenumber):
            height = 4 * self.rpg_height
            width = 3 * self.rpg_width
        elif(2 == spritenumber):
            height = 4 * self.rpg_height
            width  = 6 * self.rpg_width
        elif(3 == spritenumber):
            height = 4 * self.rpg_height
            width = 9 * self.rpg_width
        elif(4 == spritenumber):
            height = 4 * self.rpg_height
        elif(5 == spritenumber):
            width = 3 * self.rpg_width
        elif(6 == spritenumber):
            width = 6 * self.rpg_width
        elif(7 == spritenumber):
            width = 9 * self.rpg_width
        elif(8 == spritenumber):
            pass

        columns = int(input("How may columns does the sprite sheet have?: "))
        while(columns < 0):
            columns = int(input("Please enter a valid number: "))

        rows = int(input("How may rows does the sprite sheet have?: "))
        while(rows < 0):
            rows = int(input("Please enter a valid number: "))

        sprite_sheet = Image.open(self.in_directory + "\\" + picture)
        sprite_sheet.convert("RGBA")

        picture_height = sprite_sheet.height
        picture_width = sprite_sheet.width
        max_paste_width = width
        max_paste_height = height
        sprite_width = picture_width / columns
        sprite_height = picture_height / rows
        current_paste_width = (max_paste_width - 2 * self.rpg_width) - self.rpg_width / 2
        current_paste_height = (max_paste_height - 3 * self.rpg_height) - self.rpg_height / 3

        for row in self.sprite_row_names:
            selected_row = int(input("Which row on the spritesheet is " + row + ": "))
            while(selected_row < 0 or selected_row > rows):
                selected_row = int(input("Please enter a valid number: "))

            sprite_location_height = (picture_height / rows) * selected_row
            if(selected_row !=0):
                for column in self.sprite_column_names:
                    sprite_number = int(input("What sprite do you want in the " + column + " Column: "))
                    while(sprite_number < 0 or sprite_number > columns):
                        sprite_number = int(input("Please enter a valid number: "))
                    if (sprite_number != 0):
                        sprite_location_width = (picture_width / columns) * sprite_number
                        sprite_location = (sprite_location_width - sprite_width, sprite_location_height - sprite_height, sprite_location_width, sprite_location_height)
                        sprite = sprite_sheet.crop(sprite_location)
                        newImage = []
                        newImage.append((255, 255, 255, 0))
                        sprite.putdata(newImage)
                        sprite_paste = (int(current_paste_width - sprite_width/2), int(current_paste_height - sprite_height/2), int(current_paste_width + sprite_width/2), int(current_paste_height + sprite_height/2))
                        self.sprite.paste(sprite, sprite_paste)
                    current_paste_width = current_paste_width + self.rpg_width
            current_paste_width = (max_paste_width - 2 * self.rpg_width) - self.rpg_width / 2
            current_paste_height = current_paste_height + self.rpg_height
        self.sprite.save(self.out_directory + "\\" + "Test.png")    



        


def main():
    automation = Automation()
    automation.run()

if __name__ == '__main__':
    main()