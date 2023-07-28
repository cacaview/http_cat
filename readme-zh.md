# http_cats

http_cats是一个Python包，用于根据输入的HTTP响应状态代码，返回对应的猫猫图片。您可以使用http_cats轻松地将猫咪图片与不同的HTTP状态代码关联起来。

## 安装

您可以使用pip安装http_cats：

```
pip install http_cats
```

## 使用方法

```python
from http_cats import get_cat_image

# 获取HTTP响应状态码为200的猫咪图片数据
status_code = "200"
image_bytes = get_cat_image(status_code)
print("图片数据类型：", type(image_bytes))
```

## API文档

### `get_cat_image(status_code, image_format=".jpg")`

根据输入的HTTP响应状态代码和图片格式返回对应的猫咪图片数据。

参数:

- `status_code` (str): HTTP响应状态代码，如 "200"。
- `image_format` (str): 图片格式，可以是 ".jpg", ".webp", ".jxl", ".avif" 或 ".json"。默认为 ".jpg"。

返回:

- `bytes`: 图片内容的字节数据。

## 示例

### 下载并保存图片

```
from http_cats import get_cat_image, download_cat_image

status_code = "404"
image_url = get_cat_image(status_code)
save_path = "cat_image.jpg"
# 下载并保存图片到本地
download_cat_image(image_url, save_path)
```

### 使用不同格式的图片

```
from http_cats import get_cat_image

status_code = "500"
image_format = ".webp"
image_bytes = get_cat_image(status_code, image_format)
```

