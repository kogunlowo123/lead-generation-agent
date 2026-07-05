"""Lead Generation Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_search_prospects():
    """Test Search for potential leads matching ideal customer profile."""
    tools = AgentTools()
    result = await tools.search_prospects(icp_criteria="test", sources="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_score_lead():
    """Test Score a lead based on firmographic, technographic, and intent data."""
    tools = AgentTools()
    result = await tools.score_lead(lead_data="test", scoring_model="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_enrich_contact():
    """Test Enrich lead contact data with verified email, phone, and social profiles."""
    tools = AgentTools()
    result = await tools.enrich_contact(lead_id="test", enrichment_sources="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_qualify_lead():
    """Test Qualify lead against BANT or MEDDIC framework."""
    tools = AgentTools()
    result = await tools.qualify_lead(lead_id="test", framework="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.lead_generation_agent_agent import LeadGenerationAgentAgent
    agent = LeadGenerationAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
