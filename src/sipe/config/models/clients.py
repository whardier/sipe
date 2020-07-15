# ┏━┓╻┏━┓┏━╸ ┏━╸┏━┓┏┓╻┏━╸╻┏━╸ ┏┳┓┏━┓╺┳┓┏━╸╻  ┏━┓ ┏━╸╻  ╻┏━╸┏┓╻╺┳╸┏━┓
# ┗━┓┃┣━┛┣╸  ┃  ┃ ┃┃┗┫┣╸ ┃┃╺┓ ┃┃┃┃ ┃ ┃┃┣╸ ┃  ┗━┓ ┃  ┃  ┃┣╸ ┃┗┫ ┃ ┗━┓
# ┗━┛╹╹  ┗━╸╹┗━╸┗━┛╹ ╹╹  ╹┗━┛╹╹ ╹┗━┛╺┻┛┗━╸┗━╸┗━┛╹┗━╸┗━╸╹┗━╸╹ ╹ ╹ ┗━┛

# SPDX-License-Identifier: MIT

# Author: Shane R. Spencer <spencersr@gmail.com>

# Standard Library
from typing import List

# Pydantic: https://github.com/samuelcolvin/pydantic/
from pydantic import BaseModel

# Sipe Project: Absolute
from sipe.config.models.identifiers import IdentifierModel


class ClientModel(BaseModel):

    identifiers: List[IdentifierModel]
