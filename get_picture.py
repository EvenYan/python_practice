from lxml import etree
import urllib.request
import os

def handle_request(url):
    header = {
        "User-Agent":"User-Agent:Mozilla/5.0 \
        (Macintosh; U; Intel Mac OS X 10_6_8; en-us) \
        AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }

    request = urllib.request.Request(url=url, headers=header)
    return request

def download_image(image_list, name_list):
    cwd = os.path.split(os.path.realpath(__file__))[0]
    dirpath = os.path.join(cwd, "./images")
    import time
    for index, image in enumerate(image_list):
        suffix = os.path.splitext(image)[-1]
        file_name = "".join((name_list[index], suffix))
        image_name = os.path.join(dirpath, file_name)
        urllib.request.urlretrieve(image, image_name)
        print(image_name + "下载完毕")
        time.sleep(1)

def handle_data(request):
    response = urllib.request.urlopen(request)
    html = response.read()
    html_tree = etree.HTML(html)
    #print(html)
    #print(type(html_tree))
    image_url_list = html_tree.xpath("//div/a/img/@src2")
    name_list = html_tree.xpath("//div/a/img/@alt")
    print(name_list)
    
    download_image(image_url_list, name_list)
    


def main():
    start_page = int(input("请输入起始页："))
    end_page = int(input("请输入终止页："))
    base_url = "http://sc.chinaz.com/tupian/rentiyishu"
    print("开始下载图片.................")
    for i in range(start_page, end_page+1):
        if i != 1:
            url = base_url + "_" + str(i) + ".html"
        else:
            url = base_url + ".html"
        print(url)
        request = handle_request(url)
        handle_data(request)
    print("图片下载完毕.................")

if __name__ == "__main__":
    #main()
    print(os.getcwd())
    print(os.path.abspath("."))
    print(os.curdir)