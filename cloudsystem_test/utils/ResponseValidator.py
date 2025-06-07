import time
import logging

import logging

class ResponseValidator:
    @staticmethod
    def assert_status_code(response_dict, expected_code=200):
        """断言响应中的状态码字段"""
        actual_code = response_dict.get("header", {}).get("status")
        if str(actual_code) != str(expected_code):
            logging.error(f"Expected status {expected_code}, but got {actual_code}")
            raise AssertionError(f"Expected status {expected_code}, but got {actual_code}")
        logging.info(f"Status code {actual_code} matches expected {expected_code}")

    @staticmethod
    def assert_field_in_response(response_dict, field_path, *expected_values):
        """
        断言响应体中是否包含指定的字段，支持多个模糊匹配值，只要命中其中一个即通过。
        :param response_dict: API 响应（字典）
        :param field_path: 字段路径，如 'header.errMsg'
        :param expected_values: 可变参数，期望值列表，只要包含其中一个即视为通过
        """
        fields = field_path.split('.')
        current = response_dict
        for field in fields:
            if not isinstance(current, dict) or field not in current:
                raise AssertionError(f"字段 '{field_path}' 不存在于响应体中")
            current = current[field]

        if expected_values:
            current_str = str(current)
            if not any(str(val) in current_str for val in expected_values):
                raise AssertionError(
                    f"字段 '{field_path}' 的值 '{current_str}' 不包含任何期望值：{expected_values}"
                )

        logging.info(f"字段 '{field_path}' 校验通过，值为：{current}")




#调用示例
"""
ResponseValidator.assert_status_code(response, 200)  # 断言状态码为200
ResponseValidator.assert_response_time(response, 500)  # 断言响应时间不超过500ms
ResponseValidator.assert_field_in_response(response, 'data.user.id', 12345)  # 断言字段'data.user.id'的值为12345

"""