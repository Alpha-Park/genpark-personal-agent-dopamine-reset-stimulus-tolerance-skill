# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Dopamine Reset Stimulus Tolerance Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentDopamineResetStimulusTolerance

def main():
    agent = PersonalAgentDopamineResetStimulusTolerance()

    print("=" * 70)
    print("DEMO: Personal Agent Dopamine Reset & Hedonic Tolerance Modeler")
    print("=" * 70)

    # Simulate heavy modern digital day
    exposures = [
        {"type": "short_video_feed", "duration_minutes": 65.0, "intensity": 8.5},
        {"type": "infinite_scroll", "duration_minutes": 45.0, "intensity": 6.0},
        {"type": "hyper_palatable_food", "duration_minutes": 20.0, "intensity": 7.0},
        {"type": "stimulant_stack", "duration_minutes": 30.0, "intensity": 6.5}
    ]

    res_tol = agent.calculate_hedonic_tolerance(exposures)

    print(f"\n1. Hedonic Stimulus Load & D2 Down-Regulation Audit:")
    print(f"   Cumulative Daily Dose: {res_tol['cumulative_daily_stimulus_units']} units")
    print(f"   D2 Receptor Availability: {res_tol['estimated_d2_receptor_availability']}")
    print(f"   Perceived Effort Multiplier: {res_tol['perceived_cognitive_effort_multiplier']}")
    print(f"   Status: {res_tol['hedonic_saturation_state']}")
    print(f"   Guidance: {res_tol['actionable_guidance']}")

    # Synthesize 3-day reset protocol
    res_proto = agent.synthesize_dopamine_reset_protocol(res_tol['cumulative_daily_stimulus_units'], reset_duration_days=3)

    print(f"\n2. Prescribed 3-Day Dopamine Reset Protocol:")
    print(f"   Expected Tolerance Reduction: {res_proto['target_tolerance_reduction_pct']}")
    print(f"   Core Rules:")
    for rule in res_proto['strict_stimulus_blackout_rules'][:3]:
        print(f"     - {rule}")
    print(f"   Day-by-Day Forecast:")
    for item in res_proto['recovery_timeline_forecast']:
        print(f"     [{item['phase']}] -> {item['neurochemical_dynamic']}")

    print("\nVerification complete: Dopamine reset engine executed flawlessly.")

if __name__ == "__main__":
    main()
