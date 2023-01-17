from PIL import Image
import piexif

# Open the image file
image = Image.open("image.jpg")

# Extract EXIF data as a dictionary
exif_data = piexif.load(image.info["exif"])

# Extract GPS information (if present)
if piexif.GPSIFD in exif_data:
    gps_info = exif_data[piexif.GPSIFD]
    latitude = gps_info.get(piexif.GPSIFD.GPSLatitude)
    longitude = gps_info.get(piexif.GPSIFD.GPSLongitude)
    print("Latitude:", latitude)
    print("Longitude:", longitude)
else:
    print("GPS information not found in image.")

# Extract other information (if present)
if piexif.ExifIFD.DateTimeOriginal in exif_data["Exif"]:
    date_taken = exif_data["Exif"][piexif.ExifIFD.DateTimeOriginal]
    print("Date Taken:", date_taken)
else:
    print("Date Taken not found in image.")
