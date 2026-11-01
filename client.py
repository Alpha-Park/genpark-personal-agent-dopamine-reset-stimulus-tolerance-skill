# -*- coding: utf-8 -*-
"""
Personal Agent Dopamine Reset Stimulus Tolerance Client
Zero-dependency hedonic tolerance estimator, striatal D2 receptor down-regulation modeler,
and structured digital/sensory dopamine reset protocol synthesizer.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentDopamineResetStimulusTolerance:
    """
    Quantifies supernormal stimulus overload across algorithm feeds, notifications,
    hyper-palatable foods, and games, tracking hedonic baseline depression and prescribing resets.
    """

    def calculate_hedonic_tolerance(
        self,
        high_stimulus_exposures_daily: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Calculates cumulative supernormal stimulus dose and estimated D2 receptor down-regulation.
        Each exposure has: type, duration_minutes, and perceived intensity (1-10).
        """
        if not high_stimulus_exposures_daily:
            return {
                "total_stimulus_dose_score": 0.0,
                "d2_receptor_availability_pct": "100.0%",
                "effort_discounting_factor": "1.0x (Pristine intrinsic motivation)",
                "hedonic_status": "Baseline Restored (High motivation for low-friction tasks)"
            }

        total_points = 0.0
        breakdown = []

        # Stimulus weighting factors based on variable reward schedules & speed of delivery
        weights = {
            "short_video_feed": 2.4, # TikTok, Reels, Shorts (rapid variable reward)
            "infinite_scroll": 1.6,  # Twitter/X, Reddit feeds
            "hyper_palatable_food": 1.8, # Refined sugar, seed oils, fast food
            "video_gaming": 1.7,     # High-arousal multiplayer gaming
            "pornography": 2.8,      # Maximum supernormal sexual stimulus
            "stimulant_stack": 2.0   # Excessive caffeine, nicotine, pre-workouts
        }

        for item in high_stimulus_exposures_daily:
            stype = str(item.get("type", "infinite_scroll")).lower()
            dur = max(1.0, min(600.0, float(item.get("duration_minutes", 15.0))))
            intensity = max(1.0, min(10.0, float(item.get("intensity", 5.0))))

            w = weights.get(stype, 1.3)
            # Stimulus dose formula: w * (duration / 10) * (intensity / 5)^1.2
            dose = round(w * (dur / 10.0) * math.pow(intensity / 5.0, 1.2), 1)
            total_points += dose

            breakdown.append({
                "stimulus_type": stype,
                "duration_minutes": dur,
                "calculated_dose_units": dose
            })

        total_points = round(total_points, 1)

        # D2 receptor availability down-regulation model
        # Base: 100%, drops down asymptotically towards 35% under extreme chronic overload
        downregulation_factor = min(65.0, (total_points / 120.0) * 50.0)
        d2_availability = round(100.0 - downregulation_factor, 1)

        # Effort discounting: how much harder standard deep work feels
        effort_discount = round(1.0 + (downregulation_factor / 30.0), 2)

        if total_points < 35.0:
            status = "Nominal Stimulus Exposure (Healthy Hedonic Tone)"
            action = "Intrinsic focus intact. Maintain mindful digital boundary discipline."
        elif total_points < 85.0:
            status = "Moderate Hedonic Tolerance (Elevated Procrastination Risk)"
            action = "Implement a 24-hour micro-reset eliminating short-form feeds and snacking."
        else:
            status = "Severe Supernormal Stimulus Saturation (Anhedonia / Friction Aversion)"
            action = "Mandatory 48-72 hour structured dopamine reset. Enforce digital curfew."

        return {
            "cumulative_daily_stimulus_units": total_points,
            "estimated_d2_receptor_availability": f"{d2_availability}% of pristine baseline",
            "perceived_cognitive_effort_multiplier": f"{effort_discount}x harder to initiate deep work",
            "hedonic_saturation_state": status,
            "actionable_guidance": action,
            "exposure_contributions": breakdown
        }

    def synthesize_dopamine_reset_protocol(
        self,
        tolerance_score: float,
        reset_duration_days: int = 2
    ) -> Dict[str, Any]:
        """
        Generates a phased, neuro-restorative reset protocol detailing forbidden supernormal
        stimuli and prescribed low-dopamine grounding activities.
        """
        days = max(1, min(7, int(reset_duration_days)))
        score = max(0.0, float(tolerance_score))

        rules = [
            "STRICT BLACKOUT: Zero short-form algorithmic video platforms (TikTok, Reels, Shorts).",
            "COMMUNICATION DIET: Text messaging and email processed only in 2 scheduled 15-min batches.",
            "AUDITORY DELOAD: Zero podcasts, audiobooks, or background music during walking or transit.",
            "NUTRITIONAL SIMPLICITY: Monophasic whole foods only (eggs, lean meat, vegetables, rice). Zero processed sugars or sauces.",
            "BEDROOM SANCTUARY: Physical phone kept in separate room 60 minutes before bedtime."
        ]

        prescribed_activities = [
            ("Morning Sunlight Ambulation", "30-45 minutes walking outside in natural daylight with zero headphones."),
            ("Analog Deep Reading", "45-60 minutes reading physical paper books or long-form literature."),
            ("Tactile Journaling", "Unstructured stream-of-consciousness journaling on paper to process mental chatter."),
            ("Boredom Tolerance Training", "15 minutes sitting in silence with zero input to re-sensitize striatal receptors.")
        ]

        # Phased recovery trajectory
        timeline = []
        for d in range(1, days + 1):
            if d == 1:
                phase_title = "Day 1: Acute Friction & Craving Wave"
                expected_symptoms = "Peak restlessness, phantom pocket vibrations, urge to check device every 6 minutes."
            elif d == 2:
                phase_title = "Day 2: Neurochemical Stabilization"
                expected_symptoms = "Craving amplitude attenuates by ~40%. Calmer mental baseline, increased sensory awareness."
            else:
                phase_title = f"Day {d}: Striatal D2 Re-sensitization & Flow Restoration"
                expected_symptoms = "Deep work friction drops. Reading and analytical thought feel intrinsically rewarding again."
            
            timeline.append({
                "day_number": d,
                "phase": phase_title,
                "neurochemical_dynamic": expected_symptoms
            })

        return {
            "prescribed_reset_duration_days": days,
            "target_tolerance_reduction_pct": f"-{round(min(80.0, days * 28.0), 1)}% tolerance units",
            "strict_stimulus_blackout_rules": rules,
            "restorative_grounding_activities": prescribed_activities,
            "recovery_timeline_forecast": timeline
        }
