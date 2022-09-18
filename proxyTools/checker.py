from ..api.ipTest import IPTestAPI

def confirm_public_ip(proxy_dict, desired_ip):
    r, r2 = IPTestAPI().get_public_ip(proxy_dict)
    print(desired_ip, r.text, r2.text)
    ip_is_correct = r.text == desired_ip and r2.text == desired_ip
    return ip_is_correct
