options = {}

# global setup settings, and checkpoints
options['dataset'] = 'multi_pie'
options['dataset_root'] = '/esat/ruchba/xjia/image_generation/multi_pie/'
options['checkpoint_output_directory'] = '/esat/tiger/xjia/image_generation/multipie_illum/'
options['fappend'] = 'illum_aligned_60_color_stage2'
options['checkpoint_stage1'] = 'model_checkpoint_multi_pie_16-05-04-20-46_andromeda.esat.kuleuven.be_illum_aligned_60_color_onebranch_epoch199_train_434.350.p'


options['pose_code_size'] = 20
options['nbatch'] = 100
options['filter_size'] = (5,5) 

# optimization parameters
options['learning_rate'] = 1e-6 
options['beta1'] = 0.5
options['beta2'] = 0.999
options['epsilon'] = 1e-8
options['solver'] = 'sgd'

# training parameters
options['max_epochs'] = 200
options['niter_decay'] = 100
options['period'] = 10 
options['shuffle'] = True
options['verbose'] = 1
options['start_epoch'] = 0 # start from pretrained model 

options['debug_flag']=False # debug-True, run-False
