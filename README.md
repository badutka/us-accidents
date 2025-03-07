# us_accidents
 
## Section 1: Setting up Airflow with WSL in Windows 10/11

* Useful Links:
    * [Apache Airflow Installation Guide](https://www.projectpro.io/article/airflow-tutorial-on-how-to-use-apache-airflow/920)
    * [WSL Installation Guide (MS)](https://learn.microsoft.com/en-us/windows/wsl/install)
    * [Guide for VS Code setup in WSL](https://code.visualstudio.com/docs/remote/wsl)
    * [Guide for setting up Git repo with GitHub Desktop in WSL](https://mruduljohn.medium.com/github-desktop-in-windows-subsystem-for-linux-wsl2-4589aa454100)
    * [Airflow docs, quick start](https://airflow.apache.org/docs/apache-airflow/stable/start.html)
    * [Some tips on running Airflow on WSL from Stack Overflow](https://stackoverflow.com/questions/72551825/installing-and-running-airflow-on-wsl)

### 1. Installing WSL

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

1. Make sure to update your distro. This should also install (latest) stable Python release:
```bash
sudo apt update
sudo apt upgrade -y
```

2. Execute the following command to install pip, venv, mysql lib and other.
```bash
sudo apt install -y python3-pip python3-venv libmysqlclient-dev libssl-dev libffi-dev
```
 
 3. Create Python virtual environment, in our case it's named `airflow-env`. This step can be done after creating or cloning repo, in case you want to create venv inside your project structure.
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

Alternatively to steps 6-7, you can run:
```bash
airflow standalone
```
This command initializes the database, creates a user, and starts all components.

### 3. Configuring VS Code that is installed in Windows to work with a code repository in WSL

Once you have WSL installed you can follow these steps (as per guide link):

1. Install Visual Studio Code on the Windows side (not in WSL).
2. Install the WSL extension in VS Code
3. Open a WSL terminal window (for instance by running `wsl -d Ubuntu` from Windows PowerShell, or just `wsl`.)
4. Navigate to a folder you'd like to open in VS Code in.
5. Type code . in the terminal. When doing this for the first time, you should see VS Code fetching components needed to run in WSL. This should only take a short while, and is only needed once.
6. After a moment, a new VS Code window will appear, and you'll see a notification that VS Code is opening the folder in WSL.
7. Once finished, you now see a WSL indicator in the bottom left corner, and you'll be able to use VS Code as you would normally.

Check out the link on VS Code setup, for alternative options and much more.

### 4. Making sure GitHub Desktop works with WSL repo
After Installing Git, GitHub Desktop and logging in with your GitHub account, you can follow the following steps.

1. Navigate to your WSL file system via the Linux icon in Windows Explorer.
2. Navigate to your project directory in WSL file system and copy the Path. The path would look something like this : (e.g., `\\wsl.localhost\Ubuntu\home\username\projectfolder\`)
3. To clone a new repo into your Linux subsystem: in GitHub Desktop, select `File` `->` `Clone a repository`.
4. Wen using `URL` tab, paste the copied path in the `Local Path`. Add the link of the repository you want to clone in `Repository URL` field. ALternatively, you can use `GitHub.com` that shows your repos already integrated with GitHub Desktop.
5. Select the `Clone` button to clone your favorite repository to your Linux Subsystem with GitHub Desktop integrated.

Check out the link with guide on GitHub setup in WSL, for more detailed walkthrough, screenshots and more.

### 5. Running airflow

To run the scheduler and web server again:
1. Initialize WSL again
2. Navigate to directory with your `airflow-env`
3. Activate you `airflow-venv`
4. Run the following commands:

```bash
airflow scheduler &
airflow webserver --port 8080 &
```