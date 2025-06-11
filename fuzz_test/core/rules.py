from typing import List, Optional, Dict, Any

class FieldRule:
    """
    核心字段规则类

    用于描述接口中每一个字段的取值规则，供用例生成器自动生成正反向用例。
    """

    def __init__(
        self,
        name: str,                         # 字段名
        required: bool = True,              # 是否必填
        data_type: str = "string",          # 数据类型（目前支持 string、int 等）
        length: Optional[List[int]] = None, # 长度限制（如手机号等可以指定 [11, 11]）
        enum: Optional[List[Any]] = None,   # 枚举限定值
        custom_invalid: Optional[List[Any]] = None,  # 额外自定义非法值
        invalid_code_map: Optional[Dict[str, Any]] = None,  # 每种异常场景对应的预期业务码
        enable_fuzz: bool = True            # 是否参与fuzz反向用例生成
    ):
        self.name = name
        self.required = required
        self.data_type = data_type
        self.length = length
        self.enum = enum
        self.custom_invalid = custom_invalid or []
        self.invalid_code_map = invalid_code_map or {}
        self.enable_fuzz = enable_fuzz
