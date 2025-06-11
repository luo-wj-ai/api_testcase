import requests
import time

class Executor:
    """
    用例执行器：封装请求发送逻辑、耗时计算、异常捕获
    """

    @staticmethod
    def run_case(url, headers, body, desc):
        """
        执行单条测试用例
        :param url: 接口地址
        :param headers: 请求头
        :param body: 请求体 (dict 格式)
        :param desc: 用例描述
        :return: 包含 response/耗时/status 的标准化字典
        """
        start = time.time()
        try:
            response = requests.post(url, json=body, headers=headers, timeout=10)
            duration = int((time.time() - start) * 1000)
            json_resp = response.json()
            print(f"{desc} => {json_resp}")
            return {
                "response": json_resp,
                "status_code": response.status_code,
                "duration": duration
            }
        except Exception as e:
            # 捕获请求异常，保证不会中断测试流程
            return {
                "response": {"header": {"status": "EXCEPTION", "errMsg": str(e)}},
                "status_code": None,
                "duration": None
            }
