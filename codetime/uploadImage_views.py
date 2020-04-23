import filetype as filetype
import hashlib

from codetime.models import UploadImage
from codetime.util import FileLogger
from codetime.views import returnBadRequest, auth, returnForbidden, returnOk
from codetimeproject import settings

__author__ = "lfs"
@auth
def uploadImage(request):
    if request.method == 'POST':
        file = request.FILES.get("img", None)
        if not file:
            return returnBadRequest("need file.")

        # 图片大小限制
        if not pIsAllowedFileSize(file.size):
            return returnForbidden("文件太大")
            # 计算文件md5
        md5 = pCalculateMd5(file)
        uploadImg = UploadImage.getImageByMd5(md5)
        if uploadImg:  # 文件已存在
            url = uploadImg.getImageUrl()
            return returnOk({'url': url, 'md5': md5})
        # 获取扩展类型 并 判断
        ext = pGetFileExtension(file)
        if not pIsAllowedImageType(ext):
            return returnForbidden("文件类型错误")

        # 检测通过 创建新的image对象
        uploadImg = UploadImage()
        userId = request.COOKIES.get('userId')
        uploadImg.filename = file.name
        uploadImg.file_size = file.size
        uploadImg.file_md5 = md5
        uploadImg.file_type = ext
        uploadImg.userId = userId

        # 保存 文件到磁盘
        with open(uploadImg.getImagePath(), "wb+") as f:
            # 分块写入
            for chunk in file.chunks():
                f.write(chunk)

        uploadImg.save()

        # 文件日志
        FileLogger.log_info("upload_image", uploadImg, FileLogger.IMAGE_HANDLER)
        url = uploadImg.getImageUrl()
        return returnOk({'url': url, 'md5': md5})


# 检测文件类型
def pGetFileExtension(file):
    rawData = bytearray()
    for c in file.chunks():
        rawData += c
    try:
        ext = filetype.guess_extension(rawData)
        return ext
    except Exception as e:
        # todo log
        return None

# 文件大小限制
def pIsAllowedFileSize(size):
    limit = settings.IMAGE_SIZE_LIMIT
    if size < limit:
        return True
    return False

# 计算文件的md5
def pCalculateMd5(file):
    md5Obj = hashlib.md5()
    for chunk in file.chunks():
        md5Obj.update(chunk)
    return md5Obj.hexdigest()

# 文件类型过滤
def pIsAllowedImageType(ext):
    if ext in ["png", "jpeg", "jpg"]:
        return True
    return False
