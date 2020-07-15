# ┏━┓╻┏━┓┏━╸ ┏━╸┏━┓┏┓╻┏━┓┏━┓╻  ┏━╸
# ┗━┓┃┣━┛┣╸  ┃  ┃ ┃┃┗┫┗━┓┃ ┃┃  ┣╸
# ┗━┛╹╹  ┗━╸╹┗━╸┗━┛╹ ╹┗━┛┗━┛┗━╸┗━╸

# SPDX-License-Identifier: MIT

# Author: Shane R. Spencer <spencersr@gmail.com>

# Sipe Project: Absolute
from sipe.log import gen_log

console_log = gen_log.bind()


def main() -> None:
    console_log.info("sup dog")
