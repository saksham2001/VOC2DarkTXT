import os
import xml.etree.ElementTree as ET

# All the classes available in the Dataset
classes = {"car": 0, "motorcycle": 1, "autorickshaw": 2, "bus": 3, "truck": 4, "person": 5, "rider": 6,
           "traffic light": 7, "traffic sign": 8, "bicycle": 9, "train": 10, "vehicle fallback": 11,
           "animal": 12, "caravan": 13, "trailer": 14}

# Input Path of Annotations Director (XML)
vocpath = 'path/to/files'

# Output Path of Annotations Directory (txt)
outputpath = 'path/to/files'

# Get list of all directories
vocfolders = os.listdir(vocpath)

print(vocfolders)

for vocfolder in vocfolders:

    # frontFar, FronNear, etc
    folderpath = vocpath + '/' + vocfolder

    # check if it is a directory
    if os.path.isdir(folderpath):

        # create output folders
        outputfolderpath = outputpath + '/' + vocfolder
        os.mkdir(outputfolderpath)

        # subfolders
        subfolders = os.listdir(folderpath)

        print(subfolders)

        for subfolder in subfolders:

            # Subfolders like BLR-**, HYD-** etc
            subfolderpath = folderpath + '/' + subfolder

            # check if the path has directory
            if os.path.isdir(subfolderpath):

                # create output subfolders
                outputsubfolderpath = outputfolderpath + '/' + subfolder
                os.mkdir(outputsubfolderpath)

                # read name of all xml files
                xmlfiles = os.listdir(subfolderpath)

                # create annotation txt file for each xml
                for xmlfile in xmlfiles:

                    # XML file path
                    xmlpath = subfolderpath + '/' + xmlfile

                    # check if file is xml
                    if xmlpath.lower().endswith('.xml'):

                        # Parse XML Files
                        tree = ET.parse(f'{xmlpath}')
                        root = tree.getroot()

                        # get parameters for each file
                        filename = root.find('filename').text.split('.')[0]
                        folder = root.find('folder').text
                        img_size = root.find('size')
                        width = int(img_size.find('width').text)
                        height = int(img_size.find('height').text)
                        depth = int(img_size.find('depth').text)

                        # get list of all objects in the file
                        objects = root.findall('object')

                        # path of txt file
                        txtpath = outputsubfolderpath + '/' + f'{filename}.txt'

                        # create and open file
                        f = open(txtpath, "w")

                        # for each object find required attributes
                        for object in objects:
                            name = object.find('name').text
                            bndbox = object.find('bndbox')

                            xmin = int(bndbox.find('xmin').text)
                            ymax = int(bndbox.find('ymax').text)
                            xmax = int(bndbox.find('xmax').text)
                            ymin = int(bndbox.find('ymin').text)

                            x_abs = (xmin + xmax) / 2
                            y_abs = (ymin + ymax) / 2

                            obj_width_abs = xmax - xmin
                            obj_height_abs = ymax - ymin

                            x = x_abs / width
                            y = y_abs / height

                            obj_width = obj_width_abs / width
                            obj_height = obj_height_abs / height

                            cls = classes[name]

                            data = str(cls) + ' ' + str(round(x, 4)) + ' ' + str(round(y, 4)) + ' ' + str(
                                round(obj_width, 4)) + ' ' + str(round(obj_height, 4))

                            f.write(data + '\n')

                            # print(cls, round(x, 4), round(y, 4), round(obj_width, 4), round(obj_height, 4))
                            print(subfolder, xmlfile)

                        # print(filename, folder, width, height, depth)
                        f.close()
