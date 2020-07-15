# ┏━┓╻┏━┓┏━╸ ┏━╸┏━┓┏┓╻┏━╸╻┏━╸ ┏┳┓┏━┓╺┳┓┏━╸╻  ┏━┓ ╻╺┳┓┏━╸┏┓╻╺┳╸╻┏━╸╻┏━╸┏━┓┏━┓
# ┗━┓┃┣━┛┣╸  ┃  ┃ ┃┃┗┫┣╸ ┃┃╺┓ ┃┃┃┃ ┃ ┃┃┣╸ ┃  ┗━┓ ┃ ┃┃┣╸ ┃┗┫ ┃ ┃┣╸ ┃┣╸ ┣┳┛┗━┓
# ┗━┛╹╹  ┗━╸╹┗━╸┗━┛╹ ╹╹  ╹┗━┛╹╹ ╹┗━┛╺┻┛┗━╸┗━╸┗━┛╹╹╺┻┛┗━╸╹ ╹ ╹ ╹╹  ╹┗━╸╹┗╸┗━┛

# SPDX-License-Identifier: MIT

# Author: Shane R. Spencer <spencersr@gmail.com>

# Standard Library
from typing import List, Pattern, Optional
from ipaddress import IPv4Network, IPv6Network

# Pydantic: https://github.com/samuelcolvin/pydantic/
from pydantic import BaseModel


class IdentifierHeaderModel(BaseModel):
    """
    >>> try:
    ...     IdentifierHeaderModel()
    ... except:
    ...     False
    ... else:
    ...     True
    ...
    False
    """

    key: Pattern
    value: Pattern


class IdentifierNetworkModel(BaseModel):
    """
    >>> IdentifierNetworkModel()
    IdentifierNetworkModel(ipv4=[], ipv6=[])
    """

    ipv4: List[IPv4Network] = []
    ipv6: List[IPv6Network] = []


class IdentifierModel(BaseModel):
    """ Contains the lists of all possible identifiers.

    >>> IdentifierModel()
    IdentifierModel(networks=[], headers=[])

    >>> network = IdentifierNetworkModel(ipv4=[IPv4Network('192.168.1.0/24')])
    >>> identifier = IdentifierModel(networks=[network])
    >>> identifier.dict()
    {'networks': [{'ipv4': [IPv4Network('192.168.1.0/24')], 'ipv6': []}], 'headers': []}

    """

    networks: List[IdentifierNetworkModel] = []
    headers: List[IdentifierHeaderModel] = []


class Something(BaseModel):
    """"""

    ...
