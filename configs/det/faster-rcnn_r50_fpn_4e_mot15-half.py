USE_MMDET = True
_base_ = ['./faster-rcnn_r50_fpn_4e_mot17-half.py']
# data
data_root = 'data/MOT15/'
data = dict(
    train=dict(
        ann_file=f'{data_root}annotations/half-train_cocoformat.json',
        img_prefix=f'{data_root}train',
    ),
    val=dict(
        ann_file=f'{data_root}annotations/half-val_cocoformat.json',
        img_prefix=f'{data_root}train',
    ),
    test=dict(
        ann_file=f'{data_root}annotations/half-val_cocoformat.json',
        img_prefix=f'{data_root}train',
    ),
)
