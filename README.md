# DCGAN in Tensorflow

To train a model with downloaded dataset:

    $ python main.py --dataset mnist --input_height=28 --output_height=28 --train
    $ python main.py --dataset celebA --input_height=108 --train --crop
    $ python main.py --origin out_input --dataset out_gt  --input_fname_pattern="*.png" --train
    $ python main.py --origin input --dataset input_gt  --input_fname_pattern="*.png" --input_height=128 --input_width=128 --output_height=128 --output_width=128 --batch_size=64 --train
    $ python3 main.py --origin joined_input_frame --dataset gt --input_height=256 --input_width=256 --output_height=256 --output_width=256 --train
    

To test with an existing model:

    $ python main.py --dataset mnist --input_height=28 --output_height=28
    $ python main.py --dataset celebA --input_height=108 --crop
    $ python main.py --origin test --dataset test_gt  --input_fname_pattern="*.png" --input_height=128 --input_width=128 --output_height=128 --output_height=128 --batch_size=1

Or, you can use your own dataset (without central crop) by:

    $ mkdir data/DATASET_NAME
    ... add images to data/DATASET_NAME ...
    $ python main.py --dataset DATASET_NAME --train
    $ python main.py --dataset DATASET_NAME
    $ # example
    $ python main.py --dataset=eyes --input_fname_pattern="*_cropped.png" --train

If your dataset is located in a different root directory:

    $ python main.py --dataset DATASET_NAME --data_dir DATASET_ROOT_DIR --train
    $ python main.py --dataset DATASET_NAME --data_dir DATASET_ROOT_DIR
    $ # example
    $ python main.py --dataset=eyes --data_dir ../datasets/ --input_fname_pattern="*_cropped.png" --train
    
