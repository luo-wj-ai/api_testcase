# cloudsystem_test/common/assert_utils.py

def assert_response_time(res, max_ms=400):
    """
    断言响应时间不超过指定毫秒数
    :param res: requests 响应对象
    :param max_ms: 最大响应时间，单位为毫秒
    """
    response_time_ms = res.elapsed.total_seconds() * 1000
    assert response_time_ms <= max_ms, f"响应时间不在{max_ms}ms范围内，实际响应时间: {response_time_ms:.2f}ms"
