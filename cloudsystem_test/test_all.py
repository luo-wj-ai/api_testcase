"""
每次运行测试都会在report目录下创建一个新的时间戳目录（如"2025年05月20日14时20分30秒123456毫秒测试报告"）

每个时间戳目录下会有reportallure（存放原始报告数据）和reportallures（存放生成的HTML报告）两个子目录

历史报告不会被覆盖，方便追溯和比较不同时间的测试结果
"""
import subprocess
import os
import shutil
import time
from datetime import datetime

TEST_CASES_DIR = "test_case"
BASE_REPORT_DIR = "report"


def get_current_time_dir():
    """
    获取当前时间格式化的目录名，格式为：年-月-日-时-分-秒-毫秒
    """
    now = datetime.now()
    return now.strftime("%Y年%m月%d日%H时%M分%S秒%f毫秒测试报告")


def setup_report_directories():
    """
    设置报告目录结构，创建以当前时间命名的目录和子目录
    返回包含Allure结果目录和报告目录的元组
    """
    # 创建基础report目录（如果不存在）
    if not os.path.exists(BASE_REPORT_DIR):
        os.makedirs(BASE_REPORT_DIR)

    # 创建以当前时间命名的目录
    time_dir = get_current_time_dir()
    current_report_dir = os.path.join(BASE_REPORT_DIR, time_dir)
    os.makedirs(current_report_dir, exist_ok=True)

    # 创建Allure结果和报告目录
    allure_results_dir = os.path.join(current_report_dir, "reportallure")
    allure_report_dir = os.path.join(current_report_dir, "reportallures")

    # 清理可能存在的旧目录
    if os.path.exists(allure_results_dir):
        shutil.rmtree(allure_results_dir)
    if os.path.exists(allure_report_dir):
        shutil.rmtree(allure_report_dir)

    os.makedirs(allure_results_dir)
    os.makedirs(allure_report_dir)

    return allure_results_dir, allure_report_dir


def run_tests_and_generate_report():
    """
    运行测试用例并生成Allure报告的主要函数
    """
    # 设置报告目录并获取路径
    allure_results_dir, allure_report_dir = setup_report_directories()

    # 运行pytest测试用例并生成Allure报告数据
    # pytest_command = f"pytest {TEST_CASES_DIR}/test_order.py --alluredir={allure_results_dir}"
    # pytest_command = f"pytest {TEST_CASES_DIR} --alluredir={allure_results_dir}"  # 运行所有测试用例
    pytest_command = f"pytest {TEST_CASES_DIR}/api_testcase/test_ai_assistant.py --alluredir={allure_results_dir}"  # 运行单个测试用例
    subprocess.run(pytest_command, shell=True)

    # 等待一段时间，确保报告数据已完全生成
    time.sleep(2)

    # 使用Allure命令行工具生成最终的Allure报告
    """
    allure_command = f"allure generate {allure_results_dir} -o {allure_report_dir}"
    subprocess.run(allure_command, shell=True)
    """


if __name__ == '__main__':
    run_tests_and_generate_report()