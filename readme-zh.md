# httpcats-and-httpdog

![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

`httpcats-and-httpdog` 是一个用于获取 HTTP 响应状态码对应图片的 Python 包。它可以让您根据 HTTP 响应状态代码获取来自 [httpcats](https://httpcats.com) 或 [httpdog](https://http.dog) 的图片数据。

## 安装

您可以通过 `pip` 安装 `httpcats-and-httpdog` 包：

```
pip install httpcats-and-httpdog
```

## 使用方法

```python
from httpcats_and_httpdog import get_image

# 获取 httpcats 的图片数据
status_code = "200"
image_bytes = get_image("httpcats", status_code)

# 获取 httpdog 的图片数据
status_code = "200"
image_bytes = get_image("httpdog", status_code)
```

`get_image` 函数接收三个参数：服务名称 (`httpcats` 或 `httpdog`)、HTTP 响应状态代码和图片格式（可选，默认为 `.jpg`）。它将返回相应图片数据的字节数据，您可以根据需要进一步处理或保存图片数据。

## 错误处理

在调用 `get_image` 函数时，如果输入的状态代码不是三位数字或下载图片失败，将会引发 `ValueError`。请确保输入正确的状态代码，并检查网络连接是否正常。
