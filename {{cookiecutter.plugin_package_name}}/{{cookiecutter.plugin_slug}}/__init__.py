from typing import Any, Dict, Optional

from tartiflette import Directive, Resolver, Scalar

_SDL = """
Write your plugin's SDL here
"""

__all__ = ("bake",)


async def bake(
    schema_name: str, config: Optional[Dict[str, Any]] = None
) -> str:
    """
    Links the plugin to the appropriate schema and returns the SDL related
    to the plugin.
    :param schema_name: schema name to link with
    :param config: configuration of the plugin
    :type schema_name: str
    :type config: Optional[Dict[str, Any]]
    :return: the SDL related to the plugin
    :rtype: str
    """
    # Do your magic here, instanciate and decorate your directives, scalars and
    # so on.
    return _SDL
