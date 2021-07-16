## Pascal VOC XML to YOLO Darknet TXT Annotations Converter

### YOLO Darknet TXT Annotations Format
#### `<object-class> <x> <y> <width> <height>`

Where:

`<object-class>` - integer number of object from 0 to (classes-1)

`<x>` `<y>` `<width>` `<height>` - float values relative to width and height of image, it can be equal from (0.0 to 1.0)

For example: `<x> = <absolute_x> / <image_width>` or `<height> = <absolute_height> / <image_height>`

Attention: `<x>` `<y>` - are center of rectangle (are not top-left corner)

For example for img1.jpg you will be created img1.txt containing:

```
1 0.716797 0.395833 0.216406 0.147222
0 0.687109 0.379167 0.255469 0.158333
1 0.420312 0.395833 0.140625 0.166667
```

### VOC XML Format

```
<annotation>
	<folder></folder>
	<filename>000001.jpg</filename>
	<size>
		<width>500</width>
		<height>375</height>
		<depth>3</depth>
	</size>
	<object>
		<name>helmet</name>
		<bndbox>
			<xmin>112</xmin>
			<xmax>135</xmax>
			<ymin>145</ymin>
			<ymax>175</ymax>
		</bndbox>
	</object>
	...
</annotation>
```

### Requirements
* Python 3.xx

### How to Use?
* python3 app.py