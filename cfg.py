{
    "root_train": "/mnt/mfs/yiling/data/coco2017/images",
    "root_eval": "/mnt/mfs/yiling/data/coco2017/images",
    "list_train": "data/coco_train2017.txt",
    "list_eval": "data/coco_val2017.txt",
    "name_file": "data/coco_name.txt",

    "load": false,
    "save": true,
    "pretrain": true,
    "freeze_bn": true,
    "freeze_stages": 1,
    "epoches": 24,

    "nbatch_train": 16,
    "nbatch_eval": 16,
    "device": [1,2,3,5,6,7,8,9],
    "num_workers": 16,
    
    "lr_base": 0.01,
    "lr_gamma": 0.1,
    "lr_schedule": [120000, 160000],
    "momentum": 0.9,
    "weight_decay": 0.0001,
    "warmup_iter": 500,

    "boxarea_th": 32,
    "grad_clip": 3,
    
    "img_scale_min": 0.8,
    "augmentation": false,
    "seed": 0
}