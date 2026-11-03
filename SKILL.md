---
name: genpark-personal-agent-acoustic-efferent-olivocochlear-reflex-moc-skill
description: Medial Olivocochlear (MOC) efferent acoustic reflex and otoacoustic emission suppression analyzer. Evaluates contralateral broadband noise suppression of distortion product otoacoustic emissions, quantifying efferent auditory protection and speech-in-noise perception.
version: 1.0.0
author: GenPark Ecosystem
license: Apache-2.0
tags:
  - personal-agent
  - audiology
  - olivocochlear
  - oae
  - hearing-protection
  - openclaw
  - genpark
  - mcp
---

# Medial Olivocochlear (MOC) Efferent Acoustic Reflex Skill

## Overview
This skill calculates efferent suppression of otoacoustic emissions (OAEs) under contralateral acoustic stimulation (CAS):
- **Cochlear Damping**: Uncrossed and crossed medial olivocochlear cholinergic fibers synapse directly onto cochlear outer hair cells (OHCs).
- **Suppression Delta ($\Delta\text{dB}$)**: Acoustic stimulation of the contralateral ear activates the MOC bundle, attenuating OHC electromotility and reducing emission amplitude by 1.0 to 3.5 dB in healthy ears.
- **Auditory Fitness**: Blunted MOC suppression ($<0.5\text{ dB}$) indicates vulnerable auditory hair cells, impaired speech-in-noise comprehension, or hidden efferent synaptopathy.

## Mathematical Formulation
1. **Suppression Amplitude Delta**:
   $$\Delta\text{dB} = \text{OAE}_{\text{quiet}} - \text{OAE}_{\text{CAS}}$$
2. **Linear Damping Percentage**:
   $$\text{Damping} = \frac{10^{\text{OAE}_{\text{quiet}} / 20} - 10^{\text{OAE}_{\text{CAS}} / 20}}{10^{\text{OAE}_{\text{quiet}} / 20}} \times 100\%$$
3. **Signal-to-Noise Ratio (SNR)**:
   $$\text{SNR} = \text{OAE}_{\text{quiet}} - \text{NoiseFloor}$$

## Usage
```python
from client import MedialOlivocochlearReflexClient

client = MedialOlivocochlearReflexClient()
res = client.evaluate_moc_suppression(
    baseline_oae_amplitude_db_spl=12.5,
    suppressed_oae_amplitude_db_spl=10.5,
    cas_noise_level_db_spl=60.0
)
print(res["evaluation"]["cochlear_protection"])
```
