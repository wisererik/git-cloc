# -*- coding: utf-8 -*

import os

def cloc(author, since_time, until_time, *dirs, **kwargs):
    cmd = 'git log  --author="%(author)s" --since="%(since_time)s" --until="%(until_time)s" --pretty=tformat:  --numstat ' \
     	  '-- . ":(exclude)vendor" ":(exclude)openapi-spec" ":(exclude)*/*.pb.go" ' % {"author": author,
																					   "since_time": since_time, 
																					   "until_time": until_time}

    cmd += '| awk \'{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }\''

    print(cmd)

    prefix = os.getpwd()
    for item in dirs:
        current_path = os.path.join(prefix, item)
        if not os.path.isdir(current_path):
            os.system("git clone -b development https://github.com/opensds/" + item + ".git" )

        os.chdir(current_path)
        os.system(cmd)


if __name__ == "__main__":
    cloc("wisererik", "2019-01-01", "2019-06-30", "opensds", "nbp")
