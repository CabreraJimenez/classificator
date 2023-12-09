import argparse
import torch
from typing import Type
from dataclasses import is_dataclass

def set_seeds(seed: int=42):
  """Sets random seeds for torch operations.

  Args:
    seed (int, optional): Random seed to set. Defaults to 42.
  """
  #Set the seed for general torch operations
  torch.manual_seed(seed)
  torch.cuda.manual_seed(seed)

def set_device():
  """Sets the device to cuda if available, otherwise cpu.
  """
  device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
  return device

import argparse
from dataclasses import dataclass, fields

def parse_args(dclass: Type[dataclass], description: str) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=description)
    for field in fields(dclass):
        if is_dataclass(field.type):
            for nested_field in fields(field.type):
                arg_name = f"{field.name}_{nested_field.name}"
                if nested_field.default is not None:
                    parser.add_argument(f"--{arg_name}", default=nested_field.default, type=nested_field.type, help=f"{arg_name} (default: {nested_field.default})")
                else:
                    parser.add_argument(f"--{arg_name}", required=True, type=nested_field.type, help=f"{arg_name} (required)")
        else:
            if field.default is not None:
                parser.add_argument(f"--{field.name}", default=field.default, type=field.type, help=f"{field.name} (default: {field.default})")
            else:
                parser.add_argument(f"--{field.name}", required=True, type=field.type, help=f"{field.name} (required)")
    return parser.parse_args()