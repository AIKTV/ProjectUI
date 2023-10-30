# 打开文件
懒人快速使用  
[点击跳转](#jump)
## 首先
样板例子是同目录下的[CallMainWindow.py](./CallMainWindow.py)和[fileopen.py](./fileopen.py)</br>
fileopen.py是由fileopen.ui转化的python布局文件  
CallMainWindow.py是主文件

想要看例子的直接运行[CallMainWindow.py](./CallMainWindow.py)的32行

## 其次
懒得写详细文档了，下面直接贴chatgpt和我的问答，自己看吧

### 关于CallMainWindow.py
<details>
<summary>详细内容点击展开</summary>

这是一个使用PyQt5实现的简单的文件打开应用程序。以下是代码的说明：

首先，代码导入了所需的模块和库。其中，```warnings```模块用于忽略特定类别的警告信息，```QtWidgets```模块包含了用于创建GUI的各种小部件，```fileopen```是一个自定义的UI文件，用于定义应用程序的界面。

```MainForm```类继承自```QMainWindow```类和```Ui_MainWindow```类。```Ui_MainWindow```类是由Qt Designer自动生成的UI文件的Python处理类。在```MainForm```类中，首先调用```super()```方法初始化父类，然后调用```setupUi()```方法设置应用程序的界面。接下来，通过连接```actionfileopen```信号与```open_file```槽函数，实现了打开文件的功能。

```open_file```函数是一个槽函数，当用户点击"文件打开"菜单时触发。它使用```QtWidgets.QFileDialog```对话框提供了一个文件选择器，用户可以选择要打开的文件。选定文件后，文件名和文件类型将打印输出。

在主程序的末尾，创建了```QApplication```对象和```MainForm```对象，并通过```app.exec_()```方法进入Qt的事件循环，控制应用程序的执行。

此代码可用于创建一个简单的文件打开应用程序，用户可以使用该应用程序选择并打开文本文件。

</details>
<div id="tp"></div>

### 关于__init__ __name__ __main__这样的

<details>
<summary>详细内容点击展开</summary>

我明白你的意思了。让我为你解释这些特殊的方法和变量：

1. ```__init__```: ```__init__```是Python中的一个特殊方法，也被称为构造函数。它在创建类的实例时自动调用，用于对象的初始化操作。该方法可以接受参数，并用于设置对象的初始状态。

2. ```__name__```: ```__name__```是内置变量，用于表示当前模块的名称。当模块直接被执行时，```__name__```将被设置为```__main__```，表示该模块是主模块（即顶级执行模块）。当模块作为导入的模块时，```__name__```将设置为模块的实际名称。

3. ```__main__```: ```__main__```是Python中的特殊名称，用于表示主模块。当在命令行或脚本中直接执行Python代码时，解释器将设置```__name__```为__main__```，表示执行的是主模块。主模块是程序的入口点，其中通常包含可执行代码和程序的入口函数。

在上述代码中，```if __name__ == "__main__"```是一个常见的语句，用于判断当前模块是否为主模块。它将确保下面的代码仅在当前模块被直接执行时才运行，而不是作为导入的模块时执行。

通过将主要的执行逻辑放在```if __name__ == "__main__"```的分支中，可以确保模块在被导入时不会立即执行，而只有在作为脚本直接执行时才会执行。

总之，```__init__```是一个构造函数，在创建类的实例时初始化对象；```__name__```是一个内置变量，表示当前模块的名称；```__main__```是一个特殊的标识符，用于表示主模块。
</details>

### 关于pyqt5中，创建一个关联到按钮，打开选取文件界面，并在选完之后返回文件地址和类型的详细步骤或方法
<details>
<summary>详细内容点击展开</summary>

当使用PyQt5创建与按钮关联的文件选择对话框并获取选择的文件地址和类型时，可以按照以下步骤进行：

1. 首先，创建一个按钮，并使用QPushButton类创建一个按钮对象。可以通过指定按钮的文本和父部件来设置按钮的相关属性。
```python
button = QtWidgets.QPushButton("Open File", self)
```
2. 然后，在按钮的点击事件中添加一个槽函数，用于处理用户点击按钮后的操作。
```python
def open_file_dialog():
    fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(
        self, "选取文件", "", "All Files(*);;Text Files(*.txt)")
    print("Selected File:", fileName)
    print("File Type:", fileType)
```
3. 连接按钮的点击事件信号与槽函数。这可以确保当用户点击按钮时，槽函数将被调用。
```python
button.clicked.connect(open_file_dialog)
```
4. 最后，在创建主窗口对象并显示应用程序时，需要进入Qt的事件循环。
```python
app = QtWidgets.QApplication([])
window = QtWidgets.QMainWindow()
window.setGeometry(500, 500, 300, 200)
window.setCentralWidget(button)
window.show()
app.exec_()
```
上述步骤将创建一个简单的主窗口，并在窗口中添加一个按钮。当用户点击按钮时，将弹出文件选择对话框，用户选择完文件后，文件地址和文件类型将打印输出到控制台。

你可以根据你的需求和具体的应用程序进行修改和扩展。记住，需要导入QtWidgets模块来使用相关的类和函数。
</details>
<br>

## 最后
还有什么问题自己搜吧，欢迎补充，真的懒得写文档了（

</br></br></br>
<div id="jump"></div>

#### 懒人快速上手
import部分
```python
import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from AIKTVUI import Ui_MainWindow
# AIKTVUI为ui转化出的py文件名
```
正文部分
```python
class testform(QMainWindow,Ui_MainWindow):
    # testform是自定义类名，随便改成啥，下面要再用
    def __init__(self):
        super(testform, self).__init__()
        # testform记得改
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_file)
        #pushButton是你使用的控件id，clicked()为button特有，其他的可能是triggered()或者toggle()
        # open_file是下面定义的方法名

    def open_file(self):
        #open_file随便，上面要用
        fileName,fileType=QtWidgets.QFileDialog.getOpenFileName(
            self,"Open File",os.getcwd(),'随便啥文件(*)')
        #fileName和fileType是自定义变量名，用于储存文件地址和文件类型（后缀）
        print(fileName)
        print(fileType)
        #上两行是测试用的，正式用不用写
```
测试调用
```python
if __name__=='__main__':
```
此行固定使用，详见上面 [关于__init__ __name__ __main__这样的](#tp)  
接上
```python
    app = QtWidgets.QApplication(sys.argv)
    win = testform()
    #记得改成上面的自定义类名
    win.show()
    sys.exit(app.exec_())
```
最后  
可能会出现如下报错
```
DeprecationWarning: sipPyTypeDict() is deprecated, the extension module should use sipPyTypeDictRef() instead
  class testform(QMainWindow,Ui_MainWindow):
```
添加下文忽略弃用即可解决
```python
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
```