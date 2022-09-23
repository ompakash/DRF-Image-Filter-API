import cv2
from django.conf import settings
import os
import qrcode

base_dir = settings.BASE_DIR

class ImgConverter:

    def __init__(self, process, data):
        self.name = data["name"]
        self.process = process
        self.image = data["before_img"]

    def gray_scale(self, img):
        new_img = img[1:]
        file_address = os.path.join(base_dir, new_img)
        after_images = file_address.replace("before_images", "after_images")
        return_address = after_images.replace(str(base_dir), "")
        return_address=return_address.replace("\\", "/")

        # logic structure
        read_img = cv2.imread(file_address, 0)

        # saving structure
        cv2.imwrite(after_images, read_img)
        return return_address

    def QRfunc(self, img):
        return f"{img}: img url"

    def text_to_qr(self,name,img):
        # gen_img = qrcode.make(name)
        # gen_img.save(filename)

        new_img = img[1:]
        file_address = os.path.join(base_dir, new_img)
        after_images = file_address.replace("before_images", "after_images")
        return_address = after_images.replace(str(base_dir), "")
        return_address=return_address.replace("\\", "/")
        
        temp_var = self.name
        temp_var1 = temp_var.replace(" ","")
        # logic structure
        gen_img = qrcode.make(self.name)
        gen_img.save(f"media/after_images/{temp_var1}.png")
        



        # saving structure
        
        return_address = f"/media/after_images/{temp_var1}.png"
        return return_address




    def callProcess(self):
        if self.process == "bnw":
            return self.gray_scale(self.image)

        elif self.process == "qr":
            return self.QRfunc(self.image)

        
        elif self.process == "ttqr":
            return self.text_to_qr(self.name , self.image)