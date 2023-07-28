# http_cats

http_cats is a Python package that allows you to get cat images based on the input HTTP response status codes. With http_cats, you can easily associate cat images with different HTTP status codes.

这里有中文版本：[readme-zh.md](readme-zh.md)
## Installation

You can install http_cats using pip:

```
pip install http-cats
```

## Usage

```python
from http_cats import get_cat_image

# Get cat image data for HTTP response status code 200
status_code = "200"
image_bytes = get_cat_image(status_code)
print("Image data type:", type(image_bytes))
```

## API Documentation

### `get_cat_image(status_code, image_format=".jpg")`

Returns the cat image data corresponding to the input HTTP response status code and image format.

Parameters:

- `status_code` (str): The HTTP response status code, e.g., "200".
- `image_format` (str): The image format, it can be ".jpg", ".webp", ".jxl", ".avif", or ".json". Default is ".jpg".

Returns:

- `bytes`: The byte data of the cat image.

## Examples

### Download and Save Image

```
from http_cats import get_cat_image, download_cat_image

status_code = "404"
image_url = get_cat_image(status_code)
save_path = "cat_image.jpg"

# Download and save the image locally
download_cat_image(image_url, save_path)
```

### Using Different Image Formats

```
from http_cats import get_cat_image

status_code = "500"
image_format = ".webp"
image_bytes = get_cat_image(status_code, image_format)
```

