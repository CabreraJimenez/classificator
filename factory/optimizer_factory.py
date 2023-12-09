import torch.optim as optim

def get_optimizer(model, optimizer_name: str, lr: float):
    """Returns an optimizer for a given model.

    Args:
        model (torch.nn.Module): Model to train.
        optimizer_name (str): Name of the optimizer to use.
        lr (float): Learning rate for the optimizer.

    Raises:
        ValueError: If the optimizer name is not supported.

    Returns:
        torch.optim.Optimizer: Optimizer for the model.
    """
    if optimizer_name == "adam":
        return optim.Adam(params=model.parameters(),
                          lr=lr)
    elif optimizer_name == "sgd":
        return optim.SGD(params=model.parameters(),
                         lr=lr)
    else:
        raise ValueError(f"Optimizer {optimizer_name} not supported.")
