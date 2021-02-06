import subprocess

subprocess.call("sudo systemctl restart firmwared.service",shell=True)
subprocess.call("sudo pkill -f dragon-prog",shell=True)
subprocess.call("pkill -f roslaunch",shell=True)
subprocess.call("pkill -f gzserver",shell=True)
subprocess.call("pkill -f gzclient",shell=True)
ret = subprocess.check_output(["fdc","ping"]).decode("utf-8")
if "PONG" in ret:
    print("Firmwared Ready")
else:
    print("[ERROR] Firmwared not running")


