import subprocess

def run(domain):
    try:
        return subprocess.check_output(["whatweb", domain], stderr=subprocess.DEVNULL).decode()
    except Exception as e:
        return f"Error: {e}"
