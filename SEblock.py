import torch
import torch.nn as nn
import torch.nn.functional as F


class SE(nn.Module):

    def __init__(self, in_chnls, ratio=2):
        super(SE, self).__init__()
        self.squeeze = nn.AdaptiveAvgPool2d((1, 1))
        self.compress = nn.Conv2d(in_chnls, in_chnls // ratio, 1, 1, 0)
        self.excitation = nn.Conv2d(in_chnls // ratio, in_chnls, 1, 1, 0)

    def forward(self, x):
        out = self.squeeze(x)
        out = self.compress(out)
        out = F.relu(out)
        out = self.excitation(out)
        return x*nn.Sigmoid()(out)
if __name__ == '__main__':
    img = torch.randn(16, 32, 20, 20)
    net = SE(32)
    print(net)
    out = net(img)
    print(out.size())