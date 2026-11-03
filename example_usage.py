"""
Example usage of Medial Olivocochlear (MOC) Efferent Reflex Skill.
Demonstrates normal robust contralateral suppression vs blunted efferent response.
"""

import json
from client import MedialOlivocochlearReflexClient


def main():
    print("=== Testing Medial Olivocochlear (MOC) Efferent Reflex Skill ===")
    client = MedialOlivocochlearReflexClient()

    # 1. Normal robust MOC suppression (Baseline OAE = 12.5 dB SPL, with CAS 60 dB = 10.5 dB SPL -> Delta = 2.0 dB)
    res_normal = client.evaluate_moc_suppression(
        baseline_oae_amplitude_db_spl=12.5,
        suppressed_oae_amplitude_db_spl=10.5,
        cas_noise_level_db_spl=60.0,
        frequency_hz=2000.0
    )
    print("\n[Case 1: Normal Robust MOC Efferent Suppression]")
    print(json.dumps(res_normal, indent=2))

    # 2. Blunted suppression / efferent neuropathy (Delta = 0.2 dB)
    res_blunted = client.evaluate_moc_suppression(
        baseline_oae_amplitude_db_spl=11.8,
        suppressed_oae_amplitude_db_spl=11.6,
        cas_noise_level_db_spl=60.0,
        frequency_hz=2000.0
    )
    print("\n[Case 2: Blunted MOC Suppression / Vulnerable Cochlea]")
    print(json.dumps(res_blunted, indent=2))

    # Assertions
    assert res_normal["suppression_delta_db"] == 2.0
    assert res_blunted["suppression_delta_db"] < 0.5
    assert res_normal["evaluation"]["cochlear_protection"] == "Optimal / Intact"
    print("\n[SUCCESS] Medial Olivocochlear Reflex tests passed!")


if __name__ == "__main__":
    main()
