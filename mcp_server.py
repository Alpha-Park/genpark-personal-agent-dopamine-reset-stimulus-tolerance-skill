# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Dopamine Reset Stimulus Tolerance Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentDopamineResetStimulusTolerance

mcp = FastMCP("PersonalAgentDopamineResetStimulusTolerance")
client = PersonalAgentDopamineResetStimulusTolerance()

@mcp.tool()
def calculate_hedonic_tolerance(
    high_stimulus_exposures_daily: list[dict]
) -> str:
    """Calculates cumulative supernormal stimulus dose and estimated D2 receptor down-regulation."""
    import json
    return json.dumps(client.calculate_hedonic_tolerance(high_stimulus_exposures_daily), indent=2)

@mcp.tool()
def synthesize_dopamine_reset_protocol(
    tolerance_score: float,
    reset_duration_days: int = 2
) -> str:
    """Generates a structured multi-day dopamine reset protocol to restore intrinsic motivation."""
    import json
    return json.dumps(client.synthesize_dopamine_reset_protocol(tolerance_score, reset_duration_days), indent=2)

if __name__ == "__main__":
    mcp.run()
