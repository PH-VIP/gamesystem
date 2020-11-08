import oss2


def file_download():
    user_id = '01'
    path = 'http://oss-cn-guangzhou.aliyuncs.com/' + user_id + '/test-object'
    with open(r'D:\软工项目\game\ID.txt')as file:
        oss_id = file.read()
    file.close()
    with open(r'D:\软工项目\game\key.txt')as file:
        oss_key = file.read()
    file.close()
    auth = oss2.Auth(oss_id, oss_key)
    bucket = oss2.Bucket(auth, 'http://oss-cn-guangzhou.aliyuncs.com', 'jkci-test')
    bucket.get_object_to_file(path, r'D:\软工项目\game\file-test\test.txt')


def file_update():
    user_id = '01'
    path = 'http://oss-cn-guangzhou.aliyuncs.com/' + user_id + '/test-object'
    with open(r'D:\软工项目\game\ID.txt')as file:
        oss_id = file.read()
    file.close()
    with open(r'D:\软工项目\game\key.txt')as file:
        oss_key = file.read()
    file.close()
    auth = oss2.Auth(oss_id, oss_key)
    bucket = oss2.Bucket(auth, 'http://oss-cn-guangzhou.aliyuncs.com', 'jkci-test')
    bucket.put_object_from_file(path, r'D:\PythonDemo\Grade.txt')
