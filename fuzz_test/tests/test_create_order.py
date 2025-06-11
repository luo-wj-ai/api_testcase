import pytest
import allure
from config.create_order_config import URL, HEADERS, VALID_DATA, FIELD_RULES
from core.case_generator import CaseGenerator
from core.executor import Executor

@allure.feature("创建订单接口 Fuzz 测试")
class TestCreateOrder:

    @allure.story("正向用例")
    def test_valid_case(self):
        """
        正向用例：验证正常请求返回200业务码
        """
        result = Executor.run_case(URL, HEADERS, VALID_DATA, desc="正向用例")
        allure.attach(str(result["response"]), "响应体", allure.attachment_type.JSON)
        actual_code = result["response"]["header"]["status"]
        assert actual_code == "200"

    @allure.story("反向用例")
    @pytest.mark.parametrize("case", CaseGenerator.generate_invalid_cases(FIELD_RULES, VALID_DATA))
    @pytest.mark.parametrize("repeat", range(5))  # 每个反向用例执行5次
    def test_invalid_cases(self, case, repeat):
        """
        反向用例：验证异常用例是否返回预期业务码
        """
        with allure.step(f"第 {repeat+1} 次执行: {case['desc']}"):
            result = Executor.run_case(URL, HEADERS, case["body"], desc=case["desc"])
            allure.attach(str(result["response"]), "响应体", allure.attachment_type.JSON)
            actual_code = result["response"]["header"]["status"]
            assert actual_code == case["expected_biz_code"]
