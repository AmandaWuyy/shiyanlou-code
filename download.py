#!/usr/bin/env python3
import requests

def download(url):
    '''
    从指定的URL中下载文件并存储到当前目录
    url：要下载页面内容的网址
    '''
    # 检查URL 是否存在
    try:
        req = requests.get(url)
    except requests.exceptions.MissingSchema:
        print('Invalid URL "{}"'.format(url))
        return
    # 检查是否成功访问了该网站
    if req.status_code == 403:
        print('you do not have the authority to access this page.')
        return
    filename = url.split('/')[-1]
    with open(filename,'w') as fobj:
        fobj.write(req.content.decode('utf-8'))
    print("Download over.")

if __name__ == '__main__':
    url = input('Enter a URL: ')
    download(url)
