import os


class image_class:
    # 定义图像对象，name人名，id序号，score存放评分（合适2，一般1，不合适0 方便统计），src存放相对路径
    def __init__(self, name, fid, score, src):
        self.name = name
        self.id = fid
        self.score = score
        self.src = src

    def __str__(self):
        self.src = str(self.name)+'/'+str(self.id)+'.jpg'
        # self.src = str(self.name)+'/'+str(self.id)+'.png'
        return self.src


def get_img_file(file_name):
    # 根据文件夹名返回文件夹里的图片路径列表
    imagelist = []
    root = os.getcwd()
    filenames = sorted(os.listdir(os.path.join(root, 'static', file_name)))
    print(os.path.join(root, 'static', file_name))
    for filename in filenames:
        if filename.lower().endswith(('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff')):
            imagelist.append(os.path.join('static', file_name, filename).replace('\\', '/'))
    print(imagelist)
    return imagelist


def imagelist_to_attr(imagelist):
    # 从文件名列表里分离出文件夹名和图像名，赋给image对象的name和id，还未评分的图像score默认-1
    # imagelist里面的元素必须是每张图像名和上一级文件夹名，文件夹以人名命名，图像以数字命名
    img_temp = []
    for i in range(len(imagelist)):
        fname = imagelist[i].split("/")[-2]
        imgname = imagelist[i].split("/")[-1]
        fid = imgname.split(".")[0]
        img_temp.append(image_class(fname, fid, -1, imagelist[i]))

    return img_temp


def id_search(file_name, fid):
    # 根据id序号查找图片返回图片路径,页面获取路径显示
    imagelist = get_img_file(file_name)
    img_tmp = imagelist_to_attr(imagelist)
    imgfile_len = len(img_tmp)
    if int(fid) > imgfile_len:
        return imgfile_len  # 输入id号大于人物文件夹里图片数，返回图片数，在页面中alert最大输入id
    else:
        for i in range(len(img_tmp)):
            if int(img_tmp[i].id) == int(fid):
                return imagelist[i]


def get_score_fit(image_src):
    # 根据用户选择打分栏三个按钮的不同，给相应图片的score不同值
    # 合适，score记2
    fname = image_src.split("/")[-2]
    imgname = image_src.split("/")[-1]
    fid = imgname.split(".")[0]
    imagelist = get_img_file(fname)
    img_tmp = imagelist_to_attr(imagelist)
    for i in range(len(img_tmp)):
        if int(img_tmp[i].id) == int(fid):
            img_tmp[i].score = 2
    return img_tmp


def get_score_ordinary(image_src):
    # 一般，score记1
    fname = image_src.split("/")[-2]
    imgname = image_src.split("/")[-1]
    fid = imgname.split(".")[0]
    imagelist = get_img_file(fname)
    img_tmp = imagelist_to_attr(imagelist)
    for i in range(len(img_tmp)):
        if int(img_tmp[i].id) == int(fid):
            img_tmp[i].score = 1
    return img_tmp


def get_score_unfit(image_src):
    # 不合适，score记0
    fname = image_src.split("/")[-2]
    imgname = image_src.split("/")[-1]
    fid = imgname.split(".")[0]
    imagelist = get_img_file(fname)
    img_tmp = imagelist_to_attr(imagelist)
    for i in range(len(img_tmp)):
        if int(img_tmp[i].id) == int(fid):
            img_tmp[i].score = 0
    return img_tmp


def get_pre_image(image_src):
    # 用户选择上一张，如果不是第一张，根据当前图片路径返回上一张图片路径，页面获取路径显示
    image_src = image_src.replace('\\', '/')
    fname = image_src.split("/")[-2]
    imgname = image_src.split("/")[-1]
    fid = imgname.split(".")[0]
    imagelist = get_img_file(fname)
    img_tmp = imagelist_to_attr(imagelist)
    first_id = int(img_tmp[0].id)
    if int(fid) == first_id:
        return False  # 收到返回false在页面alert("当前为第一张")
    else:
        id_pre = int(fid)-1
        return id_search(fname, id_pre)


def get_next_image(image_src):
    # 用户选择下一张，如果不是最后一张，根据当前图片路径显示下一张图片
    image_src = image_src.replace('\\', '/')
    fname = image_src.split("/")[-2]
    imgname = image_src.split("/")[-1]
    fid = imgname.split(".")[0]
    imagelist = get_img_file(fname)
    img_tmp = imagelist_to_attr(imagelist)
    img_len = len(img_tmp)
    last_id = int(img_tmp[img_len-1].id)
    if int(fid) == last_id:
        return False  # 收到返回false在页面alert("当前为最后一张")
    else:
        id_next = int(fid)+1
        return id_search(fname, id_next)