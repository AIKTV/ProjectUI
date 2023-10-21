# ProjectUI

## 环境配置
默认使用Pycharm
</br></br>

### 拉取仓库
默认已经安装git
</br></br>在~~你喜欢的地方~~资源管理器合适的目录（推荐新建Projects），右键选择```git bash here```  
执行命令</br>
```
git clone https://github.com/AIKTV/ProjectUI.git
```
也可使用 [GitHub Desktop](https://desktop.github.com "这是官网页面") clone仓库
</br></br>接下来使用Pycharm打开项目

### 虚拟环境创建
接上
推荐使用conda进行环境管理
具体方法为
1. 首先打开项目
2. 不要在意可能弹出的Python解释器配置
3. 打开设置-项目-Python解释器-添加本地解释器
4. 选择conda-创建新环境-python版本3.9
5. 检查安装完成的python版本与requirements中需求是否一致
</br>使用下方终端，输入
```
python --version
```
查看python版本，如果不同，使用
```
conda install python=3.x.x
```
改变python版本

### 依赖安装
使用
```
pip install -r requirements.txt
```

安装项目所需模块

### 外部工具添加

[知乎教程](https://zhuanlan.zhihu.com/p/166086095)
注意，由于使用了conda虚拟环境，需要将**目标地址**更改为**虚拟环境**中的程序
