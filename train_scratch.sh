#!/bin/bash

python train.py \
--train-manifest "/home/GPUAdmin1/asr/german-speechdata-package-v2/train/train.csv" \
--val-manifest "/home/GPUAdmin1/asr/german-speechdata-package-v2/train/test.csv" \
--epochs 20 \
--checkpoint \
--checkpoint-per-batch 5 \
--save-folder "/home/GPUAdmin1/asr/ds_pytorch_chkpts" \
--hidden-layers 3 \
--hidden-size 700