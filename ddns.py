"""
This module is used to get the IP address of a given DNS Record.
"""
import ipaddress
import socket
from urllib.parse import urlsplit

# pylint: disable=too-few-public-methods


class DDNS:
    """DDNS related operations."""

    @staticmethod
    def get_ipv4(hostname: str) -> str | None:
        """
        Get exactly one valid IPv4 address for the given hostname, URL or IP
        (e.g. "example.com", "https://example.com:8443/path").
        Returns None if resolution fails or the result is not a valid IPv4.
        """
        try:
            host = urlsplit(hostname if "://" in hostname else f"//{hostname}").hostname
            ip_str = socket.gethostbyname(host)
            ipaddress.IPv4Address(ip_str)
            return ip_str

        # gaierror is an OSError; bad input (None, "", over-long labels) raises TypeError/ValueError.
        except (OSError, TypeError, ValueError):
            return None

    @staticmethod
    def bulk_get_ipv4(hostnames: list[str]) -> list[str | None]:
        """
        Get exactly one valid IPv4 address for each hostname in the list.
        Returns a new list, in the same order; an entry is None where resolution failed.
        """
        return [DDNS.get_ipv4(hostname) for hostname in hostnames]
