# 导入requests库
import requests
# 导入文件操作库
import os
import bs4
from bs4 import BeautifulSoup
import sys
import importlib

importlib.reload(sys)

# 给请求指定一个请求头来模拟chrome浏览器
global headers
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3352.181 Safari/537.36'
    # ,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    # ,'accept-encoding': 'gzip, deflate, br','accept-language': 'zh-CN,zh;q=0.9'
    # ,'cache-control': 'max-age=0','upgrade-insecure-requests': '1'
    }
# 爬图地址
globalUrl = 'http://tarenacode:code_2013@code.tarena.com.cn/AIDCode/aid2008/'
# 定义存储位置
global save_path

path = '/home/tarena/pyPictures'

# 创建文件夹
def createFile(file_path):
    if os.path.exists(file_path) is False:
        os.makedirs(file_path)
    else:
        print("文件已存在")
    # 切换路径至上面创建的文件夹
    os.chdir(file_path)

def get(url):
    res = requests.get(url, headers=headers)
    # response = requests.get(url=url, auth=HTTPBasicAuth(user, password))
    res.encoding = 'utf-8';
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup;

def down(address ,filePath,file):
    createFile(filePath)
    r = requests.get(address, stream=True)
    f = open(filePath+file, "wb")
    for chunk in r.iter_content(chunk_size=512):
        if chunk:
            f.write(chunk)
all_list=[]
# 主方法
def main():
    # createFile(path)
    soup = get(globalUrl);
    # 获取所有类别
    allCategory = soup.find('pre').find_all('a');
    for i in range(1, len(allCategory) - 1):
        filePath = path + "/" + allCategory[i].attrs['href'];
        # createFile(filePath)
        # 根据类型打开链接
        soup1 = get(globalUrl+ allCategory[i].attrs['href']);
        # 获取页码
        # list01=[]
        for item in soup1.text.split(' '):
            # print(item[-4:])
            if len(item)>4 and (item[-4:] in (".pdf",".zip")):
                all_list.append(globalUrl+allCategory[i].attrs['href']+item.split('\r\n',1)[1])
                down(globalUrl+allCategory[i].attrs['href']+item.split('\r\n',1)[1],filePath,item.split('\r\n',1)[1])
            elif len(item)>4 :
                str01 = item.split('\r\n')
                for ite in str01:
                    if "day" in ite and ("../" not in allCategory[i].attrs['href']):
                        soup1 = get(globalUrl+allCategory[i].attrs['href']+ite);
                        filePath = path + "/" + allCategory[i].attrs['href']+ite;
                        for dayitem in soup1.text.split('  '):
                            if len(dayitem) > 4 and (dayitem[-4:] in (".pdf", ".zip")):
                                print(globalUrl + allCategory[i].attrs['href']+ite + dayitem.split('\r\n', 1)[1])
                                all_list.append(globalUrl + allCategory[i].attrs['href']+ite + dayitem.split('\r\n', 1)[1])
                                print(len(all_list))
                                down(globalUrl + allCategory[i].attrs['href']+ite + dayitem.split('\r\n', 1)[1], filePath+ite ,dayitem.split('\r\n', 1)[1])

    # print(len(all_list))
    # for item in all_list:
    #     down()
        # pars1 = soup1.find('a').text
        # # 每个类别所有页
        # allPage = int(pars1);
        # # 抓取所有页连接
        # for j in range(allPage):
        #     url2 = '';
        #     if 'gaoqing/cn' in allCategory[i].attrs['href']:
        #         url2 = allCategory[i].attrs['href'].replace("index.html", "list_1_" + str(j + 1) + ".html");
        #     if 'gaoqing/rihan' in allCategory[i].attrs['href']:
        #         url2 = allCategory[i].attrs['href'].replace("index.html", "list_2_" + str(j + 1) + ".html");
        #     if 'gaoqing/oumei' in allCategory[i].attrs['href']:
        #         url2 = allCategory[i].attrs['href'].replace("index.html", "list_3_" + str(j + 1) + ".html");
        #     soup2 = get(url2)
        #     pars2 = soup2.find_all(class_='heart nologin')
        #     # 详情连接
        #     for k1 in range(1, len(pars2)):
        #         url3 = pars2[k1].attrs['href'];
        #         path1 = url3.split('/')[-1][0:-5];
        #         createFile(filePath + '/' + path1)
        #         soup3 = get(url3)
        #         if soup3.find('div', class_='page').text != '':
        #             pars3 = soup3.find('div', class_='page').find('a').text
        #             # 打开连接详情,循环所有页
        #             for t in range(1, int(str(pars3)[1:2])):
        #                 if t == 1:
        #                     url4 = url3;
        #                 else:
        #                     url4 = url3[0:-5] + "_" + str(t) + ".html";
        #                 # 按照页开始爬取
        #                 soup4 = get(url4)
        #                 pars4 = soup4.find('div', class_='content').find_all('img')
        #                 for t1 in range(len(pars4)):
        #                     imgUrl = pars4[t1].attrs['src'];
        #                     print(imgUrl.split('/')[-1])
        #                     file_name = imgUrl.split('/')[-1]
        #                     if os.path.exists(file_name):
        #                         pass;
        #                     else:
        #                         img = requests.get(imgUrl, headers=headers)
        #                         f = open(file_name, 'ab')
        #                         f.write(img.content)
        #                         f.close()


if __name__ == '__main__':
    main()