from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def capture_webpage_as_image(url, output_path):
    # 配置浏览器选项
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 以无头模式运行，无需显示浏览器窗口

    # 初始化浏览器
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.set_window_size(width, height)
        # 打开网页
        driver.get(url)

        # 等待页面加载（根据实际情况调整等待时间）
        driver.implicitly_wait(1)

        # 截取整个页面的屏幕截图
        driver.save_screenshot(output_path)

    finally:
        # 关闭浏览器
        driver.quit()

if __name__ == "__main__":
    url = "file:///D:/datas/%E7%A0%94%E7%A9%B6%E7%94%9F_%E6%9C%AC%E5%9C%B0/M2/ddpm-1D/gantt/%E7%94%98%E7%89%B9%E9%A1%B9%E7%9B%AE%E8%A7%84%E5%88%92%E5%99%A81.htm"  # 替换成你的HTML页面URL
    output_path = "screenshot.png"  # 保存截图的文件路径
    width = 1200  # 替换成所需的宽度
    height = 500  # 替换成所需的高度

    capture_webpage_as_image(url, output_path)






