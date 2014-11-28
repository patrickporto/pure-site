class Response(object):

    def __init__(self, content, mimetype="text/plain"):
        self.content = content
        self.headers = []
        self.headers.append(('Content-type', mimetype))

    def __str__(self):
        return self.content

    def __unicode__(self):
        return self.content
