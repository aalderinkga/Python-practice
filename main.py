"""
Created on Fri Aug 29 00:00:00 2020

@author: aalderink
"""

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from skimage.filters import try_all_threshold
from skimage.filters import threshold_yen
import os, glob


### Functions

# source : https://scikit-image.org/docs/0.13.x/auto_examples/xx_applications/plot_thresholding.html

def try_thresholds(image):
    fig, ax = try_all_threshold(image, figsize=(10, 8), verbose=False)
    plt.show()

def yen_thresh(image):
    thresh = threshold_yen(image)
    binary = image > thresh
    fig, ax = plt.subplots(2, 2, figsize=(10, 10))

    ax[0, 0].imshow(image, cmap=plt.cm.gray)
    ax[0, 0].set_title('Original')

    ax[0, 1].hist(image.ravel(), bins=256)
    ax[0, 1].set_title('Histogram')

    ax[1, 0].imshow(binary, cmap=plt.cm.gray)
    ax[1, 0].set_title('Thresholded (min)')

    ax[1, 1].hist(image.ravel(), bins=256)
    ax[1, 1].axvline(thresh, color='r')

    for a in ax[:, 0]:
        a.axis('off')
    plt.show()

def get_image_list(input_folder, string_filter='', mode_filter='include'):

    flist = glob.glob(os.path.join(input_folder,'*.tif'))
    if string_filter:
        if mode_filter=='include':
            flist = [f for f in flist if string_filter in f]
        elif mode_filter=='exclude':
            flist = [f for f in flist if string_filter not in f]
    flist.sort()

    return flist


### Script


### check current working directory
print("The current working directory is: " + os.getcwd())

### assign parent_folder
image_folder = os.path.join(
    '','..','..',
    'PycharmProjects',
    'raw_data'
    )

### compute parent folder as absolute path
image_folder = os.path.abspath(image_folder)
print("Found the image folder: " + image_folder)

flist_in = get_image_list(image_folder)
flist_in.sort()

for i in flist_in:
    image = mpimg.imread(i)
    binary_image = yen_thresh(image)

    ### save binary image in binary folder
    parent, filename = os.path.split(i)
    filename, file_extension = os.path.splitext(filename)
    new_name = os.path.join(
        parent,
        'result_binary',
        filename + '_binary' + file_extension
        )
    plt.imsave(filename, binary_image)

print("Images are done!")




# Notes: add progress bar