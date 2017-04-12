import pickle
import json
import glob

with open( "imageIdClassMap.pkl", "rb" ) as imageIdClassMap, open( "idNameMap", "r" ) as idNameMap, open('caffeLabels.txt', 'w') as result:
    idnm = json.load(idNameMap)
    labels_source = pickle.load(imageIdClassMap)
    for a_filename in glob.iglob('../../../data/ISIC-images/**/*.jpg', recursive=True):
        name = a_filename.split('/')[-1].split('.')[0]
        _id = list(filter(lambda img: img['name'] == name, idnm))[0]['_id']
        mb = '0' if labels_source[_id] == 'benign' else '1'
        result.write(a_filename.split('/')[-1] +' '+ mb+'\n')

# all the images are moved to one folder: /home/abaybektursun/projects/GitHub/IndependentStudy/source/data/ISIC-images/merged
"""
for i in `ls ./**/*.jpg`; do mv $i merged/; done
"""


"""
$CAFFE_HOME/build/tools/convert_imageset \
    --resize_height=128 --resize_width=128 --shuffle  \
    /home/abaybektursun/projects/GitHub/IndependentStudy/source/data/ISIC-images/merged/ \
    /home/abaybektursun/projects/GitHub/IndependentStudy/source/normalization/data_massage/isic/caffeLabels.txt \
    /home/abaybektursun/projects/GitHub/IndependentStudy/source/data/train_lmdb
"""
