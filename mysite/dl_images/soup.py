import requests as req
from bs4 import BeautifulSoup as bs
import os
import re
import hashlib
import dl_images.acl as acl
import dl_images.regex as rg

count = 0
def dl(url,depth=0,ulist=[],hlist=[]):

    msg = ""
    image_dir_root = "./png/"
    depth_ = depth
    url_ = url

    list_ = ulist
    hlist_ = hlist

    processes = 0
    progress = 0
    global count 

    def imageDL(src):
        try:

            r = rg.P_imageDL.search(src).group()

            name = image_dir_root + r
            r = req.get(src)
            image = r.content
            size = r.headers.get('content-length',-1)
            print("name : " + name)
            print("src : " + src)
            print("size : " + str(size) + 'bytes')
            if int(size) > 100000:
                hash = hashlib.sha256(image)
                if hash in hlist_:
                    print("hash : " + hash.hexdigest())
                    return False
                else:
                    hlist_.append(hash)
                    with open(name,'wb') as h:
                        h.write(image)
        except Exception as e:
            print(e)
            # pass
        return True

    def reshapeURL(url):
        url__ = url
        # print("url : " + url__)
        # r = re.match('https?://[^/]+',url__)
        # if re.match('^//',url__):
        if rg.P_reshapeURL_a.match(url__):
            # url__ = re.match('^https?:',url_).group() + url__
            url__ = rg.P_reshapeSrc_b.match(url_).group() + url__
            # print("url__ // : " + url__)
        # elif re.match('^/',url__):
        elif rg.P_reshapeURL_c.match(url__):
            # url__ = re.match('https?://[^/]+',url_).group() + url__
            url__ = rg.P_reshapeURL_d.match(url_).group() + url__
            # print("url__ : " + url__)
        # elif re.match('^#',url__):
        # elif rg.P_reshapeURL_e.match(url__):
            # raise ValueError('e')
            # return url__,False

        # r = re.match('https?://',url__)
        r = rg.P_reshapeURL_f.match(url__)
        if r:
            # r = re.findall('[^/]+',url__)
            # r = rg.P_reshapeURL_g.findall(url__)
            # print(r[1])

            # if not r[1] in acl.wl:
                # raise ValueError('a')
                # return url__,False
            # r = re.search('\.[a-z]{3,4}$',url__)
            r = rg.P_reshapeURL_h.search(url__)

            if r and r.group() in ['.png','.jpg','.tif','.gif','.jpeg']:
                src_ = reshapeSrc(url__)
                # imageDL(src_)
                return url__,False
                    
                # url__ = url_ + url__
                # print('url__ : ' + url__)
        # print(r.group())
        # if r.group() in cl:
            # print("url_ : " + url__)
        # r = re.search('#[^/]+$',url__)
            r = rg.P_reshapeURL_i.search(url__)
            if r:
                # print('start : ' + str(r.start()))
                url__ = url__[0:r.start()]
                # print(url__)
        else:
            return url__,False
        return url__,True

    def reshapeSrc(src):
        src_ = src
        # print("src__ : " + src_)
        # r = re.match('^//',src_) 
        if rg.P_reshapeSrc_a.match(src_) :
            # src_ = re.match('^https?:',url_).group() + src_
            src_ = rg.P_reshapeSrc_b.match(url_).group() + src_
            # print("src__ : " + src_)
        # if re.match('^/[^/]+',src_):
        if rg.P_reshapeSrc_c.match(src_):
            # src_ = re.match('https?://[^/]+',url_).group() + src_
            src_ = rg.P_reshapeSrc_d.match(url_).group() + src_
            # print("src__ : " + src_)
        return src_

    # print("depth : " + str(depth_))
    # print("url : " + url_)
    # print("list : " + " ".join(list_))
    # print("hlist : " + " ".join(hlist_))

    list_.append(url_)

    r = req.get(url_)
    s = bs(r.text,'lxml')
    a = s.find_all(acl.atag)
    # i = s.find_all('img')
    i = s.find_all(acl.imgtag)

    # print('a : ' + str(len(a)))
    # print('i : ' + str(len(i)))
    if depth_ == 0:
        processes = len(a)
        print('start')

    for b in i:
        if b.has_attr('data-src'):
            print('data-src')
            src_ = reshapeSrc(b['data-src'])
        else:    
            src_ = reshapeSrc(b['src'])
        # imageDL(src_)
    for c in a:
        print("depth : " + str(depth_))
        result = reshapeURL(c['href'])
        if result[1] and depth_ < 1 and not result[0] in list_:
            # print('recursive : ' + result[0])
            count += 1
            dl(result[0],depth_+1,list_,hlist_)
        if depth_ == 0:
            progress += 1
            print(' progress ' + str(progress) + ' in ' + str(processes))

    # print("d")

    # print("count : " + str(count))
    # print("list length : " + str(len(list_)))
    # print("hash list : " + " ".join(hlist_))

    return True
