from scrapy import cmdline

name = 'allrecipes'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())