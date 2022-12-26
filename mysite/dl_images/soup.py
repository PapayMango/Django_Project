from textwrap import indent
import requests as req
from bs4 import BeautifulSoup as bs
import os
import re
import hashlib
import dl_images.acl as acl
import dl_images.regex as rg
import dl_images.views as vi
import sys

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
count = 0
# def dl(url,depth=0,ulist=[],hlist=[]):
def dl(url,depth=0,ulist=None,hlist=None):

    msg = ""
    image_dir_root = "./png/"
    depth_ = depth
    url_ = url
    max_depth = 5
    # a = tree()
    # a.append(url_)
    # print(a.tree)
    if ulist is None:
        list_ = tree()
    else:
        list_ = ulist
    if hlist is None:
        hlist_ = tree()
    else:
        hlist_ = hlist

    processes = 0
    progress = 0

    global count

    def imageDL(src,flag):
        try:
            # if flag and src in hlist_:
            #     return False
            if flag and not hlist_.append(src):
                return False
            r = rg.P_imageDL.search(src).group()

            name = image_dir_root + r
            r = req.get(src)
            # hlist_.append(src)
            image = r.content
            size = r.headers.get('content-length',-1)
            # print("name : " + name)
            # print("src : " + src)
            # print("size : " + str(size) + 'bytes')
            if int(size) > 100000:
                with open(name,'wb') as h:
                    h.write(image)
        except Exception as e:
            print(e)
        return True

    def atag(tag):
        if tag.name=='a' and tag.has_attr('href'):
            url = tag['href']
            # print(url)
            if rg.P_reshapeURL_a.match(url):
                # r = re.findall('[^/]+',url)
                r = rg.P_reshapeURL_g.findall(url)
                if not r[0] in acl.wl:
                    return False
                else:
                    url = rg.P_reshapeSrc_b.match(url_).group() + url
            elif rg.P_reshapeURL_e.match(url):
                return False
            elif rg.P_reshapeURL_c.match(url):
                # print('c')
                url = rg.P_reshapeURL_d.match(url_).group() + url
                # print('url : ' + url)
            # elif re.search('^https?://',url): 
            elif rg.P_reshapeURL_f.search(url): 
                # r = re.findall('[^/]+',url)
                r = rg.P_reshapeURL_g.findall(url)
                if not r[1] in acl.wl:
                    return False
            r = rg.P_reshapeURL_i.search(url) 
            if r:
                url = url[0:r.start()]
            r = re.search('\?[^/]+$',url)
            if r:
                # print('before : ' + url)
                url = url[0:r.start()]
                # print('after : ' + url)

            # if rg.P_reshapeURL_f.match(url):
            r = rg.P_reshapeURL_h.search(url)
            if r and r.group() in ['.png','.jpg','.tif','.gif','.jpeg']:
                # src_ = reshapeSrc(url)
                imageDL(url,True)
                return False
            # if not url in list_:
                # list_.append(url)
                # print('before : ' + tag['href'])
            tag['href'] = url
                # print('after : ' + tag['href'])
                # print('url in tag func : ' + url)
            if depth_ == max_depth:
                return False
            return list_.append(url)
        return False

    def imgtag(tag):
        if tag.name=='img':
            if tag.has_attr('src'):
                src = tag['src']
                if rg.P_reshapeURL_a.match(src):
                    # r = re.findall('[^/]+',src)
                    r = rg.P_reshapeURL_g.findall(src)
                    if not r[0] in acl.wl:
                        return False
                    else:
                        src = rg.P_reshapeSrc_b.match(url_).group() + src
                elif rg.P_reshapeURL_f.match(src):
                    # r = re.findall('[^/]+',src)
                    r = rg.P_reshapeURL_g.findall(src)
                    if not r[1] in acl.wl:
                        return False
                elif rg.P_reshapeSrc_c.match(src):
                    src = rg.P_reshapeSrc_d.match(url_).group() + src
                # if src in hlist_:
                    # return False
                # else:
                    # hlist_.append(src)
                tag['src'] = src
                return hlist_.append(src)
            return True
        return False


    def reshapeURL(url):
        url__ = url

        # if re.match('^//',url__):
        # if rg.P_reshapeURL_a.match(url__):
            # url__ = re.match('^https?:',url_).group() + url__
            # url__ = rg.P_reshapeSrc_b.match(url_).group() + url__
        # elif re.match('^/',url__):
        # elif rg.P_reshapeURL_c.match(url__):
            # url__ = re.match('https?://[^/]+',url_).group() + url__
            # url__ = rg.P_reshapeURL_d.match(url_).group() + url__

        # r = re.match('https?://',url__)
        # r = rg.P_reshapeURL_f.match(url__)
        # if r:
        #     # r = re.search('\.[a-z]{3,4}$',url__)
        #     r = rg.P_reshapeURL_h.search(url__)

        #     if r and r.group() in ['.png','.jpg','.tif','.gif','.jpeg']:
        #         src_ = reshapeSrc(url__)
        #         imageDL(src_)
        #         return url__,False

        # # r = re.search('#[^/]+$',url__)
        #     r = rg.P_reshapeURL_i.search(url__)
        #     if r:
        #         url__ = url__[0:r.start()]

        # else:
        #     return url__,False
        return url__,True

    def reshapeSrc(src):
        src_ = src
        # r = re.match('^//',src_) 
        if rg.P_reshapeSrc_a.match(src_) :
            # src_ = re.match('^https?:',url_).group() + src_
            src_ = rg.P_reshapeSrc_b.match(url_).group() + src_
        # if re.match('^/[^/]+',src_):
        if rg.P_reshapeSrc_c.match(src_):
            # src_ = re.match('https?://[^/]+',url_).group() + src_
            src_ = rg.P_reshapeSrc_d.match(url_).group() + src_
        return src_

    print("depth : " + str(depth_))
    # print("url : " + url_)
    # print('list tree len : ' + str(len(list_.tree)))
    # print('hlist tree len : ' + str(len(hlist_.tree)))
    print('count : ' + str(count))
    # print(list_.tree)
    # print('')
    # print('')
    # print('')
    # print(hlist_.tree)
    # print("list : " + " ".join(list_))
    # print("hlist : " + " ".join(hlist_))
    # print('hlist len : ' + str(len(hlist_)))

    # list_.append(url_)

    r = req.get(url_)
    s = bs(r.text,'lxml')
    a = s.find_all(atag)
    i = s.find_all(imgtag)

    print('a : ' + str(len(a)))
    print('i : ' + str(len(i)))
    if depth_ == 0:
        processes = len(a)
        vi.set_total(processes)
        # print('start')

    for b in i:
        try:
            if b.has_attr('data-src'):
                # print('data-src')
                src_ = reshapeSrc(b['data-src'])
            else:    
                # src_ = reshapeSrc(b['src'])
                # print(b)
                src_ = b['src']
            imageDL(src_,False)
        except Exception as e:
            print(e)
    # if depth_ < max_depth:
    for c in a:
# print("depth : " + str(depth_))
# result = reshapeURL(c['href'])
# if result[1] and depth_ < 1 and not result[0] in list_:
    # print('recursive : ' + result[0])
        count += 1
    # dl(result[0],depth_+1,list_,hlist_)
    # print(c['href'])
        try:
            dl(c['href'],depth_+1,list_,hlist_)
            if depth_ == 0:
                progress += 1
                vi.set_process(progress)
                print(' progress ' + str(progress) + ' in ' + str(processes))
        except Exception as e:
            print(e)
    # print("d")

    # print("count : " + str(count))
    # print("list length : " + str(len(list_)))
    # print("hash list : " + " ".join(hlist_))
    # count = count -1
    return True
class tree:
    def __init__(self):
        self.tree = []
    # tree = []
    def append(self,a):
        c = 1
        index = 0
        # r = re.findall('[^/]+',b)
        r = rg.P_reshapeURL_g.findall(a)
        r = r[1:len(r)]
        for a in r:
            if len(self.tree) == index:
                self.tree.append({}) 
            l = self.tree[index]
            if a in l:
                if len(r) == c:
                    return False
                if l[a] == 0:
                    l[a] = len(self.tree)
                index = l[a]
            else:
                if len(r) == c:
                    l[a] = 0
                    return True
                l[a] = len(self.tree)
                index = l[a]
            c = c + 1
        return True