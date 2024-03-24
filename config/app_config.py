# 这是一个数据配置模块

from pydantic import BaseModel
from typing import Union

# 日志数据
iconPath = 'http://0.0.0.0:5500/get/data'
# 日志文件名称
logName = "./log/BCI_app.log"
# 日志项目名称
logSubject = "BCI_app 日志告警"



# 服务器参数设置
httpServer = dict(uname ='0.0.0.0',
    paths = "src.api:app", #设置服务模块
    ports = 8088,
    log = 'info',
    reloade =True)

# 测试数据
class Item(BaseModel):
    name:str
    price:float
    is_offer: Union[bool,None] = None

# 终端上传数据
class appData(BaseModel):
    data:list
