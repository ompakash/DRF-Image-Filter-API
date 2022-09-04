import cv2
from django.conf import settings
import os

base_dir = settings.BASE_DIR

class ImgConverter:

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