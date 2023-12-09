import torch
from tqdm import tqdm
from options import TrainOptions
from utils import parse_args
from factory.model_factory.model_selector import get_model
from factory.dataset_factory.dataset_selector import get_dataset
from factory.optimizer_factory import get_optimizer
from factory.loss_fn_factory import get_loss_fn

def train_step(model: torch.nn.Module,
               data_loader: torch.utils.data.DataLoader,
               loss_fn: torch.nn.Module,
               optimizer: torch.optim.Optimizer,
               device: torch.device):
    train_loss, train_acc = 0, 0
    model.to(device)
    for batch, (X, y) in enumerate(data_loader):
        # Send data to GPU
        X, y = X.to(device), y.to(device)

        # 1. Forward pass
        y_pred = model(X)

        # 2. Calculate loss
        loss = loss_fn(y_pred, y)
        train_loss += loss

        # 3. Optimizer zero grad
        optimizer.zero_grad()

        # 4. Loss backward
        loss.backward()

        # 5. Optimizer step
        optimizer.step()

    # Calculate loss and accuracy per epoch and print out what's happening
    train_loss /= len(data_loader)
    return train_loss

### Create a training function
def train(options: TrainOptions):
    model = get_model(options.model_name)
    dataset = get_dataset(name = options.dataset_name, 
                          transforms = model.transforms)
    train_dataset = dataset.train_dataset
    #test_dataset = dataset.test

    optimizer = get_optimizer(model = model,
                              optimizer_name = options.optimizer_name,
                              lr = options.optimizer_lr)
    
    loss_fn = get_loss_fn(loss_fn_name = options.loss_fn_name)
    
    train_dataloader = torch.utils.data.DataLoader(train_dataset, batch_size = options.batch_size, shuffle = True)
    #test_dataloader = torch.utils.data.DataLoader(test_dataset, batch_size = options.batch_size, shuffle = True)
    results = {"train_loss": []}
    for epoch in tqdm(range(options.epochs)):
        train_loss = train_step(model = model,
                                data_loader = train_dataloader,
                                loss_fn = loss_fn,
                                optimizer = optimizer,
                                device = options.device)
        results["train_loss"].append(train_loss.item())
        #Fix me: Add test step
        #test_loss, test_acc = test_step(model=model,
        #                              data_loader=test_dataloader,
        #                              loss_fn=loss_fn,
        #                              device=device) 
    return results

def main():
    description = "Train a model"
    options: TrainOptions = parse_args(TrainOptions, description)
    train(options = options)


if __name__ == "__main__":
    main()