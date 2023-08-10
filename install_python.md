
# [Step 1 — Downloading the Python Installer](https://www.digitalocean.com/community/tutorials/install-python-windows-10#step-1-downloading-the-python-installer)[](https://www.digitalocean.com/community/tutorials/install-python-windows-10#step-1-downloading-the-python-installer)

1.  Go to the official  [Python download page for Windows](https://www.python.org/downloads/windows/).
    
2.  Find a stable Python 3 release. This tutorial was tested with Python version 3.10.10.
    
3.  Click the appropriate link for your system to download the executable file:  **Windows installer (64-bit)**  or  **Windows installer (32-bit)**.
    
    ![Download Python Installer](https://deved-images.nyc3.digitaloceanspaces.com/CONTINT-1526%2Fpy_download.png)
    

# [Step 2 — Running the Executable Installer](https://www.digitalocean.com/community/tutorials/install-python-windows-10#step-2-running-the-executable-installer)[](https://www.digitalocean.com/community/tutorials/install-python-windows-10#step-2-running-the-executable-installer)

1.  After the installer is downloaded, double-click the  `.exe`  file, for example  `python-3.10.10-amd64.exe`, to run the Python installer.
    
2.  Select the  **Install launcher for all users**  checkbox, which enables all users of the computer to access the Python launcher application.
    
3.  Select the  **Add python.exe to PATH**  checkbox, which enables users to launch Python from the command line.
    
    ![Customize Installation](https://deved-images.nyc3.digitaloceanspaces.com/CONTINT-1526%2Fpy-installer-customize.png)
    
4.  If you’re just getting started with Python and you want to install it with default features as described in the dialog, then click  **Install Now**  and go to  [Step 4 - Verify the Python Installation](https://www.digitalocean.com/community/tutorials/install-python-windows-10#step-4-verify-the-python-installation). To install other optional and advanced features, click  **Customize installation**  and continue.
    
5.  The  **Optional Features**  include common tools and resources for Python and you can install all of them, even if you don’t plan to use them.
    
    ![Python Optional Features](https://deved-images.nyc3.digitaloceanspaces.com/CONTINT-1526%2Fpy-installer-optional.png)
    
    Select some or all of the following options:
    
    -   **Documentation**: recommended
    -   **pip**: recommended if you want to install other Python packages, such as NumPy or pandas
    -   **tcl/tk and IDLE**: recommended if you plan to use IDLE or follow tutorials that use it
    -   **Python test suite**: recommended for testing and learning
    -   **py launcher**  and  **for all users**: recommended to enable users to launch Python from the command line
6.  Click  **Next**.
    
7.  The  **Advanced Options**  dialog displays.
    
    ![Python Advanced Options](https://deved-images.nyc3.digitaloceanspaces.com/CONTINT-1526%2Fpy-installer-advanced.png)
    
    Select the options that suit your requirements:
    
    -   **Install for all users**: recommended if you’re not the only user on this computer
    -   **Associate files with Python**: recommended, because this option associates all the Python file types with the launcher or editor
    -   **Create shortcuts for installed applications**: recommended to enable shortcuts for Python applications
    -   **Add Python to environment variables**: recommended to enable launching Python
    -   **Precompile standard library**: not required, it might down the installation
    -   **Download debugging symbols**  and  **Download debug binaries**: recommended only if you plan to create C or C++ extensions
    
    Make note of the Python installation directory in case you need to reference it later.
    
8.  Click  **Install**  to start the installation.
    
9.  After the installation is complete, a  **Setup was successful**  message displays.
    
    ![Python setup was successful](https://deved-images.nyc3.digitaloceanspaces.com/CONTINT-1526%2Fpy-installer-success.png)
    

# [Step 3 — Adding Python to the Environment Variables (optional)](https://www.digitalocean.com/community/tutorials/install-python-windows-10#step-3-adding-python-to-the-environment-variables-optional)[](https://www.digitalocean.com/community/tutorials/install-python-windows-10#step-3-adding-python-to-the-environment-variables-optional)

Skip this step if you selected  **Add Python to environment variables**  during installation.

If you want to access Python through the command line but you didn’t add Python to your environment variables during installation, then you can still do it manually.

Before you start, locate the Python installation directory on your system. The following directories are examples of the default directory paths:

-   `C:\Program Files\Python310`: if you selected  **Install for all users**  during installation, then the directory will be system wide
-   `C:\Users\Sammy\AppData\Local\Programs\Python\Python310`: if you didn’t select  **Install for all users**  during installation, then the directory will be in the Windows user path

Note that the folder name will be different if you installed a different version, but will still start with  `Python`.

1.  Go to  **Start**  and enter  `advanced system settings`  in the search bar.
    
2.  Click  **View advanced system settings**.
    
3.  In the  **System Properties**  dialog, click the  **Advanced**  tab and then click  **Environment Variables**.
    
4.  Depending on your installation:
    
    -   If you selected  **Install for all users**  during installation, select  **Path**  from the list of  **System Variables**  and click  **Edit**.
    -   If you didn’t select  **Install for all users**  during installation, select  **Path**  from the list of  **User Variables**  and click  **Edit**.
5.  Click  **New**  and enter the Python directory path, then click  **OK**  until all the dialogs are closed.
    

## [Step 4 — Verify the Python Installation](https://www.digitalocean.com/community/tutorials/install-python-windows-10#step-4-verify-the-python-installation)[](https://www.digitalocean.com/community/tutorials/install-python-windows-10#step-4-verify-the-python-installation)

You can verify whether the Python installation is successful either through the command line or through the Integrated Development Environment (IDLE) application, if you chose to install it.

Go to  **Start**  and enter  `cmd`  in the search bar. Click  **Command Prompt**.

Enter the following command in the command prompt:

```
python --version

```

An example of the output is:

```
Output
Python 3.10.10
```

Source: [Digital Ocean](https://www.digitalocean.com/community/tutorials/install-python-windows-10)
