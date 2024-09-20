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


When you're downloading the rpm, use a compatible version particularly if you're not on fedora.

| Version of fedora 	| Version of glibc 	|
|-------------------	|-----------------	|
| Fedora Linux 42   	| glibc 2.40      	|
| Fedora Linux 41   	| glibc 2.40      	|
| Fedora Linux 40   	| glibc 2.39      	|
| Fedora ubi 8.3   	    | glibc 2.28      	|
| Fedora Linux 9.5   	| glibc 2.34      	|

# How to install ? 

```bash
sudo rpm -i <rpm file>
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
/usr/bin/alumet-local-agent
/usr/lib/.build-id
/usr/lib/.build-id/1e
/usr/lib/.build-id/1e/8470891dc74ab9381d5dc4d37e4a4da9cd9d26
/usr/lib/alumet-local-agent_bin
/var/lib/alumet
```

# Use the reusable workflow to build RPMs

## build_rpm.yaml

Build RPM for specified architecture and version
  
### Inputs

|          Name           |   Type   | Default value | Required |
| :---------------------: | :------: | :-----------: | :------: |
|   target-architecture   |  string  |     true      |    ✅    |
|   build-version         |  string  |     true      |    ✅    |


### Example of usage

```yaml
jobs:
  rpm:
    uses: ./.github/workflows/build_rpm.yaml
    with:
      target-architecture: x86_64
      build-version: 0.6.1
```