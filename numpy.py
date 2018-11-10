from pygsp import graphs, filters
G = graphs.Logo()
G.estimate_lmax()
g = filters.Heat(G, tau=100)
import numpy as np
DELTAS = [20, 30, 1090]
s = np.zeros(G.N)
s[DELTAS] = 1
s = g.filter(s)
G.plot_signal(s, highlight=DELTAS, backend='matplotlib')