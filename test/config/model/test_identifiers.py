import pytest

from hypothesis import given, note, strategies as st

from sipe.config.models.identifiers import (
    IdentifierHeaderModel,
    IdentifierModel,
    IdentifierNetworkModel,
)

# These are doctests

# def test_bare_identifier():
#     identifier = IdentifierModel()


# def test_bare_identifier_network_should_error():
#     try:
#         identifier_network = IdentifierNetworkModel()
#         return False
#     except Exception:
#         return True


# def test_bare_identifier_header_should_error():
#     try:
#         identifier_header = IdentifierHeaderModel()
#         return False
#     except Exception:
#         return True
