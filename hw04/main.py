import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self,m):
        m = int(m)
        html = '''
        <html>
        <body>
        <table>
        '''
        for i in range(1,m+1):
            html += '<TR>'
            for j in range(1,m+1):
                if j<=i:
                    html += '<TD>%d*%d=%2d </TD>' % (i,j,i*j)
                
            html += '</TR>'
         
        html += '''
        </html>
        </body>
        </table>
        '''
        self.write(html)

application = tornado.web.Application([
    (r"/([0-9]+)", MainHandler),
],debug=True)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

  
