import tornado.web
import tornado.ioloop
import downloadImg
import json
class Reptilian(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
    def post(self):
        url = self.get_argument('url')
        fileName = self.get_argument('fileName')
        downloadImgResult = downloadImg.downloadImg(url, fileName)
        if downloadImgResult:
            self.write('数据获取很成功')
        else:
            self.write('数据获取出现问题, 不完整 ! ')