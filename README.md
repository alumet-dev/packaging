# packaging

Alumet docker images and distro-specific packages

# Table of Contents

- [packaging](#packaging)
- [Table of Contents](#table-of-contents)
- [How to install ?](#how-to-install-)
- [How to uninstall](#how-to-uninstall)
- [What does the RPM do ?](#what-does-the-rpm-do-)
- [Use the reusable workflow to build RPMs](#use-the-reusable-workflow-to-build-rpms)
  - [build\_rpm.yaml](#build_rpmyaml)
    - [Inputs](#inputs)
    - [Example of usage](#example-of-usage)

When you're downloading the rpm, use a compatible version
particularly if you're not on fedora.

| Version of fedora   | Version of glibc  |
|-------------------  |-----------------  |
| Fedora Linux 42     | glibc 2.40        |
| Fedora Linux 41     | glibc 2.40        |
| Fedora Linux 40     | glibc 2.39        |
| Fedora ubi 8.3        | glibc 2.28        |
| Fedora Linux 9.5    | glibc 2.34        |

# How to install ?

```bash
sudo rpm -i <rpm file>
sudo -E zypper install --allow-unsigned-rpm temp_rpm/alumet-agent-0.6.1-1.fedora.40.x86_64.rpm
```

# How to uninstall

List all installed Alumet package:

```bash
rpm -qa | grep -i alumet
```

Remove the correct Alumet package

```bash
sudo rpm -e <package>
```

# What does the RPM do ?

Content of the RPM (using: **rpm -qlp file.rpm**)

```bash
/etc/alumet
/etc/alumet/alumet-config.toml
/usr/bin/alumet-agent
/usr/lib/.build-id
/usr/lib/.build-id/43
/usr/lib/.build-id/43/b1368a4c6879892cb3c8ae663d68b8640ff458
/usr/lib/alumet-agent
/usr/lib/systemd/system/alumet.service
```

# Use the reusable workflow to build RPMs

## build_rpm.yaml

Build RPM for specified architecture and version
  
### Inputs

|          Name           |   Type   | Default value | Required |
| :---------------------: | :------: | :-----------: | :------: |
|   target-architecture   |  string  |     true      |    ✅    |
|   build-version         |  string  |     true      |    ✅    |
|   release-version       |  string  |     true      |    ✅    |

### Example of usage

```yaml
jobs:
  rpm:
    uses: ./.github/workflows/build_rpm.yaml
    with:
      target-architecture: x86_64
      build-version: 0.6.1
      release-version: 1
```

When compiled for fedora 40 for x86_64 architecture, with this input, the resulting package will be
`alumet-agent-0.6.1-1.fedora.40.x86_64.rpm`
