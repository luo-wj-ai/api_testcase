import subprocess
import os
import shutil
import time

TEST_CASES_DIR = "test_case"
ALLURE_RESULTS_DIR = "report/reportallure"
ALLURE_REPORT_DIR = "report/reportallures"

def clean_previous_results():
    """
    清理之前生成的Allure报告数据和最终报告目录，以确保每次生成的报告都是全新的。
    """
    if os.path.exists(ALLURE_RESULTS_DIR):
        shutil.rmtree(ALLURE_RESULTS_DIR)
    if os.path.exists(ALLURE_REPORT_DIR):
        shutil.rmtree(ALLURE_REPORT_DIR)

    os.makedirs(ALLURE_RESULTS_DIR)
    os.makedirs(ALLURE_REPORT_DIR)

def run_tests_and_generate_report():
    """
    运行测试用例并生成Allure报告的主要函数。
    """
    # 运行pytest测试用例并生成Allure报告数据
    pytest_command = f"pytest {TEST_CASES_DIR} --alluredir={ALLURE_RESULTS_DIR}"
    # pytest_command = f"pytest {TEST_CASES_DIR}/test_Ausermanagement.py --alluredir={ALLURE_RESULTS_DIR}"
    # pytest_command = f"pytest {TEST_CASES_DIR}/test_order.py::test_case4 --alluredir={ALLURE_RESULTS_DIR}"
    subprocess.run(pytest_command, shell=True)

    # 等待一段时间，确保报告数据已完全生成（可根据实际情况调整等待时间）
    time.sleep(2)

    # 使用Allure命令行工具生成最终的Allure报告
    allure_command = f"allure generate {ALLURE_RESULTS_DIR} -o {ALLURE_REPORT_DIR}"
    subprocess.run(allure_command, shell=True)

if __name__ == '__main__':
    clean_previous_results()
    run_tests_and_generate_report()

'''使用命令生成allure报告'''
# --alluredir','../reportre/reportallure
# allure generate  ../report/reportallure -o ./reporthtml/ --clean

# --html=../reportre/20241128html.html