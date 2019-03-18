# Von Mises Distribution

This is a demonstration of the work done by D.J. Best and N.I. Fisher ([found here](https://www.researchgate.net/profile/Nicholas_Fisher11/publication/246035131_Efficient_Simulation_of_the_von_Mises_Distribution/links/5a1cd6a3aca2726120b25d4a/Efficient-Simulation-of-the-von-Mises-Distribution.pdf))

This is a finite domain analogue to the Gaussian distribution. The von Mises distribution lies in the interval [-π, π], so to normalize it, you would have to take your output `n` and do the the following to it: `n_norm = (n + π)/2π`.

You can use this distribution to generate a random number over an interval, with a bias towards the center of that interval. This is quite handy sometimes and more practical than using a Gaussian distribution that could generate any real number.

A random sampling of the distribution can be found by running `python3 main.py`
