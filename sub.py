import subprocess

datapath = "C:/Lab/datasets/MvTecAD"
datasets = ['screw', 'pill', 'capsule', 'carpet', 'grid', 'tile', 'wood', 'zipper', 'cable', 'toothbrush', 'transistor', 'metal_nut', 'bottle', 'hazelnut', 'leather']

dataset_flags = ['-d' + dataset for dataset in datasets]
dataset_flags_str = ' '.join(dataset_flags)

command = [
    'python', 'main.py',
    '--gpu', '0',
    '--seed', '0',
    '--log_group', 'simplenet_mvtec',
    '--log_project', 'MVTecAD_Results',
    '--results_path', 'results',
    '--run_name', 'run',
    'net',
    '-b', 'wideresnet50',
    '-le', 'layer2',
    '-le', 'layer3',
    '--pretrain_embed_dimension', '1536',
    '--target_embed_dimension', '1536',
    '--patchsize', '3',
    '--meta_epochs', '40',
    '--embedding_size', '256',
    '--gan_epochs', '10',
    '--noise_std', '0.015',
    '--dsc_hidden', '1024',
    '--dsc_layers', '2',
    '--dsc_margin', '0.5',
    '--pre_proj', '1',
    'dataset',
    '--batch_size', '8',
    '--resize', '329',
    '--imagesize', '288',
    *dataset_flags,  # 使用 * 将列表展开为单独的参数
    'mvtec',
    datapath
]

subprocess.run(command)
