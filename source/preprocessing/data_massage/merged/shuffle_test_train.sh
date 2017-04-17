ISIC_images_path='/home/abaybektursun/projects/GitHub/IndependentStudy/source/data/ISIC-images/merged'
ph2_images_path='/home/abaybektursun/projects/GitHub/IndependentStudy/source/data/PH2Dataset/merged'
train_path='/home/abaybektursun/projects/GitHub/IndependentStudy/source/data/merged/train'
test_path='/home/abaybektursun/projects/GitHub/IndependentStudy/source/data/merged/test'

function move_dataset {
    data_path=$1
    ds_size=$((`ls -l $data_path| grep -v ^l | wc -l`))
    train_count=`echo print $ds_size*0.6 | python`
    train_count=$((${train_count%.*}))
    counter=0
    ls $data_path |sort -R |while read file
    do
        counter=$(($counter+1))
        if [ $counter -lt $train_count ]
        then mv $data_path/$file $train_path/
        else mv $data_path/$file $test_path/
        fi
    done
}

move_dataset $ISIC_images_path
move_dataset $ph2_images_path
