# Debian package

## Useful Resources for Maintainers

- [Debian Packaging Tutorial (slides)](https://www.debian.org/doc/manuals/packaging-tutorial/packaging-tutorial.en.pdf)
- [Debian Wiki - Packaging/Intro](https://wiki.debian.org/Packaging/Intro)
- [Debchange Manual](https://manpages.debian.org/bookworm/devscripts/dch.1.html) - Tool for maintenance of the debian/changelog file
- [Debhelper Manual](https://manpages.debian.org/bullseye/debhelper/debhelper.7.en.html) - Tool suite to help you build a Debian package
- [dpkg-buildpackage Manual](https://manpages.debian.org/bookworm/dpkg-dev/dpkg-buildpackage.1.fr.html) - Build binary or source packages
- [Debian Policy Manual](https://www.debian.org/doc/debian-policy/index.html) - Policy  Requirements for the Debian distribution
  - In particular: [Chapter 8: Shared libraries](https://www.debian.org/doc/debian-policy/ch-sharedlibs.html) - Explains why the `Depends` field in `debian/control` uses `${shlibs:Depends}`

## Manually building the package

<!-- markdownlint-disable MD029 -->

Before starting, make sure that you have installed the `devscripts` package.

1. Build alumet-agent and copy the binary to the `deb` folder (next to `debian`).
2. Set the version of the package.

```sh
export PKG_VERSION=0.1.2
export PKG_REVISION=1
```

3. In the `deb` folder, run `build-package.sh`.
4. That's it! The package is produced in the _parent_ directory.

## Testing the workflow locally

```sh
act --artifact-server-path=/tmp/artifacts workflow_dispatch --matrix debian:12
```

TIP: once you have run `act` once, add the `--action-offline-mode` flag to avoid pulling images again.

NOTE: GitHub actions such as `checkout` require a recent version of node, which is not in the repositories of old Debian versions. Unless you install nodejs on your machine and mount it in the image, you cannot use `debian:11` with `act`.
