class Framework:

    def __call__(self, environ, start_response):
        start_response('200 Ok', [('Content-Type', 'text/html')])
        return ['Answer'.encode('utf-8')]
