# %%
import pyslimmc as sl
import matplotlib.pyplot as plt
import numpy as np

# Digitized w(log10 M) data from Buback et al. (1996), Fig. 1
buback1996_logM = np.linspace(3.5, 6.0, 100)
buback1996_wlogM = np.array([
    0.03000, 0.04024, 0.05024, 0.05319, 0.05928, 0.06206, 0.07388,
    0.07862, 0.08606, 0.09456, 0.10003, 0.11229, 0.12170, 0.12617,
    0.14184, 0.15286, 0.16396, 0.17883, 0.18698, 0.20623, 0.21868,
    0.23345, 0.25118, 0.26712, 0.28288, 0.29811, 0.31852, 0.33661,
    0.35586, 0.37512, 0.39571, 0.41658, 0.43431, 0.45804, 0.47729,
    0.49959, 0.52466, 0.54409, 0.56908, 0.59102, 0.61054, 0.63570,
    0.65683, 0.70304, 0.90721, 1.51972, 1.99934, 1.88418, 1.63094,
    1.41199, 1.24096, 1.12025, 1.01440, 0.93202, 0.85993, 0.78901,
    0.81954, 1.33677, 1.59825, 1.18167, 0.88894, 0.67636, 0.55368,
    0.47308, 0.66051, 0.73062, 0.46986, 0.31440, 0.23327, 0.29363,
    0.26175, 0.16289, 0.11498, 0.13128, 0.09053, 0.06018, 0.06206,
    0.04827, 0.03842, 0.03842, 0.02795, 0.01698, 0.00879, 0.00121,
    0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000,
    0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000,
    0.00000, 0.00000
])


# Expected molar-mass increment accumulated during one pulse interval
#M0 = kp * conc_MMA * delta_t * M_MMA

#kp = 480 # mol/L*s
#conc_MMA = 9.18 # mol/L
#delta_t = 0.1 # s
#M_MMA = 100.12 # g/mol

#M0 = kp * conc_MMA * delta_t * M_MMA


# Read the simulation results
run = sl.open("results")

# %%

mwd = run.mwd()

plt.figure(figsize=(5, 3))

#for x in [np.log10(M0), np.log10(2*M0), np.log10(3*M0), np.log10(4*M0)]:
#    plt.axvline(x=x, linestyle="-", linewidth=0.5, color='black')

plt.plot(mwd.x, mwd.y, 'c-', label='slimmc')
plt.plot(buback1996_logM, buback1996_wlogM, 'k--', label='Buback et al. (1996), Fig. 1')

plt.xlabel("log$_{10}$(M / g mol$^{-1}$)")
plt.ylabel("dw/dlog$_{10}$(M)")
plt.xlim(3.5,6.0)
plt.legend(loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=2, frameon=False)
plt.tight_layout()
plt.savefig("fig1.png", dpi=300)

