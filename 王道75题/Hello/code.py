import web
urls = (
    '/','index'
)

class index:
    def GET(self):
        return "Hello,world!"

if_name_=="_main_":
    app = web.application(urls,globals())
    app.run()
