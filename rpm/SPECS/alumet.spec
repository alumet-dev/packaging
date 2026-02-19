%global debug_package %{nil}
%define _build_name_fmt %%{ARCH}/%%{NAME}-%%{VERSION}-%%{RELEASE}.%{osr}.%%{ARCH}.rpm

Name:      alumet-agent
Version:   %{version}
Release:   %{release}
Summary:   Alumet agent, a tool for measuring energy and performance
License:   EUPL-1.2
Url:       https://github.com/alumet-dev/alumet
BuildArch: %{arch}

BuildRequires:  openssl-devel >= 3.0.0

Requires: glibc >= 2.2.5
Requires: openssl >= 3.0.0
Requires: libcap

%description
Customizable and efficient tool for measuring the energy consumption and performance metrics of software on HPC, Cloud and Edge devices.

%prep
echo prep
cp %{_sourcedir}/* %{_builddir}/

%build
echo build
cd "%{_builddir}"
ALUMET_CONFIG=alumet-config.toml ./alumet-agent --plugins csv,perf,procfs,socket-control config regen
cd -

%install
ls -al %{_builddir}/
install -D -m 0755 "%{_builddir}/alumet-agent"          "%{buildroot}%{_libdir}/alumet-agent"
install -D -m 0755 "%{_builddir}/alumet-agent-launcher" "%{buildroot}%{_bindir}/alumet-agent"
install -D -m 0644 "%{_builddir}/alumet.service"        "%{buildroot}%{_libdir}/systemd/system/alumet.service"
install -D -m 0644 "%{_builddir}/alumet-config.toml"    "%{buildroot}%{_sysconfdir}/alumet/alumet-config.toml"
chmod 777 %{buildroot}%{_sysconfdir}/alumet

%files
%{_bindir}/alumet-agent
%{_libdir}/alumet-agent
%{_libdir}/systemd/system/alumet.service
%dir %{_sysconfdir}/alumet/
%{_sysconfdir}/alumet/alumet-config.toml

%post
KERNEL_VERSION=$(uname -r)
KERNEL_MAJOR=$(echo "$KERNEL_VERSION" | cut -d'.' -f1)
KERNEL_MINOR=$(echo "$KERNEL_VERSION" | cut -d'.' -f2)

# Check for correct integer value
if ! [[ "$KERNEL_MAJOR" =~ ^[0-9]+$ ]] || ! [[ "$KERNEL_MINOR" =~ ^[0-9]+$ ]]; then
    echo "Error: KERNEL_MAJOR or KERNEL_MINOR is not a valid integer."
    echo "KERNEL_MAJOR: $KERNEL_MAJOR; KERNEL_MINOR: $KERNEL_MINOR"
    exit 1  # Exit or handle as needed
fi

# Add capabilities to alumet binary:
# - if Linux >= 5.8, CAP_SYS_NICE, CAP_SYS_PTRACE and CAP_PERMON
# - else, CAP_SYS_NICE, CAP_SYS_PTRACE and CAP_SYS_ADMIN
if [ "$KERNEL_MAJOR" -gt 5 ] || { [ "$KERNEL_MAJOR" -eq 5 ] && [ "$KERNEL_MINOR" -ge 8 ]; }; then
    setcap 'cap_perfmon=ep cap_sys_nice=ep cap_sys_ptrace=ep' %{_exec_prefix}/lib/alumet-agent
else
    setcap 'cap_sys_admin=ep cap_sys_nice=ep cap_sys_ptrace=ep' %{_exec_prefix}/lib/alumet-agent
fi

%changelog
* Wed Sep 18 2024 Cyprien cyprien.pelisse-verdoux@eviden.com - 0.0.1
- Initial package
