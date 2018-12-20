# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class RecipespiderPipeline(object):

    def process_item(self, item, spider):

        directions = item['directions']

        if directions:

            # 连接成段
            text = ""
            for dir in directions:
                text = text + dir.strip().replace('\n', '')  # 初步清洗

            # 确保词间仅有一个空格
            text = " ".join(text.split())  # 删去词间多余空格
            tmps = text.split(",")
            text = []
            for tmp in tmps:
                text.append(tmp.strip())
            text = ", ".join(text)  # 逗号与后一个词间有一空格

            # 确保句间有一个空格
            steps = text.split(".")  # 分割成句
            text = ""
            for step in steps:
                if step:
                    text = text + step.strip() + ". "

            print(text, "\n")
            item['directions'] = text.strip()

        return item
