#!/usr/bin/env sh

TOOLS=$CAFFE_HOME/build/tools

$TOOLS/caffe train \
  --solver=cifar10_quick_solver.prototxt

# reduce learning rate by factor of 10 after 8 epochs
$TOOLS/caffe train \
  --solver=cifar10_quick_solver_lr1.prototxt \
  --snapshot=cifar10_quick_iter_4000.solverstate.h5
