from factory.dataset_factory.datasets.food101 import CustomFood101
from torchvision import transforms
#Change the dictionary to a class that raise and exception if the model is not found
#model_selector = {'EffnetB0': EffnetB0 }
#cretae a class that raise and exception if the model is not found


dataset_selector = {'Food101': CustomFood101 }

def get_dataset(name, transforms: transforms.Compose):
    try:
        dataset_class = dataset_selector[name]
    except KeyError:
        raise Exception(f"""Dataset {name} not available, available datasets are: {list(dataset_selector.keys())}""")
    return dataset_class(transforms = transforms)