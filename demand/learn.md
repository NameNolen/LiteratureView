#### 定义template的位置
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'dj_literature/templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

#### 在普通html里使用react.js时需要引入的\<script/>标签
```
<script src="https://cdnjs.cloudflare.com/ajax/libs/react/16.6.3/umd/react.production.min.js"/>
<script src="https://cdnjs.cloudflare.com/ajax/libs/react-dom/16.6.3/umd/react-dom.production.min.js"/>
<script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/6.26.0/babel.min.js"/>
```

#### rest-ful django api
引入 `pip install djangorestframework` 依赖包.
<del>测试 `pip install httpie` 包</del>.测试使用的ide自带的工具

#### 交互式shell
`python manage.py shell` 进入命令.`manage.py`是相对路径

#### conda环境失效
添加conda的环境变量到path中

#### conda 查看环境
`conda info --envs`
#### 进入conda环境
`` 进入conda环境
#### conda 复制环境
`conda create -n dj --clone base`

