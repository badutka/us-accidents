# us_accidents
 
## Section 1: Setting up Airflow with WSL in Windows 10/11

### 1. Installing WSL

* Useful Links:

    * [Apache Airflow Installation Guide](https://www.projectpro.io/article/airflow-tutorial-on-how-to-use-apache-airflow/920)
    * [WSL Installation Guide (MS)](https://learn.microsoft.com/en-us/windows/wsl/install)

1. We can start by running Windows PowerShell as administrator and executing the command below:

```bash
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

2. To install a specific Linux distro (e.g. Ubuntu, in my case) you can run:
```bash
wsl --install -d Ubuntu
```

3. You can see if your distro appears as functional in the WSL list:
```bash
wsl --list --verbose
```

4. Then you can run your linux (This process will fail if virtualization is not enabled in bios):
```bash
wsl -d Ubuntu
```
In case you did not enable virtualization in your bios settings and you had to reboot, just run the installation again to create a user and initialize Linux (step 2).

5. In case you want to delete the current distro installation:
```bash
wsl --unregister Ubuntu
```

### 2. Installing Python and Airflow inside WSL

1. Make sure to update your distro:
```bash
sudo apt update
sudo apt upgrade -y
```

2. Execute the following command to install python, and a few additional things we will need later.
```bash
sudo apt install -y python3-pip python3-venv libmysqlclient-dev libssl-dev libffi-dev
```
 
 3. Create Python virtual environment, in our case it's named `airflow-env`.
```bash
python3 -m venv airflow-env
```

4. Activate the virtual environment
```bash
source airflow-env/bin/activate
```

5. Install Apache Airflow in the virtual environment
```bash
pip install apache airflow
```

6. Initialize database
```bash
airflow db init
```

7. Run Airflow
```bash
airflow webserver --port 8080
```

2. Creating ariflow venv (this step can be done after creating or cloning repo)

3. configuring VS Code that is installed in Windows to work with a code repository in WSL

https://code.visualstudio.com/docs/remote/wsl

4. Making sure GitHub Desktop works with WSL repo

https://mruduljohn.medium.com/github-desktop-in-windows-subsystem-for-linux-wsl2-4589aa454100

5. 
running scheduler and web server:
```bash
airflow scheduler &
airflow webserver --port 8080 &
```