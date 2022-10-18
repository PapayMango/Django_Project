import re

P_imageDL = re.compile('[^/]+.[^/.]+$')
P_reshapeURL_a = re.compile('^//')
P_reshapeURL_b = re.compile('^https?:')
P_reshapeURL_c = re.compile('^/')
P_reshapeURL_d = re.compile('https?://[^/]+')
P_reshapeURL_e = re.compile('^#')
P_reshapeURL_f = re.compile('^https?://')
P_reshapeURL_g = re.compile('[^/]+')
P_reshapeURL_h = re.compile('\.[a-z]{3,4}$')
P_reshapeURL_i = re.compile('#[^/]+$')
P_reshapeSrc_a = re.compile('^//')
P_reshapeSrc_b = re.compile('^https?:')
P_reshapeSrc_c = re.compile('^/[^/]+')
P_reshapeSrc_d = re.compile('https?://[^/]+')

print('regex loaded')

