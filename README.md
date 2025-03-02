# us_accidents
 
1. Installing WSL

https://www.projectpro.io/article/airflow-tutorial-on-how-to-use-apache-airflow/920

https://learn.microsoft.com/en-us/windows/wsl/install

We can start bu running Windows PowerShell as administrator

```bash
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

Installing a specific linux distro:
```bash
wsl --install -d Ubuntu
```

You can see if your distro appears as functional in the WSL list:
```bash
wsl --list --verbose
```

You can run your linux:
```bash
wsl -d Ubuntu
```

In case you want to delete the current distro installation:
```bash
wsl --unregister Ubuntu
```

In case you did not turn virtualization and you had to reboot, just run the installation again to create a user and initialize linux:
```bash
wsl --install -d Ubuntu
```

THEN

```bash
sudo apt update
sudo apt upgrade -y
```

```bash
sudo apt install -y python3-pip python3-venv libmysqlclient-dev libssl-dev libffi-dev
```
 
```bash
python3 -m venv airflow-env
```

```bash
source airflow-env/bin/activate
```

```bash
pip install apache airflow
```

```bash
airflow db init
```

```bash
airflow webserver --port 8080
```
