import getpass
import os
values={
        "SNO":1
        }
def get_user():
    return getpass.getuser()
def curr_pid():
    return os.getpid()
def check_who():
    cmd="zgrep sshd /var/log/auth.log* | grep rhost | sed -re 's/.*rhost=([^ ]+).*/\\1/' | sort -u"
    who=os.popen(cmd).read()[:-1]
    return who

def login_details():
    values["user"]=str(get_user())
    values["ip_address"]=str(check_who())
    values["pid"]=str(curr_pid())
    #print (values)
    return values
