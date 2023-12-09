from torch import nn

loss_functions = {
    "cross_entropy": nn.CrossEntropyLoss(),
    "mse": nn.MSELoss()
}

def get_loss_fn(loss_fn_name: str):
    """Returns a loss function for a given name.

    Args:
        loss_fn_name (str): Name of the loss function to use.

    Raises:
        ValueError: If the loss function name is not supported.

    Returns:
        torch.nn.Module: Loss function.
    """
    try:
        return loss_functions[loss_fn_name]
    except KeyError:
        raise ValueError(f"Loss function {loss_fn_name} not supported. available are: {list(loss_functions.keys())}")