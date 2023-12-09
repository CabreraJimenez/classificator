from dataclasses import dataclass, field

@dataclass
class ModelOptions:
    """Options for training a model.
    """
    # Model to train
    name: str

@dataclass
class OptimizerOptions:
    """Options for a torch optimizer."""
    name: str
    lr: float

@dataclass
class LossFnOptions:
    """Options for a loss function."""
    name: str

@dataclass
class DatasetOptions:
    """Options for a dataset."""
    # Dataset to use
    name: str

@dataclass
class TrainOptions:
    """Options for training a model.
    """

    # epochs to train for
    epochs: int

    # batch size
    batch_size: int

    # device to use
    device: str

    # Model to train
    model: ModelOptions = field(default_factory = ModelOptions)

    # Optimizer to use
    optimizer: OptimizerOptions = field(default_factory = OptimizerOptions)

    # Loss function to use
    loss_fn: LossFnOptions = field(default_factory = LossFnOptions)

    # Dataset to use
    dataset: DatasetOptions = field(default_factory = DatasetOptions)

    #



