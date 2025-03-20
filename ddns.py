"""
This module is used to get the IP address of a given DNS Record.
"""
import ipaddress
import socket

# pylint: disable=too-few-public-methods


class DDNS:
    """DDNS related operations."""

    @staticmethod
    def get_ipv4(hostname: str) -> str | None:
        """
        Get exactly one valid IPv4 address for the given hostname.
        Returns None if resolution fails or the result is not a valid IPv4.
        """
        try:
            ip_str = socket.gethostbyname(hostname)
            ipaddress.IPv4Address(ip_str)
            return ip_str

        except (socket.gaierror, ipaddress.AddressValueError):
            return None

        except Exception as e:
            print(f"Unexpected error: {e}")
            raise e

    @staticmethod
    def bulk_get_ipv4(hostnames: list[str]) -> list[str]:
        """
        Get exactly one valid IPv4 address for each hostname in the list.
        Returns a list of valid IPv4 addresses.
        """
        for index, hostname in enumerate(hostnames):
            hostnames[index] = DDNS.get_ipv4(hostname)

        return hostnames
