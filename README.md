# LiteratureView
Django website for manage literature and RSS Feed.

# Note
* Better use latest django version 2.1
* 把literature 作为一个独立的app去开发，然后做一个project的例子。参考 [packaging-your-app](https://docs.djangoproject.com/en/2.1/intro/reusable-apps/#packaging-your-app)

* 开发的时候使用sqlite作为数据库，作为示范。部署的时候再使用mysql或者其他数据库。这样开发环境更简单。

# Install the develop mode recently!
`python setup.py develop`

# index theme

不确定使用什么主题，在[bootstrap](https://startbootstrap.com/template-overviews/2-col-portfolio/)上选的这个简单的

# 前端的框架

<del>不想使用jQuery了。准备使用reactjs试一下。<del>
还是得使用jQuery,对reactjs不熟.他应该是前后端分离的框架.使用babel转化浏览器一直给警告.
尽量使用es6,尽量不适用jQuery

# 功能列表
1. 保存文献.ris文件,rss源.管理-删除,添加 form,修改,查.       对文献聚类/分类. note(todo)
2. rss订阅,拉取.rss源管理.

# url格式