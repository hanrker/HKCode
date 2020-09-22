print("开始测试")
API = "http://api.gapit.cn:8013"
import requests,json
# user_info = '{"name" : "南湖", "gender" : {"a":1,"b":4}, "age": 28}' #注意：此时里面必须都是双引号，否则会报错
# user_dict_2 = json.loads(user_info)
# print(user_dict_2['gender']['a'])


# params = json.dumps({
#     'account':'GP', 
#     'password':'961cb6eb034ac826fe5e642b695961ed'
# }) 
header = {}
def login(url):
    params ={
        'account':'GP', 
        'password':'961cb6eb034ac826fe5e642b695961ed'
    }

    r = requests.get(url+"/user/login/1000?",params)

    j = json.loads(json.dumps(r.json())) 
    token = j['data']['token']

    auth = 'basicAuth'+' '+str(token)
    # print(auth)
    global header 
    header  = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'Authorization':auth,
            'Host':'api.gapit.cn:8013',
            'Origin':'http://sys.gapit.cn:8012',
            'Referer':'http://sys.gapit.cn:8012/depot/index.html',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
        }

def CreatProject(url):
    login(url)
    # print(header)
    newProjectPara = {
        'name':'H11',
        'projectNo':'H2',
        'beginDate':'1592582400000',
        'level':-1
    }
    # newProjectPara = json.dumps(newProjectPara)
    # print(newProjectPara) 
    newProjectRequest = requests.post(url+"/project/new/1000",data=newProjectPara ,headers=header)
    print(newProjectRequest.json())

def GetProject(url):
    login(url)
    print(header)
    requireProjectPara = {
    'skip': 0,
    'take': 10,
    'filed': 0,
    }
    requireProject = requests.get(url + "/project/require/1000?",params= requireProjectPara,headers=header)
    # print(requireProject.url)
    print(requireProject.json())
    return requireProject.json()
# CreatProject(API)

def Pallet(url):
    login(url)

