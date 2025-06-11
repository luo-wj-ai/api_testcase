from core.rules import FieldRule

# 创建订单接口字段规则配置

URL = "https://koophone-cc.cmtest.xyz/cloudphone/order/createOrder"
HEADERS = {
    "token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxOTIxNzczOTUyNzEwMjE3NzMwIiwib3JpVG9rZW4iOiI1RTA2NEYzMUVFMTA0MDA4OUQxNEZEQzc3Qzk2QTVCOSIsInN1YklkIjoiMTkyMTc3Mzk1MjcxMDIxNzczMCIsImFjY291bnQiOiI3ZjhmYmRhZjE0MGYzMjQyZDRlMGRmMGNjYjgxOWQ1NWViY2JkMWFlODVjZjAzZjIyNWU1OTUyZjY1N2E1YWM1OTRhZDBhZmE5OTVhYWE4NDAyZmVhYiIsInRlbmFudElkIjoiODYwMSIsImV4cCI6MTc0OTc4MjYxNiwiY2xpZW50VHlwZSI6Ikg1IiwibG9naW5NZXRob2QiOiJQQVNTV09SRCJ9.T1Ami55ZWOnegbLVjQgf3vfaj2GWZH7VG13I8cXTlEIHLB6M__kh31VyZQxMf6DIA43x5awvyTuxn5l47to-fA",
    "Content-Type": "application/json"}

# 正向用例合法数据，作为所有反向用例的基准数据
VALID_DATA = {
    "memberPackageId": "32",
    "channel": "APP"
}

# 针对字段的规则配置（可扩展支持更多字段）
FIELD_RULES = [
    FieldRule(
        name="memberPackageId",
        required=True,
        data_type="string",
        custom_invalid=["INVALID_ID", ""],
        invalid_code_map={
            "missing": "500010",
            "type_error": "502001",
            "custom_INVALID_ID": "502001",
            "custom_empty": "500010"
        }
    ),
    FieldRule(
        name="channel",
        required=True,
        data_type="string",
        enum=["APP", "H5"],
        custom_invalid=["WEB", ""],
        invalid_code_map={
            "missing": "500010",
            "type_error": "630012",
            "enum_error": "630012",
            "custom_WEB": "630012",
            "custom_empty": "500010"
        }
    )
]
