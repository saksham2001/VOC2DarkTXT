import xml.etree.ElementTree as ET

classes = {"car": 0, "motorcycle": 1, "autorickshaw": 2, "bus": 3, "truck": 4, "person": 5, "rider": 6,
           "traffic light": 7, "traffic sign": 8}

annot_path = 'annot_path'

xmlname = "XML Name"

tree = ET.parse(f'{xmlname}')
root = tree.getroot()

filename = root.find('filename').text.split('.')[0]
folder = root.find('folder').text
img_size = root.find('size')
width = int(img_size.find('width').text)
height = int(img_size.find('height').text)
depth = int(img_size.find('depth').text)
objects = root.findall('object')
path = annot_path + '/' + folder + '/' + f'{filename}.txt'

f = open(path, "w")

for object in objects:
    name = object.find('name').text
    bndbox = object.find('bndbox')

    xmin = int(bndbox.find('xmin').text)
    ymax = int(bndbox.find('ymax').text)
    xmax = int(bndbox.find('xmax').text)
    ymin = int(bndbox.find('ymin').text)

    x_abs = (xmin + xmax)/2
    y_abs = (ymin + ymax)/2

    obj_width_abs = xmax - xmin
    obj_height_abs = ymax - ymin

    x = x_abs/width
    y = y_abs/height

    obj_width = obj_width_abs/width
    obj_height = obj_height_abs/height

    cls = classes[name]

    data = str(cls) + ' ' + str(round(x, 4)) + ' ' + str(round(y, 4)) + ' ' + str(round(obj_width, 4)) + ' ' + str(round(obj_height, 4))

    f.write(data + '\n')

    print(cls, round(x, 4), round(y, 4), round(obj_width, 4), round(obj_height, 4))


print(filename, folder, width, height, depth)
f.close()
