# This is a demonstration of the work done by D.J. Best and N.I. Fisher https://www.researchgate.net/profile/Nicholas_Fisher11/publication/246035131_Efficient_Simulation_of_the_von_Mises_Distribution/links/5a1cd6a3aca2726120b25d4a/Efficient-Simulation-of-the-von-Mises-Distribution.pdf

import math
import random

def von_mises(k):
    tau = 1 + (1 + 4 * (k**2))**0.5
    rho = (tau - (2 * tau)**0.5) / (2 * tau)
    u1, u2, u3 = random.random(), random.random(), random.random()
    r = (1 + rho**2)/(2*rho)
    z = math.cos(math.pi * u1)
    f = (1 + r * z)/(r+z)
    c = k * (r - f)
    theta = None

    if (c * (2 - c) - u2) > 0:
        theta = math.copysign(1, u3-0.5) * math.acos(f)

    while (math.log(c/u2) + 1 - c) < 0:
        u1, u2, u3 = random.random(), random.random(), random.random()
        z = math.cos(math.pi * u1)
        f = (1 + r * z)/(r+z)
        c = k * (r - f)
        if (c * (2 - c) - u2) > 0:
            theta = math.copysign(1, u3-0.5) * math.acos(f)
            break

    if theta is None:
        theta = math.copysign(1, u3-0.5) * math.acos(f)
    
    return theta

# Example to show the distribution
if __name__ == '__main__':
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    num = 1000

    points = [von_mises(1) for __ in range(num)]
    print(f'max: {max(points)}')
    print(f'min: {min(points)}')

    sns.set_style('whitegrid')
    sns.kdeplot(np.array(points), bw=0.5);
    plt.show()