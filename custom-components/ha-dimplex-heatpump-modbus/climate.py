"""Climate platform from Midea Smart AC."""
from __future__ import annotations

import logging

import voluptuous as vol

from homeassistant.components.climate import ClimateEntity
from homeassistant.components.climate.const import (
  PRESET_AWAY,
  PRESET_BOOST,
  PRESET_ECO,
  PRESET_NONE,
  PRESET_SLEEP,
  ClimateEntityFeature,
  HVACMode,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
  ATTR_TEMPERATURE,
  CONF_ENABLED,
  UnitOfTemperature,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers import entity_platform
from homeassistant.helpers.entity_platform import AddEntitiesCallback


_LOGER = loggign.getLogger(__name__)
