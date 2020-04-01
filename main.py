import numpy as np
import tensornetwork as tn

tn.set_default_backend('numpy')

I = np.eye(2)
X = np.array([[0, 1], [1, 0]])

# Shape convention for core nodes: (left, right, bottom, top)
x = 2
thrice_bot, thrice = np.zeros((2, 2, x, x)), np.zeros((2, 2, 1, x))
addone_bot, addone = np.zeros((2, 2, 2, 2)), np.zeros((2, 2, 1, 2))

# FILL IN NONZERO ENTRIES OF CORES USING SIMPLE DERIVATION 

thrice_unit = AlgPEPS(tn.node(thrice_bot), tn.node(thrice))
addone_unit = AlgPEPS(tn.node(addone_bot), tn.node(addone))

class AlgPEPS:
    def __init__(self, bot_core, core):
        self.bot_core = bot_core
        self.core = core

    def convert_to_minimal(self):
        """
        Losslessly compress vertical bonds of AlgPEPS to get minimal cores
        """
        pass

        self.bot_core = minimal_bot
        self.core = minimal_core

    def __matmul__(self, right_unit):
        """
        Multiply two AlgPEPS along their horizontal edges to get new one
        """
        pass

        return AlgPEPS(prod_bot, prod_core)

