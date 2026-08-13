# A01 PLP Buback 1996

## 1. Scientific question

Can Slimmc reproduce the molecular-weight distribution shown in **Fig. 1 of Buback et al. [1]** for pulsed-laser polymerization (PLP) of methyl methacrylate (MMA)?

## 2. Source

The reference case is **Fig. 1 of Buback et al. [1]**.
The reference curve used for comparison was digitized from the published figure.

## 3. Model

The Slimmc model contains MMA, primary radicals `R`, active polymer chains `P`, and dead polymer chains `D`. The mechanism includes initiation, propagation, and termination by disproportionation.

The relevant part of the model file is:

```code

desc "Modeling of molecular weight distribution in pulsed laser free-radical homopolymerizations"

param seed 1000
param kmc_volume 1e-13
# total simulation time 2s
param t_end 2
param output_dir "results"

monomer MMA 9.18 100.12
species R 0
polymer P active
polymer D dead

rate ki 4800
rate kp 480

# only termination by disproportionation
rate ktc 0
rate ktd 2.5e7


macro init R + MMA -> P ki
macro prop P + MMA -> P kp
macro term_c P + P -> D ktc
macro term_d P + P -> D + D ktd

# each laser pulse adds 5e-7 mol/L primary radicals
# 20 pulses, prr of 10 Hz
from 0.0 repeat 20 every 0.1 add_c R 5e-7

# save state
every 0.1 save
# save macromolecular state
every 0.1 save_chains

every 0.1 print_info


```

Each laser pulse is represented as an instantaneous addition of primary radicals. Twenty pulses are applied at a pulse repetition rate of 10 Hz.

## 4. Parameters

| Parameter | Value | Origin |
|---|---:|---|
| `[MMA]0` | 9.18 mol/L | calculated from MMA density and molar mass |
| `M_MMA` | 100.12 g/mol | physical property of MMA |
| `ki` | 4800 L/(mol s) | assumed effective initiation coefficient |
| `kp` | 480 L/(mol s) | taken from [1] |
| `ktc` | 0 L/(mol s) | assumed; combination disabled |
| `ktd` | 2.5e7 L/(mol s) | taken from [1] |
| radical increment | 5e-7 mol/L per pulse | taken from [1] |
| pulse repetition rate | 10 Hz | taken from [1] |
| number of pulses | 20 | simulation setting |
| `t_end` | 2 s | simulation setting |
| `kmc_volume` | 1e-13 L | numerical simulation setting |
| `seed` | 1000 | numerical simulation setting |

The initial MMA concentration was calculated from

`[MMA]0 = rho / M`

using approximately `rho = 0.919 g/mL` and `M = 100.12 g/mol`, giving

`[MMA]0 ≈ 9.18 mol/L`.

The characteristic molar-mass increment during one pulse period is

`M0 = kp [M] Delta_t M_MMA`

which gives

`M0 ≈ 4.4e4 g/mol`.

## 5. Reproduction target

The reproduction target is the mass-weighted molecular-weight distribution

`dw/dlog10(M)`

shown in **Fig. 1 of [1]**.

The Slimmc result is compared directly with the digitized reference curve on the same `log10(M)` coordinate.

## 6. Expected result and acceptance criterion

The reproduction is considered successful if the principal PLP features occur at approximately the same molar masses as in the digitized reference curve and the overall distribution shape is reproduced.

The dominant first feature should occur close to `M0`, with subsequent structure appearing near higher multiples of this characteristic molar-mass increment.

## 7. Limitations

The reference curve was digitized from Fig. 1 of [1], which introduces a small digitization uncertainty.

The binning or smoothing procedure used to generate the distribution shown in [1] is not known, so small differences in local peak shape and fine structure should not be overinterpreted.

## 8. References

[1] M. Buback, M. Busch, R. A. Lämmel, “Modeling of molecular weight distribution in pulsed laser free-radical homopolymerizations,” *Macromolecular Theory and Simulations* **5** (1996) 845–861. https://doi.org/10.1002/mats.1996.040050505
