# vue-element-admin-fastapi
vue-element-admin-fastpai
  
frontend:vue-element-admin  
backend:fastapi and Full Stack FastAPI and PostgreSQL

```
root:[vue-element-admin-fastapi]
|--frontend		#vue-element-admin
|--backend
|      |--app
|      |      |--alembic	#alembic
|      |      |--app
|      |      |      |--api
|      |      |      |      |--api_v1
|      |      |      |      |      |--api.py
|      |      |      |      |      |--endpoints
|      |      |      |      |      |--report	#excel export api 敏捷开发 
|      |      |      |      |      |      |--gen_excel.py
|      |      |      |      |      |      |--gen_report.py
|      |      |      |      |      |      |--report
|      |      |      |      |      |      |--__init__.py
|      |      |      |      |      |--system
|      |      |      |      |      |--websocket	#python-socketio,异步类视图区分命名空间
|      |      |      |      |      |      |--server.py
|      |      |      |      |--deps.py
|      |      |      |--celery_app	#celery
|      |      |      |      |--celery_app.py
|      |      |      |      |--worker
|      |      |      |      |      |--example.py
|      |      |      |--core
|      |      |      |      |--config.py
|      |      |      |      |--security.py
|      |      |      |--crud
|      |      |      |--db
|      |      |      |      |--base.py
|      |      |      |      |--session.py
|      |      |      |--extensions
|      |      |      |      |--exception.py	#全局异常捕获 暂时没有使用的需要,所以没用
|      |      |      |      |--logger.py	#替代原来的日志
|      |      |      |      |--routing.py	#重写路由器  支持exclude_dependencies参数=>支持全局登陆验证剔除login端口 或者你可以通过单独挂载一个新的路由器来避免全局变量
|      |      |      |      |--utils.py		#utils 主要使用了其中的list_to_tree
|      |      |      |--initial_data.py		#初始化数据
|      |      |      |--main.py
|      |      |      |--middleware			#中间件
|      |      |      |      |--access_middle.py		#中间件 登陆日志
|      |      |      |--models		#models 	Table
|      |      |      |--schemas		#schemas	Pydantic
|      |      |      |--tests
|      |      |      |--__init__.py
|      |      |--pyproject.toml		#项目所需要的包
|      |      |--scripts
|--logs				#日志路径
|      |--backend
|      |--celery
```
#### socket.io
frontend:socket.io-client  
backend:python-socketio  
前后端版本兼容请去官网检查，我使用的已经是最新的版本  
前端：socket.io-client version 3.X  
后端：python-socketio  version 5.X  

#### celery
celery-redis  
start celery:sh backend\app\worker-start.sh   
you can use swagger : http://49.235.242.224:8080/docs  api:/utils/test-celery  try send email by celery,just post your email address

#### middleware


#### EXCEL敏捷开发
```
#前端原本使用window.location.href直接下载后端接口的excel,但是这种方法无法携带token
frontend:frontend\vue-element-admin-fastapi\frontend\src\utils\ruoyi.js   function download
		 axios发送get请求携带token,通过访问header['content-disposition']获取文件名(需要后端设置Access-Control-Expose-Headers)
backend:backend\app\app\api\api_v1\report\__init__.py
```


#### DEMO:http://49.235.242.224:9527/ 



#### 开发规则整理：  
1.模块化  
2.router.include_router下对根路由的RESTFUL请求需要结尾加"/",这个需要前端配合，其他都不需要加"/"


#### 如何快速本地启动
##### python packages
```
cd vue-element-admin-fastapi\backend\app
pip install -r requirements.txt
```
##### ip及数据库连接
```
frontend
#websocket连接的ip
vue-element-admin-fastapi\frontend\src\views\monitor\server\index.vue 
#开发环境连接的后端ip
vue-element-admin-fastapi\frontend\.env.development	
#生产环境连接的后端ip
vue-element-admin-fastapi\frontend\.env.production	

backend
#alembic的数据库连接
vue-element-admin-fastapi\backend\app\alembic\env.py
#后端的数据库连接
vue-element-admin-fastapi\backend\app\app\core\config.py
#celery的数据库连接
vue-element-admin-fastapi\backend\app\app\celery_app\celery_app.py
```
##### 数据准备
vue-element-admin-fastapi\backend\app\prestart.sh
```
#检查数据库连接
python /app/app/db_pre_start/backend_pre_start.py
#alembic初始化本地表结构
alembic revision --autogenerate -m "first commit"
alembic upgrade head
#初始化数据
python /app/app/initial_data.py
```
##### 开发环境启动
```
frontend:npm run dev
backend:python main.py
celery:见启动脚本
```


#### 联系方式:
QQ：619511821
