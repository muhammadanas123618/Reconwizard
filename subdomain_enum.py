import requests

def run(domain):
    subs = set()
    try:
        crt_resp = requests.get(f"https://crt.sh/?q=%25.{domain}&output=json", timeout=10)
        if crt_resp.status_code == 200:
            for entry in crt_resp.json():
                name = entry['name_value']
                subs.update(name.split('\n'))
    except Exception:
        pass
    return sorted(subs)
