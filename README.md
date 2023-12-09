# classificator

This project aims to give a good code structure to train your own classification problem with a fast code. One of the main problems that are found when training DeepLearning models are that is difficult to have a good base to train big models. Here you would find different models architectures and datasets to play with and a basic code structure. You can take this base to train your own models and run them in parallel with more advance software that you could find in a basic pytorch course. 

First usage:
`python3 train.py --model_name EffnetB0 --dataset_name Food101 --optimizer_lr 0.01 --optimizer_name adam --loss_fn_name cross_entropy --batch_size 1 --epochs 1 --device cpu`