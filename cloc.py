# -*- coding: utf-8 -*

import os
import subprocess


def cloc(author, since_time, until_time, *dirs, **kwargs):
    cmd = 'git log --author="%(author)s" --since="%(since_time)s" --until=' \
          '"%(until_time)s" --pretty=tformat: --numstat -- . ":(exclude)' \
          'vendor" ":(exclude)openapi-spec" ":(exclude)*/*.pb.go" ' % {
                                "author": author,
                                "since_time": since_time,
                                "until_time": until_time}
    # cmd = 'git log --author="wisererik" --since="2019-01-01" --until=' \
    #       '"2019-06-30" --pretty=tformat: --numstat -- . ":(exclude)' \
    #       'vendor" ":(exclude)openapi-spec" ":(exclude)*/*.pb.go" '
    # # cmd = 'git log --author="wisererik"'

    cmd += '| awk \'{ add += $1; subs += $2; loc += $1 - $2 } END { printf ' \
           '"%s:%s:%s", add, subs, loc }\''
    # cmd = str(cmd)
    # print(cmd)

    prefix = "/home/root1/gopath/src/github.com/opensds"
    add = 0
    subs = 0
    loc = 0
    for item in dirs:
        os.chdir(prefix)
        current_path = os.path.join(prefix, item)
        # print(current_path)
        if not os.path.isdir(current_path):
            os.system(
                "git clone https://github.com/opensds/" + item + ".git")
        os.chdir(current_path)

        try:
            f = os.popen(cmd)
            result = f.read().split(':')
            if len(result[0]) > 0:
                add += int(result[0])
            if len(result[1]) > 0:
                subs += int(result[1])
            if len(result[2]) > 0:
                loc += int(result[2])
        except Exception as e:
            raise e
        finally:
            f.close()
    msg = r"%s: 新增 %s, 删除 %s, 代码行数 %s" % (author, add, subs, loc)
    print(msg)


if __name__ == "__main__":
    cloc("wisererik", "2019-01-01", "2019-06-30", "opensds", "nbp",
         "multi-cloud", "opensds-dashboard", "opensds-installer",
         "orchestration", "anomaly-detection")
    cloc("jerry", "2019-01-01", "2019-06-30", "opensds", "nbp",
         "multi-cloud", "opensds-dashboard", "opensds-installer",
         "orchestration", "anomaly-detection")
    cloc("Shruthi-1MN", "2019-01-01", "2019-06-30", "opensds", "nbp",
         "multi-cloud", "opensds-dashboard", "opensds-installer",
         "orchestration", "anomaly-detection")
    cloc("sfzeng", "2019-01-01", "2019-06-30", "opensds", "nbp",
         "multi-cloud", "opensds-dashboard", "opensds-installer",
         "orchestration", "anomaly-detection")
    # cloc("satya-gorli", "2019-01-01", "2019-06-30", "opensds", "nbp",
    #      "multi-cloud", "opensds-dashboard", "opensds-installer",
    #      "orchestration", "anomaly-detection")
    cloc("PravinRanjan10", "2019-01-01", "2019-06-30", "opensds", "nbp",
         "multi-cloud", "opensds-dashboard", "opensds-installer",
         "orchestration", "anomaly-detection")
    cloc("nguptaopensds", "2019-01-01", "2019-06-30", "opensds", "nbp",
         "multi-cloud", "opensds-dashboard", "opensds-installer",
         "orchestration", "anomaly-detection")
    cloc("NajmudheenCT", "2019-01-01", "2019-06-30", "opensds", "nbp",
         "multi-cloud", "opensds-dashboard", "opensds-installer",
         "orchestration", "anomaly-detection")
    cloc("liuqinguestc", "2019-01-01", "2019-06-30", "opensds", "nbp",
         "multi-cloud", "opensds-dashboard", "opensds-installer",
         "orchestration", "anomaly-detection")
    cloc("leonwanghui", "2019-01-01", "2019-06-30", "opensds", "nbp",
         "multi-cloud", "opensds-dashboard", "opensds-installer",
         "orchestration", "anomaly-detection")
    cloc("kumarashit", "2019-01-01", "2019-06-30", "opensds", "nbp",
         "multi-cloud", "opensds-dashboard", "opensds-installer",
         "orchestration", "anomaly-detection")
    cloc("Joseph Vazhappilly", "2019-01-01", "2019-06-30", "opensds", "nbp",
         "multi-cloud", "opensds-dashboard", "opensds-installer",
         "orchestration", "anomaly-detection")
    cloc("jimccfun", "2019-01-01", "2019-06-30", "opensds", "nbp",
         "multi-cloud", "opensds-dashboard", "opensds-installer",
         "orchestration", "anomaly-detection")
    cloc("jackhaibo", "2019-01-01", "2019-06-30", "opensds", "nbp",
         "multi-cloud", "opensds-dashboard", "opensds-installer",
         "orchestration", "anomaly-detection")
    cloc("himanshuvar", "2019-01-01", "2019-06-30", "opensds", "nbp",
         "multi-cloud", "opensds-dashboard", "opensds-installer",
         "orchestration", "anomaly-detection", "gophercloud")
    cloc("anvithks", "2019-01-01", "2019-06-30", "opensds", "nbp",
         "multi-cloud", "opensds-dashboard", "opensds-installer",
         "orchestration", "anomaly-detection")
    cloc("rhsakarpos", "2019-01-01", "2019-06-30", "opensds", "nbp",
         "multi-cloud", "opensds-dashboard", "opensds-installer",
         "orchestration", "anomaly-detection")
