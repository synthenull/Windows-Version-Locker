# Windows Version Locker

A lightweight Python script that allows you to easily lock your Windows 11 version using official Windows Update registry policies, preventing unwanted automatic feature updates.

## Description
Windows Version Locker is a command-line tool designed for Windows 11 users who want to stay on a specific operating system version (e.g., `24H2`)[cite: 1]. By configuring the standard Windows Update registry keys (`TargetReleaseVersion`, `ProductVersion`, and `TargetReleaseVersionInfo`), this script locks your system to your chosen release version, giving you complete control over your updates[cite: 1].

## Features
* **Version Locking:** Pins your Windows 11 installation to any specified target release version[cite: 1].
* **Automatic Elevation:** Automatically checks for administrator privileges and prompts for elevation if needed[cite: 1].
* **Zero Dependencies:** Built purely with Python's standard libraries (`ctypes`, `os`, `sys`, `winreg`), meaning no external packages are required[cite: 1].

## Prerequisites
* Windows 11
* Python 3.x

## Usage
1. Download or clone the `WindowsVersionLocker.py` script[cite: 1].
2. Run the script using Python. 
3. Grant administrator privileges when the User Account Control (UAC) prompt appears[cite: 1].
4. Enter the desired Windows 11 version you wish to lock to (e.g., `24H2`) when prompted[cite: 1].
5. Restart your computer for the registry changes to take effect[cite: 1].

## License
Distributed under the MIT License. See `LICENSE` for more information.

---
*Developed by [synthenull](https://github.com/synthenull)[cite: 1].*
