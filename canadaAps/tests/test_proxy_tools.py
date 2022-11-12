import pytest
import socket
from ..util.proxyTools import ProxyTools


def arrange_get_proxy_ip():
    return ProxyTools().get_proxy_ip(0)


def arrange_create_proxy_dict(ip, port):
    return ProxyTools().create_proxy_dict(ip, port)


def arrange_confirm_public_ip(proxy_dict, proxy_ip):
    return ProxyTools().confirm_public_ip_is_proxy_ip(proxy_dict, proxy_ip)


def is_some_ip(test_string):
    for unit in test_string.split("."):
        if int(unit) < 0 or int(unit) > 255:
            return False
    return True


def is_some_port(test_port):
    if 0 < int(test_port) < 65535:
        return True
    return False

# @pytest.mark.skip(reason="uses external api - dont wanna run it every time")
def test_get_proxy_ip():
    ip, port = arrange_get_proxy_ip()
    assert is_some_ip(ip)
    assert is_some_port(port)
    return ip, port


# @pytest.mark.skip(reason="uses external api - dont wanna run it every time")
def get_current_public_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    current_ip = s.getsockname()[0]
    s.close()
    return current_ip


# @pytest.mark.skip(reason="uses external api - dont wanna run it every time")
def test_confirm_public_ip():
    ip, port = arrange_get_proxy_ip()
    proxy_dict = arrange_create_proxy_dict(ip, port)
    is_public_ip = arrange_confirm_public_ip(proxy_dict, ip)
    assert is_public_ip

