# Install Langflow | Langflow Documentation

- Get started
- Install Langflow

On this page# Install Langflow

[data-ch-theme="github-dark"] {  --ch-t-colorScheme: dark;--ch-t-foreground: #c9d1d9;--ch-t-background: #0d1117;--ch-t-lighter-inlineBackground: #0d1117e6;--ch-t-editor-background: #0d1117;--ch-t-editor-foreground: #c9d1d9;--ch-t-editor-lineHighlightBackground: #6e76811a;--ch-t-editor-rangeHighlightBackground: #ffffff0b;--ch-t-editor-infoForeground: #3794FF;--ch-t-editor-selectionBackground: #264F78;--ch-t-focusBorder: #1f6feb;--ch-t-tab-activeBackground: #0d1117;--ch-t-tab-activeForeground: #c9d1d9;--ch-t-tab-inactiveBackground: #010409;--ch-t-tab-inactiveForeground: #8b949e;--ch-t-tab-border: #30363d;--ch-t-tab-activeBorder: #0d1117;--ch-t-editorGroup-border: #30363d;--ch-t-editorGroupHeader-tabsBackground: #010409;--ch-t-editorLineNumber-foreground: #6e7681;--ch-t-input-background: #0d1117;--ch-t-input-foreground: #c9d1d9;--ch-t-input-border: #30363d;--ch-t-icon-foreground: #8b949e;--ch-t-sideBar-background: #010409;--ch-t-sideBar-foreground: #c9d1d9;--ch-t-sideBar-border: #30363d;--ch-t-list-activeSelectionBackground: #6e768166;--ch-t-list-activeSelectionForeground: #c9d1d9;--ch-t-list-hoverBackground: #6e76811a;--ch-t-list-hoverForeground: #c9d1d9; }Langflow can be installed in multiple ways:

- Langflow Desktop (Recommended): Download and install the standalone desktop application for the least complicated setup experience.
This option includes dependency management and facilitated upgrades.
- Docker: Pull and run the Langflow Docker image to start a Langflow container and run Langflow in isolation.
- Python package: Install and run the Langflow OSS Python package.
This option offers more control over the environment, dependencies, and versioning.
- Install from source: Use this option if you want to contribute to the Langflow codebase or documentation.

## Install and run Langflow Desktop​

Langflow Desktop is a desktop version of Langflow that simplifies dependency management and upgrades.
However, some features aren't available for Langflow Desktop, such as the Shareable Playground and Voice Mode.

- macOS
- Windows

Langflow Desktop requires macOS 13 or later.

1. Navigate to Langflow Desktop.
2. Click Download Langflow, enter your contact information, and then click Download.
3. Mount and install the Langflow application.
4. When the installation completes, open the Langflow application, and then create your first flow with the Quickstart.

warningIf you are upgrading Langflow Desktop on Windows, don't use the in-app update feature to upgrade to Langflow version 1.6.0.
For more information, see Known issues for 1.6.0.

1. Navigate to Langflow Desktop.
2. Click Download Langflow, enter your contact information, and then click Download.
3. Open the File Explorer, and then navigate to Downloads.
4. Double-click the downloaded .msi file, and then use the install wizard to install Langflow Desktop.
tipWindows installations of Langflow Desktop require a C++ compiler that may not be present on your system. If you receive a C++ Build Tools Required! error, follow the on-screen prompt to install Microsoft C++ Build Tools, or install Microsoft Visual Studio.
5. When the installation completes, open the Langflow application, and then create your first flow with the Quickstart.

For upgrade information, see the Release notes.

To manage dependencies in Langflow Desktop, see Install custom dependencies in Langflow Desktop.

## Install and run Langflow with Docker​

You can use the Langflow Docker image to start a Langflow container.
For more information, see Deploy Langflow on Docker.

1. Install and start Docker.
2. Pull the latest Langflow Docker image and start it:
_10docker run -p 7860:7860 langflowai/langflow:latest
3. To access Langflow, navigate to http://localhost:7860/.
4. Create your first flow with the Quickstart.

## Install and run the Langflow OSS Python package​

1. Make sure you have the required dependencies and infrastructure:
Python
macOS and Linux: Version 3.10 to 3.13
Windows: Version 3.10 to 3.12
uv
Sufficient infrastructure:
Minimum: Dual-core CPU and 2 GB RAM
Recommended: Multi-core CPU and at least 4 GB RAM
Browser:
Google Chrome is recommended but not required
2. Create a virtual environment with uv.
Need help with virtual environments?Virtual environments ensure Langflow is installed in an isolated, fresh environment.
To create a new virtual environment, do the following.Linux or macOSWindows
Navigate to where you want your virtual environment to be created, and then create it with uv:
_10uv venv VENV_NAME
Replace VENV_NAME with a name for your virtual environment.
Start the virtual environment:
_10source VENV_NAME/bin/activate
Your shell's prompt changes to display that you're currently working in a virtual environment:
_10(VENV_NAME) ➜  langflow git:(main) ✗
To deactivate the virtual environment and return to your regular shell, type deactivate.
When activated, the virtual environment temporarily modifies your PATH variable to prioritize packages installed within the virtual environment.
To avoid conflicts with other projects, it's a good idea to deactivate your virtual environment when you're done working in it.
To delete the virtual environment, type rm -rf VENV_NAME.
This completely removes the virtual environment directory and its contents.
Navigate to where you want your virtual environment to be created, and create it with uv.
_10uv venv VENV_NAME
Replace VENV_NAME with a name for your virtual environment.
Start the virtual environment:
_10VENV_NAME\Scripts\activate
Your shell's prompt changes to display that you're currently working in a virtual environment:
_10(VENV_NAME) PS C:/users/username/langflow-dir>
To deactivate the virtual environment and return to your regular shell, type deactivate.
When activated, the virtual environment temporarily modifies your PATH variable to prioritize packages installed within the virtual environment.
To avoid conflicts with other projects, it's a good idea to deactivate your virtual environment when you're done working in it.
To delete the virtual environment, type Remove-Item VENV_NAME.
This completely removes the virtual environment directory and its contents.
3. In your virtual environment, install Langflow:
_10uv pip install langflow
To install a specific version of the Langflow package, add the required version to the command, such as uv pip install langflow==1.4.22.
Reinstall or upgrade LangflowTo reinstall Langflow and all of its dependencies, run uv pip install langflow --force-reinstall.To upgrade Langflow to the latest version, run uv pip install langflow -U.
However, the Langflow team recommends taking steps to backup your existing installation before you upgrade Langflow.
For more information, see Prepare to upgrade.
4. Start Langflow:
_10uv run langflow run
It can take a few minutes for Langflow to start.
5. To confirm that a local Langflow instance is running, navigate to the default Langflow URL http://127.0.0.1:7860.
6. Create your first flow with the Quickstart.

For upgrade information, see the Release notes.

For information about optional dependency groups and support for custom dependencies to extend Langflow OSS functionality, see Install custom dependencies.

## Next steps​

- Quickstart: Build and run your first flow in minutes.
- Build flows: Learn about building flows.
- Troubleshoot Langflow: Get help with common Langflow install and startup issues.
