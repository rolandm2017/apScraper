from simple_chalk import chalk

from dotenv import load_dotenv
import os
from time import sleep

from canadaAps.api.proxyAPI import ProxyAPI
from canadaAps.scraper.Logger import report_progress

load_dotenv()

username = os.getenv("username")
password = os.getenv("password")
print(username, password)
if username is None or password is None:
    raise RuntimeError("invalid env file")

class ProxyTools:
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_ip(choice):
        token = os.environ.get("apikey")

        selected_proxy_ip = None
        selected_proxy_port = None
        # todo: if throttled, rerun function with "choice + 1"
        while selected_proxy_ip is None or selected_proxy_port is None:
            # r = ProxyAPI().get_proxy_connection_info(token)
            # result = r.json()
            result = get_hardcoded_proxy_conn_info()

            try:
                if result["detail"] == 'Request was throttled. Expected available in 45 seconds.':
                    sleep(60)
                    r = ProxyAPI().get_proxy_connection_info(token)
                    result = r.json()
            except KeyError as e:
                print("No throttling yet")
            try:
                selected_proxy_ip = result["results"][choice]["proxy_address"]
                selected_proxy_port = result["results"][choice]["port"]
            except KeyError as e:
                print("e:", e)
                print("error:", result)  # look whats on it, maybe something useful
                error = result["detail"]
                remaining_seconds = error[45:47]
                print("sleeping for " + remaining_seconds + " on proxy: " + str(choice))
                sleep(int(remaining_seconds))
                return selected_proxy_ip, selected_proxy_port
                # File "/home/rlm/Code/canadaAps/canadaAps/util/proxyTools.py", line 26, in get_proxy_ip
                # selected_proxy_ip = result["results"][choice]["proxy_address"]
                # KeyError: 'results'
        return selected_proxy_ip, selected_proxy_port

    @staticmethod
    def create_proxy_dict(ip, port):
        username = os.environ.get("username")
        password = os.environ.get("password")
        http_proxy_string = f"http://{username}:{password}@{ip}:{port}"
        # http_proxy_string = "http://" + str(ip) + ":" + str(port)
        # https_proxy_string = "https://" + str(proxy_ip) + ":" + str(proxy_port)
        proxy_dict = {"http": http_proxy_string, "https": http_proxy_string}
        return proxy_dict

    @staticmethod
    def confirm_public_ip_is_proxy_ip(proxy_dict, desired_ip_from_proxy):
        # token = os.environ.get("apikey")
        r, r2 = ProxyAPI().get_public_ip(proxy_dict)
        ip_is_correct = r.text == desired_ip_from_proxy and r2.text == desired_ip_from_proxy
        return ip_is_correct


def get_hardcoded_proxy_conn_info():
    # hardcode the list we'd get anyway to avoid requesting the list approx 5000x per scrape session
    return {'count': 10, 'next': None, 'previous': None, 'results': [
        {'id': 'd-782270686', 'username': username, 'password': password, 'proxy_address': '185.199.229.156',
         'port': 7492, 'valid': True, 'last_verification': '2023-01-28T14:22:42.276416-08:00', 'country_code': 'ES',
         'city_name': 'Las Rozas De Madrid', 'created_at': '2022-10-08T17:21:18.335739-07:00'},
        {'id': 'd-715009785', 'username': username, 'password': password, 'proxy_address': '185.199.228.220',
         'port': 7300, 'valid': True, 'last_verification': '2023-01-28T14:23:45.502755-08:00', 'country_code': 'ES',
         'city_name': 'Las Rozas De Madrid', 'created_at': '2022-08-16T11:22:03.306482-07:00'},
        {'id': 'd-715009786', 'username': username, 'password': password, 'proxy_address': '185.199.231.45',
         'port': 8382, 'valid': True, 'last_verification': '2023-01-28T14:22:20.492493-08:00', 'country_code': 'ES',
         'city_name': 'Las Rozas De Madrid', 'created_at': '2022-08-16T11:22:03.306482-07:00'},
        {'id': 'd-786570550', 'username': username, 'password': password, 'proxy_address': '188.74.210.207',
         'port': 6286, 'valid': True, 'last_verification': '2023-01-28T14:23:11.040817-08:00', 'country_code': 'IT',
         'city_name': 'Rome', 'created_at': '2022-10-12T06:03:47.268474-07:00'},
        {'id': 'd-788346827', 'username': username, 'password': password, 'proxy_address': '188.74.183.10',
         'port': 8279, 'valid': True, 'last_verification': '2023-01-28T14:23:05.822205-08:00', 'country_code': 'IT',
         'city_name': 'Rome', 'created_at': '2022-10-13T17:36:06.399382-07:00'},
        {'id': 'd-790788207', 'username': username, 'password': password, 'proxy_address': '188.74.210.21',
         'port': 6100, 'valid': True, 'last_verification': '2023-01-28T14:23:22.237701-08:00', 'country_code': 'IT',
         'city_name': 'Rome', 'created_at': '2022-10-15T19:43:03.176327-07:00'},
        {'id': 'd-791352933', 'username': username, 'password': password, 'proxy_address': '45.155.68.129',
         'port': 8133, 'valid': True, 'last_verification': '2023-01-28T14:21:59.792584-08:00', 'country_code': 'NL',
         'city_name': 'Haarlem', 'created_at': '2022-10-16T07:51:11.729889-07:00'},
        {'id': 'd-792703565', 'username': username, 'password': password, 'proxy_address': '154.95.36.199',
         'port': 6893, 'valid': True, 'last_verification': '2023-01-28T14:23:48.426109-08:00', 'country_code': 'ES',
         'city_name': 'Madrid', 'created_at': '2022-10-17T12:24:57.071829-07:00'},
        {'id': 'd-795974692', 'username': username, 'password': password, 'proxy_address': '45.94.47.66',
         'port': 8110, 'valid': True, 'last_verification': '2023-01-28T14:20:33.170061-08:00', 'country_code': 'NL',
         'city_name': 'Victoria', 'created_at': '2022-10-20T06:29:23.910490-07:00'},
        {'id': 'd-794115810', 'username': username, 'password': password, 'proxy_address': '144.168.217.88',
         'port': 8780, 'valid': True, 'last_verification': '2023-01-28T13:50:25.488643-08:00', 'country_code': 'US',
         'city_name': 'Piscataway', 'created_at': '2022-10-18T17:41:53.190116-07:00'}]}
