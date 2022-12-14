class PostRequests:
    @staticmethod
    def get_data_from_POST_query(env):
        content_length_data = env.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0
        data = env['wsgi.input'].read(content_length) \
            if content_length > 0 else b''
        return data.decode(encoding='utf-8')
