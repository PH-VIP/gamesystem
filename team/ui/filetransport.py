import oss2


def file_download():
    auth = oss2.Auth('LTAI4G6ZoHDeuGAhKfUqp27x', 'VncuDVuUn7jFs6TFMYogNysXmnwb2T')
    bucket = oss2.Bucket(auth, 'http://oss-cn-guangzhou.aliyuncs.com', 'jkci-test')
    bucket.get_object_to_file('http://oss-cn-guangzhou.aliyuncs.com/test-object', r'D:\软工项目\game\file-test\test.txt')

def file_update():
    auth = oss2.Auth('LTAI4G6ZoHDeuGAhKfUqp27x', 'VncuDVuUn7jFs6TFMYogNysXmnwb2T')
    bucket = oss2.Bucket(auth, 'http://oss-cn-guangzhou.aliyuncs.com', 'jkci-test')
    bucket.put_object_from_file('http://oss-cn-guangzhou.aliyuncs.com/test-object', r'D:\PythonDemo\Grade.txt')