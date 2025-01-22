# InterVelo
## Discription
![figure1](https://github.com/user-attachments/assets/5822bddd-be01-4083-8b68-98c2db17a0e7)
InterVelo is a python package that simultaneously learns cellular pseudotime and RNA velocity. RNA velocity plays a crucial role in uncovering cellular trajectory and genetic transcriptional dynamics from snapshot single-cell data. However, existing RNA velocity inference methods often assume constant transcriptional rates and treat genes independently, which can introduce biases and deviate from biological realities. To address these limitations, we have proposed InterVelo, a novel framework that simultaneously learns cellular pseudotime and RNA velocity. InterVelo uses estimated pseudotime to guide RNA velocity inference and leverages the inferred RNA velocity to refine pseudotime estimation.

## Installation

Clone this repository and install it via pip:

```bash
git clone https://github.com/yurouwang-rosie/InterVelo.git
cd InterVelo
pip install .
```
## Example
```python
import scvelo as scv
import numpy as np
import random
import torch
from scvelo.preprocessing.moments import get_moments
import gc

from InterVelo.train import train, Constants
from InterVelo.simulation2 import simulation
from InterVelo._utils import update_dict, autoset_coeff_s
from InterVelo.data import preprocess_data

SEED = 1
torch.manual_seed(SEED)
torch.backends.cudnn.enabled = True
torch.backends.cudnn.benchmark = True
np.random.seed(SEED)
random.seed(SEED)
#multiomic simulated data
alpha = np.random.lognormal(mean=2, sigma=1, size=1000)
alpha_c = np.random.lognormal(mean= -2, sigma=0.5, size=1000)
beta = np.random.lognormal(mean= 0, sigma=0.3, size=1000)
gamma = np.random.lognormal(mean= 0, sigma=0.3, size=1000)
adata = simulation(
        n_obs=10000, n_vars=1000, alpha_c=alpha_c, alpha=alpha, beta=beta, gamma=gamma,
        alpha_=0, t_max=20, noise_model="normal", noise_level=0.8, 
        random_seed=SEED
        )

adata.var["alpha_c"]=alpha_c
adata.var["alpha"]=alpha
adata.var["beta"]=beta
adata.var["gamma"]=gamma
#preprocess data
scv.pp.filter_and_normalize(adata, min_shared_counts=20, n_top_genes=2000)
scv.pp.normalize_per_cell(adata)
scv.pp.log1p(adata)
scv.pp.moments(adata, n_pcs=30, n_neighbors=30) ##30
adata.layers["Ma"]=get_moments(adata, layer="atac")
adata = preprocess_data(adata, layers=["Ma","Ms","Mu"], filter_on_r2=False)
#spliced = csr_matrix(adata.layers["spliced"]).astype(np.float32).A
spliced = torch.tensor(adata.layers["Ms"])
unspliced = torch.tensor(adata.layers["Mu"])
inputdata = torch.tensor(adata.layers["Ma"].astype(np.float32))
inputdata=torch.cat([spliced,unspliced,inputdata],dim=1)
#model train  
configs = {
        "name": "InterVelo", # name of the experiment
        "loss_pearson": {"coeff_s": autoset_coeff_s(adata)},# Automatic setting of the spliced correlation objective
        "trainer": { "epochs": 100, "loss1_epochs":0},
    }
configs = update_dict(Constants.default_configs, configs)
trainer = train(adata, inputdata, configs)
```
