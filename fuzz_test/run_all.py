import subprocess
import os
import shutil

# 一键执行入口

RESULT_DIR = "results"
REPORT_DIR = "report"

def clear_directories():
    """清理历史测试结果"""
    if os.path.exists(RESULT_DIR):
        shutil.rmtree(RESULT_DIR)
    if os.path.exists(REPORT_DIR):
        shutil.rmtree(REPORT_DIR)

def run_tests():
    """运行pytest收集测试数据"""
    os.makedirs(RESULT_DIR, exist_ok=True)
    subprocess.run(f"pytest --alluredir={RESULT_DIR}", shell=True)

def generate_allure_report():
    """生成并打开allure报告"""
    subprocess.run(f"allure generate {RESULT_DIR} -o {REPORT_DIR} --clean", shell=True)
    subprocess.run(f"allure open {REPORT_DIR}", shell=True)

if __name__ == '__main__':
    clear_directories()
    run_tests()
    generate_allure_report()
