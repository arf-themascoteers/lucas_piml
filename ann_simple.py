import torch
import torch.nn as nn


class ANNSimple(nn.Module):
    def __init__(self, device, input_size, X_columns, y_column, alpha=0.5):
        super().__init__()
        self.device = device
        self.input_size = input_size
        self.X_columns = X_columns
        self.y_column = y_column

        self.inputsoc_to_savi = nn.Sequential(
            nn.Linear(1, 10),
            nn.LeakyReLU(),
            nn.Linear(10, 1)
        )
        self.criterion_soc = torch.nn.MSELoss(reduction='mean')

    def forward(self, x, soc):
        soc_hat = self.input_to_soc(x)
        soc_hat = soc_hat.reshape(-1)
        loss_soc = self.criterion_soc(soc_hat, soc)
        return soc_hat, soc_hat, loss_soc