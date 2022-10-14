import re
import dl_images.regex as rg
acl = [
    'click.dtiserv2.com',
    'al.dmm.co.jp',
    'www.mgstage.com',
    'pcmax.jp',
    'asp.m-live.jp',
    'www.g-apart.com',
    'www.chatpia.jp',
    'www.angel-live.com',
    'click.duga.jp',
    'dl.getchu.com',
    'gcolle.net',
    'pcolle.jp',
    'www.hdouga.com',
    'free-avx.jp',
    'free-av-douga.com',
    'twitter.com',
    'www.po-kaki-to.com',
    'xvideo-jp.com',
    'www.sokmil.com',
    'eroanime-movie.com',
    'www.prestige-av.com',
    'www.s-cute.com',
    'www.madonna-av.com',
    'www.alicejapan.co.jp',
    'www.attackers.net',
    'graphis.ne.jp',
    'www.google.co.jp',
    'sbs.nsk-sys.com',
    'www.themediaplanets.com',
    'the-101.com',
    'otland.blog.2nt.com',
    'imgs1.a.la9.jp',
    'gold2.h-paradise.net',
    'www.tameikegoro.jp',
    'adult.contents.fc2.com',
    'pc.194964.com',
    'mintj.com',
    '550909.com',
    'www.e-nls.com',
    'news-channel.doorblog.jp',
    '2channeler.com',
    'matomeja.jp',
    'blog.livedoor.jp',
    'www.amazon.co.jp',
    'rank.i2i.jp',
    'www.i2i.jp',
    'siterank.flash-l.net',
    'idol-blog.com',
    'www.news-edge.com',
    'news-choice.net',
    'news-three-stars.net',
    'mabo02.livedoor.biz',
    'matomeantena.com',
    'antenna.i-like-movie.net',
    'vippers.jp',
    'adultportal.jp',
    'giko-antenna.com',
    '2ch-2.net',
    'matometatta-news.net',
    'afo-news.com',
    'jyouhouya3.net',
    'tyoieronews.blog.jp',
    'kita-kore.com',
    'news-select.net',
    'newsnow-2ch.com',
    'world-best-news.doorblog.jp',
    'yorozubako.blog71.fc2.com',
    'www.shock-tv.com',
    'dvdrev.blog68.fc2.com',
    'aya0205.smart-douga.mobi',
    'newpuru.doorblog.jp',
    'kimootoko.net',
    'hnalady.com',
    'track.bannerbridge.net',
    'www.hatena.ne.jp',
    'www.addtoany.com',
    'www.indies-av.co.jp',
    'www.av-event.jp',
    'www.beyourlover.co.jp',
    'docs.google.com',
    'www.dmm.co.jp',
    'cpz.to',
    'feeds.feedburner.com',
    'sukebeee.com',
    'image-eyes1.a.la9.jp',
    'live.fc2.com'
]

wl = [
    'www.bakufu.jp',
    'img.bakufu.jp',
    'bakufu.jp',
    'minkch.com',
    'imgs.minkch.com',
    'ertk.net',
    'i4.ertk.net',
    'i1.ertk.net',
    'i.imgur.com',
    'gifnuki.com',
    'img.gifnuki.com'
]

def atag(tag):
    # if tag.has_attr('href'):
    #     print("tag href : " + tag['href'])
    # else:
    #     return False
    # print(tag)
    # print(tag.name)
    if tag.name=='a' and tag.has_attr('href'):
        # print(tag)
        # print(tag['href'])
        url = tag['href']
        if rg.P_reshapeURL_a.match(url):
            # print(url)
            r = re.findall('[^/]+',url)
            # print(r[0])
            if not r[0] in wl:
                return False
        if rg.P_reshapeURL_e.match(url):
            # print('#')
            return False

        r = re.search('https?://',url) 
        if r:
            r = re.findall('[^/]+',url)
            if not r[1] in wl:
                return False
        # print(tag['href'])
        return True
    return False

def imgtag(tag):
    if tag.name=='img':
        # print(tag)
        # print(tag.attrs)
        return True
    return False