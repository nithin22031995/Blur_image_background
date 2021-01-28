#Last login: Thu Jan 21 11:14:51 on ttys002
#(base) nithinvenkat@student-10-201-23-058 ~ % ipython
#Python 3.7.6 (default, Jan  8 2020, 13:42:34)
#Type 'copyright', 'credits' or 'license' for more information
#IPython 7.12.0 -- An enhanced Interactive Python. Type '?' for help.

import pixellib
from pixellib.tune_bg import alter_bg
#import cv2

change_bg = alter_bg()
change_bg.load_pascalvoc_model("deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")
change_bg.blur_bg("linkedIn_picture.jpeg", extreme = True, output_image_name="blur_image.jpeg")
#cv2.imwrite("img.jpg", output)
