"""
Medial Olivocochlear (MOC) Efferent Acoustic Reflex & OAE Suppression Client.
Zero-mock pure Python standard library implementation.
Calculates contralateral broadband acoustic suppression of Distortion Product
Otoacoustic Emissions (DPOAE / TEOAE), efferent suppression delta (dB),
and outer hair cell (OHC) motor electromotility modulation.
"""

import math
from typing import Dict, Any, List, Optional


class MedialOlivocochlearReflexClient:
    """
    Evaluates Medial Olivocochlear (MOC) efferent feedback bundle function by analyzing
    otoacoustic emission suppression under contralateral acoustic stimulation (CAS).
    """

    def __init__(self):
        pass

    def evaluate_moc_suppression(
        self,
        baseline_oae_amplitude_db_spl: float,
        suppressed_oae_amplitude_db_spl: float,
        cas_noise_level_db_spl: float = 60.0,
        frequency_hz: float = 2000.0,
        baseline_noise_floor_db_spl: float = -20.0
    ) -> Dict[str, Any]:
        """
        Calculates MOC efferent suppression index (dB) and efferent attenuation percentage.
        baseline_oae_amplitude_db_spl: OAE emission amplitude in quiet (dB SPL).
        suppressed_oae_amplitude_db_spl: OAE amplitude during contralateral acoustic stimulation (CAS) (dB SPL).
        cas_noise_level_db_spl: Intensity of contralateral noise stimulus (typically 50-65 dB SPL to avoid stapedial reflex).
        frequency_hz: Test probe frequency (Hz).
        baseline_noise_floor_db_spl: Probe microphone noise floor (dB SPL).
        """
        if baseline_oae_amplitude_db_spl < baseline_noise_floor_db_spl:
            raise ValueError("Baseline OAE signal must exceed microphone noise floor.")
        if cas_noise_level_db_spl < 20.0 or cas_noise_level_db_spl > 90.0:
            raise ValueError("CAS noise stimulus must be between 20.0 and 90.0 dB SPL.")

        # Efferent Suppression (Delta dB SPL):
        # Delta = Baseline_Amplitude - Suppressed_Amplitude
        suppression_delta_db = baseline_oae_amplitude_db_spl - suppressed_oae_amplitude_db_spl

        # Signal-to-noise ratio in quiet
        snr_quiet_db = baseline_oae_amplitude_db_spl - baseline_noise_floor_db_spl

        # Linear amplitude conversion:
        # Pressure P = 20 * 10^-6 * 10^(dB / 20)
        p_base = 10.0 ** (baseline_oae_amplitude_db_spl / 20.0)
        p_supp = 10.0 ** (suppressed_oae_amplitude_db_spl / 20.0)
        linear_damping_pct = max(0.0, min(100.0, ((p_base - p_supp) / p_base) * 100.0))

        # Clinical evaluation:
        # Normal healthy CAS MOC suppression in young/adult ears: 1.0 to 3.5 dB (damping 10% - 35%)
        # Sub-clinical efferent neuropathy (auditory processing disorder, noise vulnerability): < 0.5 dB
        # Hyper-suppression (> 4.0 dB): possible middle-ear acoustic reflex contamination if CAS > 75 dB SPL.
        stapedial_contamination_warning = False
        if cas_noise_level_db_spl > 70.0 and suppression_delta_db > 3.5:
            stapedial_contamination_warning = True

        if suppression_delta_db < 0.5:
            classification = "Blunted MOC Efferent Suppression / Efferent Neuropathy"
            pathophysiology = "Deficient cholinergic olivocochlear feedback; reduced cochlear protection against noise and impaired speech-in-noise perception."
            cochlear_protection = "Compromised"
        elif suppression_delta_db <= 1.0:
            classification = "Borderline / Mild Efferent Damping"
            pathophysiology = "Mild MOC attenuation; modest outer hair cell prestin motor inhibition."
            cochlear_protection = "Low-Normal"
        elif suppression_delta_db <= 3.5:
            classification = "Normal Robust Medial Olivocochlear Reflex"
            pathophysiology = "Intact brainstem-cochlear efferent loop modulating outer hair cell electromotility."
            cochlear_protection = "Optimal / Intact"
        else:
            if stapedial_contamination_warning:
                classification = "High Suppression with Middle-Ear Reflex Contamination"
                pathophysiology = "Suppression > 3.5 dB likely compounded by stapedial muscle contraction at high CAS levels."
                cochlear_protection = "Indeterminate / Reflex-Mixed"
            else:
                classification = "Supranormal Efferent Inhibition"
                pathophysiology = "Pronounced olivocochlear efferent hyper-responsiveness."
                cochlear_protection = "High"

        return {
            "status": "success",
            "frequency_hz": frequency_hz,
            "baseline_oae_db_spl": round(baseline_oae_amplitude_db_spl, 2),
            "suppressed_oae_db_spl": round(suppressed_oae_amplitude_db_spl, 2),
            "suppression_delta_db": round(suppression_delta_db, 2),
            "linear_damping_percentage": round(linear_damping_pct, 1),
            "signal_to_noise_ratio_db": round(snr_quiet_db, 1),
            "evaluation": {
                "classification": classification,
                "cochlear_protection": cochlear_protection,
                "stapedial_contamination_risk": stapedial_contamination_warning,
                "pathophysiology": pathophysiology
            }
        }
