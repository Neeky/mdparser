#!/usr/bin/env python3

"""
从指定的 md 文件中读取内容，然后转码成 html 并输出 stdout
"""

import os
import re
import logging
import markdown
import argparse

from mdparser import messages


def parser_args():
    """
    """
    # 取得文件名
    name, *_ = os.path.basename(__file__).split('.')

    # 创建转换器
    parser = argparse.ArgumentParser(name)

    # 添加参数
    parser.add_argument('mdfile', help="markdown file path")
    return parser.parse_args()


def main():
    """
    """
    # 参数处理
    args = parser_args()
    mdfile = args.mdfile

    if not os.path.isfile(mdfile):

        # 打印文件不存在的错误信息 并退出
        logging.error(messages.FILE_NOT_EXISTS.format(mdfile))
        return

    # 如果可以执行到这里说明，说明指定的文件存在

    try:

        # 读取 md 文件中的内容
        with open(mdfile) as f:
            mdtext = f.read()

        # 转码
        html_template = """
                <html>
                <head>
                    <title>index.html</title>
                </head>

                <body>
                    {0}
                </body>

                < / html > """
        # 转码并格式化
        html = html_template.format(
            markdown.markdown(mdtext, extensions=['tables', 'toc', 'fenced_code']))
        #
        print(html)
    except Exception as err:
        logging.error(messages.UNHANDLED_EXCEPTION.format(err))


if __name__ == "__main__":
    main()
