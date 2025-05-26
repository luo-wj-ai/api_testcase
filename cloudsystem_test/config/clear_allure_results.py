import os
import shutil

'''清楚报告旧数据'''
def clear_allure_results_dir(results_dir):
    if os.path.exists(results_dir):
        try:
            shutil.rmtree(results_dir)
            print(f"已清除 {results_dir} 目录下的旧数据")
        except Exception as e:
            print(f"清除数据时出错: {e}")
    else:
        print(f"{results_dir} 目录不存在，无需清理")
    return
#     results_dir = "../report/reportallure"
#     clear_allure_results_dir(results_dir)
