# packaging
Alumet docker images and distro-specific packages

# Table of Contents
- [packaging](#packaging)
- [Table of Contents](#table-of-contents)
- [Create your own package](#create-your-own-package)
- [How to install ?](#how-to-install-)
- [How to uninstall](#how-to-uninstall)
- [What does the DEB do ?](#what-does-the-deb-do-)

When you're downloading the deb, use a compatible Unix system version.

| Version of Debian base OS | Version of libc 	|
|---------------------------|-----------------	|
| Debian 12   		          | glibc 2.35      	|
| Ubuntu 24.04.1 LTS        | glibc 2.3      	  |

# Create your own package

```bash
sudo dpkg --build <folder_to_package> <package.deb>
```

# How to install ? 

```bash
sudo dpkg -i <package_file.deb>
```
Or :
```bash
sudo apt install ./<package_file.deb>
```

# How to uninstall

List all installed Alumet package: 

```bash
dpkg -l alumet
```

Remove the correct Alumet package 
```bash
sudo dpkg -r alumet
```
Or :
```bash
sudo apt remove alumet
```

# What does the DEB do ? 

The DEB create a folder **alumet** inside the */var/lib/* folder. Here will be put the **alumet-config.toml** file which is the config file for Alumet by default. 
The RPM also put inside the */usr/bin/* folder the Alumet binary. As usually */usr/bin/* folder is in the path, you can just run Alumet like:

```bash
alumet-local-agent
```
