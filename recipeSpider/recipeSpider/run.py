from scrapy import cmdline

name = 'allrecipes'
cmd = 'scrapy crawl {0} --nolog'.format(name)
cmdline.execute(cmd.split())