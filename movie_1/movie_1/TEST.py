import requests
import execjs

proxies = {
    'http': 'http://112.84.48.26:8118'
}
s = requests.Session()

data = {
                'uid_name' : "__cm_warden_uid",
                'uid_value' : "caa04fb22886152d128e718ad45e5406coo",
                'upi_name' : "__cm_warden_upi",
                'upi_value' : "MTE1LjE5NC4xODEuOA==",
                'url' : "https://www.80s.tw/movie/list/-----p/1",
                'quite_time' : "86400"
            }
ctx = execjs.compile("""
     function setCookie(cookie_name,value,cookie_time){
                var exdate=new Date();
                exdate.setTime(exdate.getTime()+(cookie_time*1000));
                a = cookie_name + "=" +escape(value)+((cookie_time==null) ? "" : "; path=/; expires="+exdate.toGMTString());
                return a
            }
""")
# c = requests.cookies.RequestsCookieJar()
#
# a = ctx.call("setCookie", data['uid_name'],data['uid_value'],data['quite_time'])
# b = ctx.call("setCookie", data['upi_name'],data['upi_value'],data['quite_time'])
# for a in a.split(';'):
#     s.cookies[a.split('=')[0]] = a.split('=')[1]
# for b in b.split(';'):
#     s.cookies[b.split('=')[0]] = b.split('=')[1]
# print(list(s.cookies))
for i in range(100):
    s.get('https://www.80s.tw/movie/list/-----p/1')
response = s.get('https://www.80s.tw/movie/list/-----p/1')
print(response.content.decode())