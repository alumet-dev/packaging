# Building the Images Locally

## Prerequisites

Do this first:

1. Clone the `alumet` repository and build an `alumet-agent` binary.
2. Build a [DEB](../deb/README.md) or [RPM](../rpm/README.md) package with the provided scripts. You can also download a pre-built package from [Alumet releases](https://github.com/alumet-dev/alumet/releases).
3. Install [podman](https://podman.io/) (or docker).

## Image Building

Prepare some environment variables and `cd` to the root directory of this repository.

As an example, we will prepare to tag the image with the _ghcr_ repository, which is used by the official Alumet releases.
This will make testing the image easier, in particular with Helm (see [Alumet Helm Charts](https://github.com/alumet-dev/helm-charts)). You can use something else, but you will need to adapt the tool that uses the image (if any − if you just want an image for yourself, do what you want :D).

We will use the DEB package and the Ubuntu 24.04 base image.

```sh
export PKG_VERSION=0.9.1-snapshot
export PKG_REVISION=1
export PKG_FILE=alumet-agent_0.9.1-snapshot-1_amd64.deb
export BASE_IMAGE=ubuntu_24.04
export IMG_REGISTRY=ghcr.io/alumet-dev # change this as needed
export TAG="$IMG_REGISTRY/alumet-agent:$PKG_VERSION-"$PKG_REVISION"_$BASE_IMAGE"
export TAG_LATEST="$IMG_REGISTRY/alumet-agent:latest"
```

Then, build the image by setting the relevant build arguments.

```sh
podman build -t $TAG -t $TAG_LATEST \
             --build-arg ALUMET_VERSION=$PKG_VERSION \
             --build-arg BUILDER_IMAGE=$BASE_IMAGE \
             --build-arg ARTIFACT_FILE=$PKG_FILE \
             -f docker/ubuntu/Dockerfile \
             .
```

Check that the image is available locally:

```sh
❯❯❯ podman image ls
REPOSITORY                          TAG                             IMAGE ID      CREATED         SIZE
ghcr.io/alumet-dev/alumet-agent     0.9.1-snapshot-1_ubuntu_24.04   be78752b44cf  2 minutes ago   157 MB
ghcr.io/alumet-dev/alumet-agent     latest                          be78752b44cf  2 minutes ago   157 MB
```
