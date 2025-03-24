# Workflow usage <!-- omit in toc -->

## Table of Contents <!-- omit in toc -->

- [About version numbers](#about-version-numbers)
- [Workflows](#workflows)
  - [build\_rpm.yaml](#build_rpmyaml)
  - [build\_deb.yaml](#build_debyaml)

## About version numbers

Version numbers are "normalized" by the workflows.
In particular, hyphens `-` are replaced with tildes `~` so that a version number like `0.8.0-d89b24f` is turned into `0.8.0~d89b24f`, which is considered to be OLDER than `0.8.0`.

## Workflows

### build_rpm.yaml

Build an RPM package for specified architecture and version.

Example:

```yaml
jobs:
  rpm:
    uses: ./.github/workflows/build_rpm.yaml
    with:
      arch: x86_64
      version: 0.6.1
      release-version: 1
      tag: v0.5.0
```

When compiled for fedora 40 for x86_64 architecture, with this input, the resulting package will be `alumet-agent-0.6.1-1.fc40.x86_64.rpm`.

### build_deb.yaml

Build a DEB package.

Example:

```yaml
jobs:
  deb:
    uses: ./.github/workflows/build_deb.yaml
    with:
      arch: amd64
      version: 0.6.1
      revision: 1
      tag: v0.5.0
```
