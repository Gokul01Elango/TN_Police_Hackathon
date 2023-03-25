from PIL import Image
from PIL.ExifTags import TAGS

# path to the image
imagename = input("Enter Image Name With File Extension : ")

# read the image data using PIL
image = Image.open(imagename)

# extract basic image metadata
info_dict = {
    "Filename": image.filename,
    "Image Size": image.size,
    "Image Height": image.height,
    "Image Width": image.width,
    "Image Format": image.format,
    "Image Mode": image.mode,
    "Image is Animated": getattr(image, "is_animated", False),
    "Frames in Image": getattr(image, "n_frames", 1)
}
for label, value in info_dict.items():
    print(f"{label:25}: {value}")

# extract EXIF metadata
exifdata = image.getexif()

# map tag ID to human-readable text
tag_dict = {}
for tag_id in TAGS:
    tag_dict[TAGS[tag_id]] = tag_id

# iterate over all EXIF metadata fields
for tag, value in exifdata.items():
    # get human-readable tag name
    tag_name = tag_dict.get(tag, tag)
    # decode byte strings
    if isinstance(value, bytes):
        value = value.decode()
    # print tag name and value
    print(f"{tag_name:25}: {value}")
