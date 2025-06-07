import requests
import logging
import json

class RequestHandler:
    @staticmethod
    def send_request(method, url, data=None, headers=None, params=None):
        """
        发送请求方法，可以处理 GET 和 POST 请求
        :param method: 请求方式 (GET or POST)
        :param url: 请求的URL
        :param data: POST 请求的 JSON 数据 (默认为 None)
        :param headers: 请求头
        :param params: GET 请求的 URL 参数
        :return: 返回的 JSON 数据
        """
        try:
            if method.upper() == 'POST':
                res = requests.post(url, data=data, headers=headers)
            elif method.upper() == 'GET':
                res = requests.get(url, headers=headers, params=params)
            else:
                logging.error(f"Unsupported HTTP method: {method}")
                return None

            logging.info(f"Request URL: {url}, Response Status: {res.status_code}")
            res.raise_for_status()  # 如果返回状态码不是 2xx 会抛出异常
            return res.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Request error: {e}")
            return None

    @staticmethod
    def extract_field(response, field_path, default=None):
        """
        从返回的 JSON 中提取特定路径的字段值
        :param response: 响应对象
        :param field_path: 字段路径，例如 'header.errMsg' 或 'encrypt'
        :param default: 默认值，若没有找到字段则返回此值
        :return: 提取的字段值
        """
        # result = response.json()  # 直接转换成字典
        result = response
        fields = field_path.split('.')  # 根据 . 分隔字段路径

        # 遍历每个字段路径，逐级深入字典
        for field in fields:
            result = result.get(field, default)
            if result == default:  # 如果某一层字段不存在，直接返回默认值
                return default
        return result
