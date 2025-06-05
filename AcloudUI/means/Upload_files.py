import os

import requests


#上传图片的方法
def handle_screenshot(driver):
    screenshot_path = './temp_screenshot.png'

    # 如果截图文件已存在，不再截图，直接用
    if not os.path.exists(screenshot_path):
        driver.save_screenshot(screenshot_path)

    return os.path.abspath(screenshot_path)

#上传gnz文件的方法
def create_gnz_file():
    # 定义文件名（不带后缀）
    base_filename = "test_gnz"
    txt_file = f"{base_filename}.txt"
    gnz_file = f"{base_filename}.gnz"

    # 如果.gnz文件已存在，直接返回路径
    if os.path.exists(gnz_file):
        return os.path.abspath(gnz_file)

    try:
        # 创建并写入txt文件
        with open(txt_file, 'w', encoding='utf-8') as f:
            f.write("123")

        # 重命名为.gnz文件
        os.rename(txt_file, gnz_file)

        return os.path.abspath(gnz_file)

    except Exception as e:
        # 如果出现异常，确保清理临时文件
        if os.path.exists(txt_file):
            os.remove(txt_file)
        raise Exception(f"创建文件失败: {str(e)}")

#上传apk的方法
def download_apk():
    apk_path = './test.apk'

    # 如果apk文件不存在，就返回None
    if not os.path.exists(apk_path):
        return None

    return os.path.abspath(apk_path)
