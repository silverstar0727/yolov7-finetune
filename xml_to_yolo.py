import os

import xml.etree.ElementTree as ET

def get_info(ann_root):
    filename = ann_root.findtext('filename')
    assert filename is not None
    img_name = os.path.basename(filename)

    size = ann_root.find('size')
    width = float(size.findtext('width'))
    height = float(size.findtext('height'))

    objs = ann_root.findall("object")
    classes = []
    bboxes = []
    for obj in objs:
        classes.append(obj.findtext("name"))

        bbox = obj.find("bndbox")
        xmin = int(bbox.findtext("xmin"))
        ymin = int(bbox.findtext("ymin"))
        xmax = int(bbox.findtext("xmax"))
        ymax = int(bbox.findtext("ymax"))
        bboxes.append([xmin, ymin, xmax, ymax])

    image_info = {
        'file_name': filename,
        'height': height,
        'width': width,
        'classes': classes,
        'bboxes': bboxes
    }
    return image_info

def make_yolo_format(image_info):
    img_width = image_info["width"]
    img_height = image_info["height"]

    results_lines = []
    for i in range(len(image_info["classes"])):
        class_str = image_info["classes"][i]

        x1 = float(image_info["bboxes"][i][0])
        y1 = float(image_info["bboxes"][i][1])
        x2 = float(image_info["bboxes"][i][2])
        y2 = float(image_info["bboxes"][i][3])
        
        intx1 = int(x1)
        inty1 = int(y1)
        intx2 = int(x2)
        inty2 = int(y2)

        bbox_center_x = float( (x1 + (x2 - x1) / 2.0) / img_width)
        bbox_center_y = float( (y1 + (y2 - y1) / 2.0) / img_height)
        bbox_width = float((x2 - x1) / img_width)
        bbox_height = float((y2 - y1) / img_height)

        line_to_write = str(names_to_idx_dict[class_str]) + ' ' + str(bbox_center_x)+ ' ' + str(bbox_center_y)+ ' ' + str(bbox_width)+ ' ' + str(bbox_height) +'\n'
    
        results_lines.append(line_to_write)
    return results_lines

if __name__ == "__main__":
    annotations_path = "/yolov7/annotations"
    yolo_annotations_path = "/yolov7/yolo/labels"
    names_to_idx_dict = {
        "mask_weared_incorrect": 0,
        "with_mask": 1,
        "without_mask": 2
    }

    annos = os.listdir(annotations_path)
    os.makedirs(yolo_annotations_path, exist_ok=True)

    for anno_path in annos:
        ann_tree = ET.parse(os.path.join(annotations_path, anno_path))
        ann_root = ann_tree.getroot()

        img_info = get_info(ann_root)
        yolo_lines = make_yolo_format(img_info)

        with open(f"{yolo_annotations_path}/{img_info['file_name'].split('.')[0]}.txt", "w") as file:
            file.writelines(yolo_lines)