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

## usage
