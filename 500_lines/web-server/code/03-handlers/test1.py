# -*- coding: UTF-8 -*-
import os

# How to display a directory listing.
Listing_Page = '''\
     <html>
     <body>
     <ul>
     {0}
     </ul>
     </body>
     </html>
     '''


def list_dir(full_path):
    # os.listdir 通过listdir来获取当前目录下面的子目录，然后显示他们
    try:
        entries = os.listdir(full_path)
        bullets = ['<li>{0}</li>'.format(e) for e in entries if not e.startswith('.')]
        page = Listing_Page.format('\n'.join(bullets))
        print page
    except OSError as msg:
        msg = "'{0}' cannot be listed: {1}".format(full_path, msg)
        print msg


if __name__=='__main__':
    # 可以通过.format('\n'.join(b)) 这样的方式把列表自动拆分成每一部分
    # a=['a','b','c']
    # print(a)
    # b=['a1','b1','c1']
    # print('{}'.format('\n'.join(b)))

    list_dir('D:\\github\\web_server\\500_lines\\web-server'
             '\\code\\03-handlers\\subdir')