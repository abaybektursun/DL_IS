with open('ph2Meta', 'r') as metaFile, open('caffeLabels.txt', 'w') as result:
    for a_line in metaFile:
        lineList = a_line.split('|')
        img = lineList[1].strip()
        label = lineList[3].strip()
        mb = '1' if label == '2' else 0
        result.write('{}.bmp {}\n'.format(img, mb))

#for i in `ls images/**/**/*.bmp`; do mv $i merged/; done


"""
$CAFFE_HOME/build/tools/convert_imageset \
    --resize_height=128 --resize_width=128 --shuffle  \
    /home/abaybektursun/projects/GitHub/IndependentStudy/source/data/PH2Dataset/merged/ \
    /home/abaybektursun/projects/GitHub/IndependentStudy/source/normalization/data_massage/ph2/caffeLabels.txt \
    /home/abaybektursun/projects/GitHub/IndependentStudy/source/data/test_lmdb
"""
