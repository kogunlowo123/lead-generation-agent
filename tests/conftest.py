"""Test configuration for Lead Generation Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "lead-generation-agent", "category": "Sales"}
