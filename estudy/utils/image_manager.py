# 检查修改前后的图片是否一致
from skimage.metrics import structural_similarity as sk_cpt_ssim
import cv2


class ImageManager:
    """判断宝贝信息页面修改前后宝贝头像的相似率"""
    def compare_baby_info_baby_portrait(self):
        image_a = cv2.imread(r'E:\\study\\Fork\\estudy\\estudy\\image\\test_baby_info_baby_portrait1.jpg')
        image_b = cv2.imread(r'E:\\study\\Fork\\estudy\\estudy\\image\\test_baby_info_baby_portrait2.jpg')
        gray_a = cv2.cvtColor(image_a, cv2.COLOR_BGR2GRAY)
        gray_b = cv2.cvtColor(image_b, cv2.COLOR_BGR2GRAY)
        (score, diff) = sk_cpt_ssim(gray_a, gray_b, full=True)
        print("SSIM: {}".format(score))
        return score

    """判断宝贝信息页面修改前后宝贝头像的相似率"""
    def compare_my_page_baby_portrait(self):
        image_1 = cv2.imread(r'E:\\study\\Fork\\estudy\\estudy\\image\\test_my_page_baby_portrait1.jpg')
        image_2 = cv2.imread(r'E:\\study\\Fork\\estudy\\estudy\\image\\test_my_page_baby_portrait2.jpg')
        gray_1 = cv2.cvtColor(image_1, cv2.COLOR_BGR2GRAY)
        gray_2 = cv2.cvtColor(image_2, cv2.COLOR_BGR2GRAY)
        (score, diff) = sk_cpt_ssim(gray_1, gray_2, full=True)
        print("SSIM: {}".format(score))
        return score


"""测试函数，再实际运行过程中可以注释"""
# if __name__ == '__main__':
#     image_1 = r'E:\\study\\Fork\\test_image\\imag.jpg'
#     image_2 = r'E:\\study\\Fork\\test_image\\woniu.jpg'
#     # image_3 = 'E:\\study\\Fork\\test_image\\imag2.jpg'
#     check_image = CheckImage()
#     check_image.compare_image(image_1, image_2)
#