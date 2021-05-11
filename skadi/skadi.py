import glob
import cv2


def skadi_idle():
    img_array = []
    print("开始读取图片...")

    # 修改此处为自己的路径
    for filename in glob.glob(r"F:\interact" + r'\skadi l2d idle_*.png'):
        print(filename)
        img = cv2.imread(filename)
        if img is None:
            print(filename + " is error!")
            continue
        img_array.append(img)

    print("读取图片结束...")
    fps = 60
    size = (5306, 4045)

    # 修改此处为自己的路径
    out = cv2.VideoWriter('skadi_idle.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

    print("开始合成视频...")
    for i in range(len(img_array)):
        out.write(img_array[i])
    print("合成视频结束...")

    out.release()


def skadi_interact():
    img_array = []

    # 修改此处为自己的路径
    for filename in glob.glob(r"F:\interact" + r'\skadi l2d interact_*.png'):
        print(filename)
        img = cv2.imread(filename)
        if img is None:
            print(filename + " is error!")
            continue
        img_array.append(img)

    fps = 60
    size = (5306, 4045)

    # 修改此处为自己的路径
    out = cv2.VideoWriter('skadi_interact.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()


def skadi_special():
    img_array = []

    # 修改此处为自己的路径
    for filename in glob.glob(r"F:\interact" + r'\skadi l2d special_*.png'):
        print(filename)
        img = cv2.imread(filename)
        if img is None:
            print(filename + " is error!")
            continue
        img_array.append(img)

    fps = 60
    size = (5306, 4045)

    # 修改此处为自己的路径
    out = cv2.VideoWriter('skadi_special.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()


if __name__ == "__main__":
    skadi_idle()
    skadi_interact()
    skadi_special()
