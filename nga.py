import requests


class NGA(object):
    """bbs.nga.cc 精英玩家俱乐部API"""

    def __init__(self):
        self.http = requests.session()

        self.http.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
            'Connection': 'keep-alive',
            'cookie': 'lastvisit=1574431448; lastpath=/; ngaPassportUid=39788792; bbsmisccookies=%7B%22uisetting%22%3A%7B0%3A%22b%22%2C1%3A1574431750%7D%2C%22pv_count_for_insad%22%3A%7B0%3A-47%2C1%3A1574442020%7D%2C%22insad_views%22%3A%7B0%3A1%2C1%3A1574442020%7D%7D; UM_distinctid=16e936c455d62-0a4a5ad31c28fd8-4c302b7a-190140-16e936c455e210; CNZZDATA30043604=cnzz_eid%3D376000271-1574428901-%26ntime%3D1574428810; taihe_bi_sdk_uid=881d113bf9055f9371134eb3b34e7179; taihe_bi_sdk_session=86d349015b7a8c31c2a5c191b1f8b2f0; weibojs_1648254866=access_token%3D2.008uYcTCu4uXnB9fca9e8566smHU5C%26remind_in%3D2609804%26expires_in%3D2609804%26uid%3D2269970067%26isRealName%3Dtrue; ngacn0comUserInfo=%25B0%25C1%25D1%25A9%25D2%25F7%25CB%25AA%25B0%25D7%25C8%25E7%25B1%25F9%09%25E5%2582%25B2%25E9%259B%25AA%25E5%2590%259F%25E9%259C%259C%25E7%2599%25BD%25E5%25A6%2582%25E5%2586%25B0%0939%0939%09%0910%095400%094%090%090%0961_4%2C39_30; ngacn0comUserInfoCheck=429ebddbfc58eeb90f4dc06b13df6bea; ngacn0comInfoCheckTime=1574431429; ngaPassportUrlencodedUname=%25B0%25C1%25D1%25A9%25D2%25F7%25CB%25AA%25B0%25D7%25C8%25E7%25B1%25F9; ngaPassportCid=X8n24634gsahhll599hksdl3291ea8u6g44cqekv'
        })

    def t_list(self, fid, recommend=0, page=1):
        """
        帖子列表
        :return:
        :param fid: 论坛板块ID {往事杂谈: -7, }
        :param recommend: 是否精华贴 {0： 否， 1： 是}
        :param page: page
        """
        return self.response('http://bbs.nga.cn/app_api.php?__lib=subject&__act=list', data={
            'fid': fid,
            'stid': '0',
            'recommend': recommend,
            'page': page,
        })

    def t_list_hot(self, fid, days=1, page=1):
        """
        热门帖子
        :param fid: 论坛id
        :param days: 热帖周期 {1, 7, 30}
        :param page: page
        :return:
        """
        return self.response('http://bbs.nga.cn/app_api.php?__lib=subject&__act=hot', data={
            'fid': fid,
            'days': days,
            'page': page,
        })

    def t_content(self, tid, page=1):
        """
        帖子内容
        :param tid: 帖子ID
        :param page: page
        :return:
        """
        return self.response('http://bbs.nga.cn/app_api.php?__lib=post&__act=list', data={
            'page': page,
            'tid': tid
        })

    def u_content(self, uid):
        """
        用户信息
        :param uid: 用户uid
        :return:
        """
        return self.response('http://bbs.nga.cn/app_api.php?__lib=user&__act=detail', data={
            'uid': uid,
            '__ngaClientChecksum': '1fe72a148a1c3ae2c5b99e32d3c6cfd01526891914',  # 作用未知 可忽略
        })

    def u_reply(self, uid, page=1):
        """
        用户回帖列列表
        :param uid: 用户uid
        :param page: page
        :return:
        """
        return self.response('http://bbs.nga.cn/app_api.php?__lib=user&__act=replys', data={
            'uid': uid,
            'page': page,
        })

    def u_post(self, uid, page=1):
        """
        用户发帖列表
        :param uid: 用户ID
        :param page: page
        :return:
        """
        return self.response('http://bbs.nga.cn/app_api.php?__lib=user&__act=subjects', data={
            'uid': uid,
            'page': page,
        })

    def u_posts(self, uid, page=1):
        """
        用户发帖列表
        :param uid: 用户ID
        :param page: page
        :return:
        """
        x = self.http.post('http://bbs.nga.cn/app_api.php?__lib=user&__act=subjects', data={
            'uid': uid,
            'page': page,
        })

        return x.json()

    def response(self, url, data={}):
        """
        响应内容
        :param url:
        :param data:
        :return: json-encoded content
        """
        return self.http.post(url, data=data).json()