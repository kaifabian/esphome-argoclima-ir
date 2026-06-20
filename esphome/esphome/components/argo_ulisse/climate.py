import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import climate_ir
from esphome.const import CONF_CHANNEL

AUTO_LOAD = ["climate_ir"]

argo_ulisse_ns = cg.esphome_ns.namespace("argo_ulisse")
ArgoUlisseClimate = argo_ulisse_ns.class_("ArgoUlisseClimate", climate_ir.ClimateIR)

ArgoProtocolVersion = argo_ulisse_ns.enum("ArgoProtocolVersion")
PROTOCOL_VERSIONS = {
    "WREM-2": ArgoProtocolVersion.ARGO_PROTOCOL_WREM2,
    "WREM-3": ArgoProtocolVersion.ARGO_PROTOCOL_WREM3,
}

CONF_PROTOCOL_VERSION = "protocol_version"
CONF_IFEEL_UPDATE_INTERVAL = "ifeel_update_interval"

CONFIG_SCHEMA = climate_ir.climate_ir_with_receiver_schema(ArgoUlisseClimate).extend({
    cv.Optional(CONF_PROTOCOL_VERSION, default="WREM-3"): cv.enum(PROTOCOL_VERSIONS, upper=True),
    cv.Optional(CONF_CHANNEL, default=0): cv.int_range(min=0, max=3),
    cv.Optional(CONF_IFEEL_UPDATE_INTERVAL, default="30s"): cv.positive_time_period_milliseconds,
})


async def to_code(config):
    var = await climate_ir.new_climate_ir(config)
    cg.add(var.set_protocol_version(config[CONF_PROTOCOL_VERSION]))
    cg.add(var.set_channel(config[CONF_CHANNEL]))
    cg.add(var.set_ifeel_update_interval(config[CONF_IFEEL_UPDATE_INTERVAL]))
