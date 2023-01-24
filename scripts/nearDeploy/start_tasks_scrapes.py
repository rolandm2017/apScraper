import requests

queuing_url = "http://127.0.01:8080/queue_scrapes"

response = requests.get(queuing_url)

current_date = ""

log_file_name = "quuee_script_output_" + current_date + ".txt"

with open(log_file_name, "w") as f:
    if response.status_code == 200:
        f.write("success")
        f.write("\n===\n===\n\n\n")
    else:
        f.write(response.text)
        f.write("\n===\n===\n\n\n")


# ### activate scrapers

def make_activation_url(port):
    return f"http://127.0.01:{port}/activate"


def activate_provider(provider, port):
    activation_url = make_activation_url(5000)
    payload = {"provider": provider}
    response = requests.post(activation_url, data=payload)
    return response


response_rent_canada = activate_provider("rentCanada", 5000)
response_rent_faster = activate_provider("rentFaster", 5001)
response_rent_seeker = activate_provider("rentSeeker", 5002)


def log_response(provider_response, log_file_name_param, provider_name):
    with open(log_file_name_param, "w") as f:
        if provider_response.status_code == 200:
            f.write("successful activation for " + provider_name)
            f.write("\n===\n===\n\n\n")
        else:
            f.write("\n** ** **\nfailure for " + provider_name)
            f.write("\n** ** **")
            f.write(provider_response.text)
            f.write("\n===\n===\n\n\n")

# activation_url = make_activation_url(5001)
#
# payload = {"provider": "rentFaster"}
# response = requests.post(activation_url, data=payload)
