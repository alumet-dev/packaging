# RPM usage <!-- omit in toc -->

This folder contains all necessary to package Alumet in RPM format. To know how
to use the associated Github action, please look at [this README](../docs/README.md).

## Table of Contents <!-- omit in toc -->

- [How to install ?](#how-to-install-)
  - [Install on RHEL like distribution](#install-on-rhel-like-distribution)
  - [Install on OpenSuze like distribution](#install-on-opensuze-like-distribution)
- [How to uninstall](#how-to-uninstall)
  - [Uninstall on RHEL like distribution](#uninstall-on-rhel-like-distribution)
  - [Uninstall on OpenSuze like distribution](#uninstall-on-opensuze-like-distribution)
- [List all installed Alumet package](#list-all-installed-alumet-package)
  - [List on RHEL like distribution](#list-on-rhel-like-distribution)
  - [List on OpenSuze like distribution](#list-on-opensuze-like-distribution)

When you're downloading the rpm, use a compatible version
particularly if you're not on fedora.

| Version of fedora | Version of glibc |
| ----------------- | ---------------- |
| Fedora Linux 42   | glibc 2.40       |
| Fedora Linux 41   | glibc 2.40       |
| Fedora Linux 40   | glibc 2.39       |
| ubi 8.3           | glibc 2.28       |
| ubi 9.5           | glibc 2.34       |

## How to install ?

### Install on RHEL like distribution

```bash
sudo dnf install --allow-unsigned-rpm ./file.rpm
```

### Install on OpenSuze like distribution

```bash
sudo zypper install --allow-unsigned-rpm ./file.rpm
```

## How to uninstall

### Uninstall on RHEL like distribution

```bash
sudo dnf remove <package>
```

### Uninstall on OpenSuze like distribution

```bash
sudo zypper remove <package>
```

## List all installed Alumet package

### List on RHEL like distribution

```bash
sudo dnf search alumet
```

### List on OpenSuze like distribution

```bash
sudo zypper search --installed-only -s -t package | grep -i alumet
```
