# RPM usage <!-- omit in toc -->

This folder contains all the necessary to package Alumet in RPM format.
To know how to use the associated Github action, please look at [this README](../docs/README.md).

## Table of Contents <!-- omit in toc -->

- [Manually building the package](#manually-building-the-package)
  - [/usr/lib vs /usr/lib64](#usrlib-vs-usrlib64)
- [Installing the package](#installing-the-package)
  - [Install on RHEL like distribution](#install-on-rhel-like-distribution)
  - [Install on OpenSuze like distribution](#install-on-opensuze-like-distribution)
- [How to uninstall](#how-to-uninstall)
  - [Uninstall on RHEL like distribution](#uninstall-on-rhel-like-distribution)
  - [Uninstall on OpenSuze like distribution](#uninstall-on-opensuze-like-distribution)
- [List all installed Alumet package](#list-all-installed-alumet-package)
  - [List on RHEL like distribution](#list-on-rhel-like-distribution)
  - [List on OpenSuze like distribution](#list-on-opensuze-like-distribution)

When downloading the rpm, use a compatible version, particularly if you're not on fedora.

| Version of fedora | Version of glibc |
| ----------------- | ---------------- |
| Fedora Linux 42   | glibc 2.40       |
| Fedora Linux 41   | glibc 2.40       |
| Fedora Linux 40   | glibc 2.39       |
| ubi 8.3           | glibc 2.28       |
| ubi 9.5           | glibc 2.34       |

## Manually building the package

1. Build alumet-agent and copy the binary to the `SOURCES` folder.
2. Set the version of the package.
```sh
export PKG_VERSION=0.1.2
export PKG_RELEASE=1
```
3. Run `rpmbuild` in the `rpm` folder with the following arguments:
```sh
export TOPDIR="$(pwd)/build"
export ARCH=x86_64
export OS_NAME=$(grep '^ID=' "/etc/os-release" | cut -d'=' -f2 | tr -d '"')
rpmbuild -bb -vv \
  --define "_topdir $TOPDIR" \
  --define "_sourcedir $(pwd)/SOURCES" \
  --define "version $PKG_VERSION" \
  --define "release $PKG_RELEASE" \
  --define "osr $OS_NAME" \
  --define "arch $ARCH" \
  SPECS/alumet.spec
```
4. The package is produced in `${TOPDIR}/${ARCH}/RPMS`.

### /usr/lib vs /usr/lib64

By default, RHEL-based distributions use /usr/lib64 on 64-bits system.
To use /usr/lib instead, redefine the `%{_libdir}` macro by adding the following argument:
```
--define "_libdir /usr/lib"
```

## Installing the package

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
sudo dnf search --installed alumet
```

### List on OpenSuze like distribution

```bash
sudo zypper search --installed-only -s -t package | grep -i alumet
```
