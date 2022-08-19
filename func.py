import os

class image_class:
    # 定义图像对象，name人名，id序号，score存放评分（合适2，一般1，不合适0 方便统计），src存放相对路径
    def __init__(self, name, fid, index, score, src):
        self.name = name
        self.id = fid
        self.index = index
        self.score = score
        self.src = src

def get_img_file(file_name):
    # 根据文件夹名返回文件夹里的图片路径列表
    imagelist = []
    root = os.getcwd()
    filenames = sorted(os.listdir(os.path.join(root, 'static', file_name, 'image')))
    for filename in filenames:
        if filename.lower().endswith(('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff')):
            imagelist.append(os.path.join('static', file_name, 'image', filename).replace('\\', '/'))
    return imagelist


def imagelist_to_attr(imagelist):
    # 从文件名列表里分离出人名和图像序号，赋给image对象的name和id，还未评分的图像score默认-1
    # imagelist里面的元素必须是每张图像名和上一级文件夹名，文件夹以人名命名，图像以数字命名
    img_temp = []
    for i in range(len(imagelist)):
        fname = imagelist[i].split("/")[-2]
        imgname = imagelist[i].split("/")[-1]
        fid = imgname.split(".")[0]
        index = str(i+1)
        img_temp.append(image_class(fname, fid, index, -1, imagelist[i]))

    return img_temp


def id_search(file_name, id):
    # 根据id序号查找图片返回图片路径,页面获取路径显示
    imagelist = get_img_file(file_name)
    img_tmp = imagelist_to_attr(imagelist)
    imgfile_len = len(img_tmp)
    if int(id) > imgfile_len:
        return imgfile_len  # 输入id号大于人物文件夹里图片数，返回图片数，在页面中alert最大输入id
    else:
        for i in range(len(img_tmp)):
            if int(img_tmp[i].index) == int(id):
                return img_tmp[i]


def get_score_fit(image_src):
    # 根据用户选择打分栏三个按钮的不同，给相应图片的score不同值
    # 合适，score记2
    image_src = image_src.replace('\\', '/')
    fname = image_src.split("/")[-3]
    imagelist = get_img_file(fname)
    img_tmp = imagelist_to_attr(imagelist)
    fid = match_class(image_src, img_tmp)
    for i in range(len(img_tmp)):
        if int(img_tmp[i].id) == int(fid):
            img_tmp[i].score = 2
    return img_tmp


def get_score_ordinary(image_src):
    # 一般，score记1
    image_src = image_src.replace('\\', '/')
    fname = image_src.split("/")[-3]
    imagelist = get_img_file(fname)
    img_tmp = imagelist_to_attr(imagelist)
    fid = match_class(image_src, img_tmp)
    for i in range(len(img_tmp)):
        if int(img_tmp[i].id) == int(fid):
            img_tmp[i].score = 1
    return img_tmp


def get_score_unfit(image_src):
    # 不合适，score记0
    image_src = image_src.replace('\\', '/')
    fname = image_src.split("/")[-3]
    imagelist = get_img_file(fname)
    img_tmp = imagelist_to_attr(imagelist)
    fid = match_class(image_src, img_tmp)
    for i in range(len(img_tmp)):
        if int(img_tmp[i].id) == int(fid):
            img_tmp[i].score = 0
    return img_tmp


def get_pre_image(image_src):
    # 用户选择上一张，如果不是第一张，根据当前图片路径返回上一张图片路径，页面获取路径显示
    image_src = image_src.replace('\\', '/')
    fname = image_src.split("/")[-3]
    imagelist = get_img_file(fname)
    img_tmp = imagelist_to_attr(imagelist)
    fid = match_class(image_src, img_tmp)
    first_id = int(img_tmp[0].index)
    if int(fid) == first_id:
        return False  # 收到返回false在页面alert("当前为第一张")
    else:
        id_pre = int(fid)-1
        return id_search(fname, id_pre)


def get_next_image(image_src):
    # 用户选择下一张，如果不是最后一张，根据当前图片路径显示下一张图片
    image_src = image_src.replace('\\', '/')
    fname = image_src.split("/")[-3]
    imagelist = get_img_file(fname)
    img_tmp = imagelist_to_attr(imagelist)
    fid = match_class(image_src, img_tmp)
    img_len = len(img_tmp)
    last_id = int(img_tmp[img_len-1].index)
    if int(fid) == last_id:
        return False  # 收到返回false在页面alert("当前为最后一张")
    else:
        id_next = int(fid)+1
        return id_search(fname, id_next)

def match_class(image_src, imagelist):
    for image in  imagelist:
        image_s = image.src
        if image_src in image_s:
            return image.index