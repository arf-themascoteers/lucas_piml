import torch
import torch.nn as nn


class ANNSimple10(nn.Module):
    def __init__(self, device, input_size, X_columns, y_column, alpha=0.5):
        super().__init__()
        self.device = device
        self.input_size = input_size
        self.X_columns = X_columns
        self.y_column = y_column

        self.input_to_soc = nn.Sequential(
            nn.Linear(input_size, 30),
            nn.LeakyReLU(),
            nn.Linear(30, 1)
        )
        self.criterion_soc = torch.nn.MSELoss(reduction='sum')

    def forward(self, x, soc):
        soc_hat = self.input_to_soc(x)
        soc_hat = soc_hat.reshape(-1)
        loss_soc = 10 * self.criterion_soc(soc_hat, soc)
        return soc_hat, soc_hat, loss_soc
