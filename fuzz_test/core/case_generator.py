import copy
from core.rules import FieldRule

class CaseGenerator:
    """
    核心用例生成器：
    按照字段规则，自动生成反向用例，输出具体异常描述、异常数据体、预期业务码
    """

    @staticmethod
    def generate_invalid_cases(field_rules: list, valid_data: dict):
        """
        遍历字段规则，生成反向用例列表
        """
        cases = []

        for field in field_rules:
            if not field.enable_fuzz:
                continue  # 跳过不参与 fuzz 的字段

            # 1. 缺失字段场景
            if field.required:
                data = copy.deepcopy(valid_data)
                data.pop(field.name, None)
                code = field.invalid_code_map.get("missing", "400")
                cases.append({
                    "desc": f"{field.name} 缺失",
                    "body": data,
                    "expected_biz_code": code
                })

            # 2. 类型错误场景
            data = copy.deepcopy(valid_data)
            # 模拟类型错误：故意反类型
            data[field.name] = 12345 if field.data_type == "string" else "INVALID"
            code = field.invalid_code_map.get("type_error", "400")
            cases.append({
                "desc": f"{field.name} 类型错误",
                "body": data,
                "expected_biz_code": code
            })

            # 3. 非法枚举值场景
            if field.enum:
                data = copy.deepcopy(valid_data)
                data[field.name] = "INVALID_ENUM"
                code = field.invalid_code_map.get("enum_error", "400")
                cases.append({
                    "desc": f"{field.name} 非法枚举",
                    "body": data,
                    "expected_biz_code": code
                })

            # 4. 自定义非法值场景
            for invalid_value in field.custom_invalid:
                data = copy.deepcopy(valid_data)
                data[field.name] = invalid_value
                key = f"custom_{invalid_value}" if invalid_value != "" else "custom_empty"
                code = field.invalid_code_map.get(key, "400")
                cases.append({
                    "desc": f"{field.name} 自定义非法值 {invalid_value}",
                    "body": data,
                    "expected_biz_code": code
                })

        return cases
