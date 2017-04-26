#!/usr/bin/env sh

TOOLS=$CAFFE_HOME/build/tools

time $TOOLS/caffe train \
  --solver=cifar_full_solver.prototxt
  --log_dir=/home/abaybektursun/IS/source/network/logs

# reduce learning rate by factor of 10
#$TOOLS/caffe train \
#  --solver=cifar_full_solver_lr1.prototxt \
#  --snapshot=cifar_full_iter_60000.solverstate.h5

# reduce learning rate again by factor of 10
#$TOOLS/caffe train \
#  --solver=cifar_full_solver_lr2.prototxt \
#  --snapshot=cifar_full_iter_65000.solverstate.h5

