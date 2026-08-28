# Windows Version Locker

A lightweight Python script that allows you to easily lock your Windows 11 version using official Windows Update registry policies, preventing unwanted automatic feature updates.

## Description
Windows Version Locker is a command-line tool designed for Windows 11 users who want to stay on a specific operating system version (e.g., `24H2`). By configuring the standard Windows Update registry keys (`TargetReleaseVersion`, `ProductVersion`, and `TargetReleaseVersionInfo`), this script locks your system to your chosen release version, giving you complete control over your updates.

## Features
* **Version Locking:** Pins your Windows 11 installation to any specified target release version.
* **Automatic Elevation:** Automatically checks for administrator privileges and prompts for elevation if needed.
* **Zero Dependencies:** Built purely with Python's standard libraries (`ctypes`, `os`, `sys`, `winreg`), meaning no external packages are required.

## Prerequisites
* Windows 11
* Python 3.x

## Usage
1. Download or clone the `WindowsVersionLocker.py` script.
2. Run the script using Python. 
3. Grant administrator privileges when the User Account Control (UAC) prompt appears.
4. Enter the desired Windows 11 version you wish to lock to (e.g., `24H2`) when prompted.
5. Restart your computer for the registry changes to take effect.
