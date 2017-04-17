#!/usr/bin/env sh

DATA=/home/abaybektursun/projects/GitHub/IndependentStudy/source/data
DBTYPE=lmdb

echo "Computing image mean..."

$CAFFE_HOME/build/tools/compute_image_mean -backend=$DBTYPE \
  $DATA/train_$DBTYPE $DATA/mean.binaryproto

echo "Done."
