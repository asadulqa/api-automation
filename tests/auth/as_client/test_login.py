from src.utilities.request_utility import RequestsUtility
from src.data.static_data import data


def test_login():
    """
    Sending post request with correct credentials and making sure user identified
    and returned same user data point
    :return:
    """
    mail = data['client_user']['email']
    payload = {
        "email": mail,
        "password": data['client_user']['password']
    }
    r = RequestsUtility()
    res = r.post("auth/token/", payload=payload)
    print(res)
    assert res['user']['role'] == "client", "Client role does not match"
    assert res['user']['email'] == mail, f"Expected user mail is not found on response"
