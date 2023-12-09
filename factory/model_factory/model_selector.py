from factory.model_factory.models.effnet_models import EffnetB0
#Change the dictionary to a class that raise and exception if the model is not found
#model_selector = {'EffnetB0': EffnetB0 }
#cretae a class that raise and exception if the model is not found


model_selector = {'EffnetB0': EffnetB0 }

def get_model(model_name):
    try:
        model_class = model_selector[model_name]
    except KeyError:
        raise Exception(f"'Model {model_name} not available, models available are: {str(model_selector.keys())}")
    return model_class()

