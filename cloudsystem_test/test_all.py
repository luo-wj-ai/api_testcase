# import subprocess
# import os
# import shutil
# import time
#
# TEST_CASES_DIR = "test_case"
# ALLURE_RESULTS_DIR = "report/reportallure"
# ALLURE_REPORT_DIR = "report/reportallures"
#
# def clean_previous_results():
#     """
#     清理之前生成的Allure报告数据和最终报告目录，以确保每次生成的报告都是全新的。
#     """
#     if os.path.exists(ALLURE_RESULTS_DIR):
#         shutil.rmtree(ALLURE_RESULTS_DIR)
#     if os.path.exists(ALLURE_REPORT_DIR):
#         shutil.rmtree(ALLURE_REPORT_DIR)
#
#     os.makedirs(ALLURE_RESULTS_DIR)
#     os.makedirs(ALLURE_REPORT_DIR)
#
# def run_tests_and_generate_report():
#     """
#     运行测试用例并生成Allure报告的主要函数。
#     """
#     # 运行pytest测试用例并生成Allure报告数据
#     # pytest_command = f"pytest {TEST_CASES_DIR} --alluredir={ALLURE_RESULTS_DIR}"
#     pytest_command = f"pytest {TEST_CASES_DIR}/test_Ausermanagement.py --alluredir={ALLURE_RESULTS_DIR}"
#     # pytest_command = f"pytest {TEST_CASES_DIR}/test_order.py::test_case1 --alluredir={ALLURE_RESULTS_DIR}"
#     subprocess.run(pytest_command, shell=True)
#
#     # 等待一段时间，确保报告数据已完全生成（可根据实际情况调整等待时间）
#     time.sleep(2)
#
#     # 使用Allure命令行工具生成最终的Allure报告
#     allure_command = f"allure generate {ALLURE_RESULTS_DIR} -o {ALLURE_REPORT_DIR}"
#     subprocess.run(allure_command, shell=True)
#
# if __name__ == '__main__':
#     clean_previous_results()
#     run_tests_and_generate_report()
#
# '''使用命令生成allure报告'''
# # --alluredir','../reportre/reportallure
# # allure generate  ../report/reportallure -o ./reporthtml/ --clean
#
# # --html=../reportre/20241128html.html


###上面都是久方法，每次只会生成一个测试报告，历史测试报告不会保存

###下面功能
# 每次运行测试都会在report目录下创建一个新的时间戳目录（如"2025年05月20日14时20分30秒123456毫秒测试报告"）
#
# 每个时间戳目录下会有reportallure（存放原始报告数据）和reportallures（存放生成的HTML报告）两个子目录
#
# 历史报告不会被覆盖，方便追溯和比较不同时间的测试结果
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
    pytest_command = f"pytest {TEST_CASES_DIR} --alluredir={allure_results_dir}"  # 运行所有测试用例
    # pytest_command = f"pytest {TEST_CASES_DIR}/test_order.py::test_case8 --alluredir={allure_results_dir}"  # 运行单个测试用例
    subprocess.run(pytest_command, shell=True)

    # 等待一段时间，确保报告数据已完全生成
    time.sleep(2)

    # 使用Allure命令行工具生成最终的Allure报告
    allure_command = f"allure generate {allure_results_dir} -o {allure_report_dir}"
    subprocess.run(allure_command, shell=True)


if __name__ == '__main__':
    run_tests_and_generate_report()