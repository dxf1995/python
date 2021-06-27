import requests
from lxml import etree
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
'Cookie': 'antipas=949g 23Fm404MZ468i6287831; uuid=119064f2-5b36-4107-f656-7d16d012e775; cityDomain=bj; user_city_id=12; ganji_uuid=4679756788575942307208; lg=1; close_finance_popup=2019-05-25; clueSourceCode=%2A%2300; sessionid=caf34b1f-d951-4441-9183-1ab571e3e905; cainfo=%7B%22ca_s%22%3A%22seo_google%22%2C%22ca_n%22%3A%22default%22%2C%22ca_i%22%3A%22-%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_a%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%22119064f2-5b36-4107-f656-7d16d012e775%22%2C%22sessionid%22%3A%22caf34b1f-d951-4441-9183-1ab571e3e905%22%7D; Hm_lvt_936a6d5df3f3d309bda39e92da3dd52f=1558755258,1558756601,1558756608; preTime=%7B%22last%22%3A1558756742%2C%22this%22%3A1558755252%2C%22pre%22%3A1558755252%7D; Hm_lpvt_936a6d5df3f3d309bda39e92da3dd52f=1558756743'
}

#获取详情页面的url
def ge_detail_urls(url):
    # 获取页面内容

    resp = requests.get(url, headers=headers)
    text = resp.content.decode('utf-8')
    # print(text)

    # 解析网页
    html = etree.HTML(text)
    ul = html.xpath('//ul[@class="carlist clearfix js-top"]')[0]
    # print(ul)
    html_li = ul.xpath('./li')
    # print(html_li)
    detail_urls = []
    for li in html_li:
        detail_url = li.xpath('./a/@href')
        detail_url = "https://www.guazi.com" + detail_url[0]
        # print(detail_url)
        detail_urls.append(detail_url)
    return  detail_urls

def main():
    url = 'https://www.guazi.com/bj/benz/'
    detail_urls = ge_detail_urls(url)
    # print(detail_urls)
    for detail_url in detail_urls:
        resp = requests.get(detail_url,headers=headers)
        text = resp.content.decode('utf-8')
        html = etree.HTML(text)
        # print(html)
        title = html.xpath('//div[@class="product-textbox"]/h2/text()')[0]
        # 剔除空格
        title = title.replace(r'/r/n','').strip()
        print(title)
        print(html.xpath('//div[@class="product-textbox"]/ul/li/span/text() '))
        # info = html.xpath('//div[@class="product-textbox"]/ul/li/span/text() ')[0]
        # print(info)
# 保存数据
if __name__ == '__main__':
    main()



