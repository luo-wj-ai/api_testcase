import os

#上传图片的方法
def handle_screenshot(driver):
    screenshot_path = './temp_screenshot.png'

    # 如果截图文件已存在，不再截图，直接用
    if not os.path.exists(screenshot_path):
        driver.save_screenshot(screenshot_path)

    return os.path.abspath(screenshot_path)



#调用示例：
# privilege6 = (By.XPATH, "//input[@type='file']")
#
# # 1. 截图（自动删除旧图）并获取路径
# screenshot_path = handle_screenshot(driver)
#
# # 2. 上传截图
# driver.find_element(*privilege6).send_keys(os.path.abspath(screenshot_path))