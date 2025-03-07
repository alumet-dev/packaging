# DEB Packaging

Alumet debian based system image package

# Create your own package

To create a .deb package file to ensure its compatibility with an operating system, you need to build the **Alumet** project on it. 
Run the *config.sh* script that downloading **Alumet** project sources on github ("https://github.com/alumet-dev/alumet"), 
extract and compile its content in a final binary according the targeted operating system version and distribution.

```bash
./packager.sh
```

# How to install ? 

```bash
sudo dpkg -i <package_file.deb>
```
Or with **apt** package manager :
```bash
sudo apt install ./<package_file.deb>
```

# How to uninstall

Remove the correct **Alumet** package :
```bash
sudo dpkg -r alumet
```
Or with **apt** package manager :
```bash
sudo apt remove alumet
```

# What does the DEB package do ? 

On Debian based operating system, the DEB create a folder **alumet** inside the */var/lib/alumet/* folder,
to put the *alumet-config.toml* file, which is the configuration file used for Alumet by default.
It also creating a daemon disable by default, but runnable and usable by the *systemd* services manager.
Finally, the package put the **Alumet** binary program in the */usr/lib/alumet* folder, and its runnable script in */usr/bin/*.

    alumet/
    |__ usr
    │   └── lib
    │       └── systemd
    │           └── system
    │               └── alumet.service
    ├── var
    |   └── lib
    │       └── alumet
    │           └── alumet-config.toml
    └── usr
        ├── bin
        │   └── alumet
        └── lib
            └── alumet
                └── alumet-agent

Finally, you can just run **Alumet** program like this :

```bash
alumet
```
