# Workflow usage <!-- omit in toc -->

## Table of Contents <!-- omit in toc -->

- [Use the reusable workflow to build RPMs](#use-the-reusable-workflow-to-build-rpms)
  - [build\_rpm.yaml](#build_rpmyaml)
    - [Inputs](#inputs)
    - [Example of usage](#example-of-usage)

## Use the reusable workflow to build RPMs

### build_rpm.yaml

Build RPM for specified architecture and version
  
#### Inputs

|        Name         |  Type  | Default value | Required |
| :-----------------: | :----: | :-----------: | :------: |
| target-architecture | string |     true      |    ✅    |
|    build-version    | string |     true      |    ✅    |
|   release-version   | string |     true      |    ✅    |
|         tag         | string |     '  '      |    ❌    |

#### Example of usage

```yaml
jobs:
  rpm:
    uses: ./.github/workflows/build_rpm.yaml
    with:
      target-architecture: x86_64
      build-version: 0.6.1
      release-version: 1
      tag: v0.5.0
```

When compiled for fedora 40 for x86_64 architecture, with this input, the resulting package will be
`alumet-agent-0.6.1-1.fedora.40.x86_64.rpm`
