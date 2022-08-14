# 图片筛选工具
## 任务说明
本次进行的是一个真实场景下的人像抠图数据集的构建，这一部分的工作是筛选出符合要求的人像图片供模型自动生成高质量的透明度遮罩
## 筛选标准
该工具的主要用途是对人像图片进行筛选，筛选的图片包含以下标准：
* 图片必须为正常图片，不能为海报、胶片状、纯黑白
* 图片须有明确的前景人物（一个或者多个），人物最好面朝相机
* 必须有清晰的人物主体（只有手或者只有部分面部、躯体都不合适），尽量不要有虚影
* 人物不能被遮挡，多人物图片最好站位分散尽量少有交叉
## 工具的使用
首先大家需将此工具下载到本地并配置flask：

    git clone git@github.com:huangfeihongthegreast123/Dataset_imagechoose.git
    cd Dataset_imagechoose
    pip install -r requirements.txt
    
之后大家需要按照后续指示将各自对应的图片文件夹下载到[static目录]下，确保浏览器能正确找到文件位置并显示

---

在该目录下运行main.py，程序将网页映射到本地的5000端口：127.0.0.1:5000
进入该本地网页后，大家在搜索框中搜索各自对应的文件夹名，即可开始进行筛选

---
筛选过程中大家依据图片对上述标准的符合程度将其分为：合适、一般、不合适三类