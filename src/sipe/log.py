# ┏━┓╻┏━┓┏━╸ ╻  ┏━┓┏━╸
# ┗━┓┃┣━┛┣╸  ┃  ┃ ┃┃╺┓
# ┗━┛╹╹  ┗━╸╹┗━╸┗━┛┗━┛

# SPDX-License-Identifier: MIT

# Author: Shane R. Spencer <spencersr@gmail.com>

# Structlog: https://github.com/hynek/structlog
from structlog import get_logger
from structlog.dev import ConsoleRenderer, set_exc_info, _has_colorama
from structlog.processors import TimeStamper, StackInfoRenderer, format_exc_info
from structlog.contextvars import merge_contextvars

_logger = get_logger(
    processors=[
        merge_contextvars,
        StackInfoRenderer(),
        set_exc_info,
        format_exc_info,
        TimeStamper(fmt="%Y-%m-%d %H:%M.%S", utc=False),
        ConsoleRenderer(colors=_has_colorama),
    ]
)

access_log = _logger.bind()
app_log = _logger.bind()
gen_log = _logger.bind()


class Wut(object):
    def __init__(self):
        ...


def stuff() -> None:
    return None
