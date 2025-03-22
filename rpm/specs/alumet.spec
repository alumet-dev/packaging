%global debug_package %{nil}
%define _build_name_fmt %%{ARCH}/%%{NAME}-%%{VERSION}-%%{RELEASE}.%{osr}.%%{ARCH}.rpm


Name:           alumet-agent
Version:        %{version}
Release:        %{release}
Summary:        A tool for measuring the energy consumption and performance metrics
License:        EUPL-1.2
Url:            https://github.com/alumet-dev/alumet
Source:         %{name}.tar.gz
BuildArch:      %{arch}

BuildRequires:  openssl-devel >= 3.0.0

Requires: glibc >= 2.2.5
Requires: openssl >= 3.0.0
Requires: libcap
 
%description
Customizable and efficient tool for measuring the energy consumption and performance metrics of software on HPC, Cloud and Edge devices. 

%prep
%autosetup -n alumet
 
%build
mkdir -p %{_builddir}/bin/
cp packaging/rpm/alumet-agent %{_builddir}/alumet-agent
cp packaging/rpm/alumet.service %{_builddir}/alumet.service
cd %{_builddir}/alumet/alumet/agent
CARGO_TARGET_DIR=%{_builddir}/bin/ ALUMET_AGENT_RELEASE=true cargo build --release -p alumet-agent --bins --all-features
ALUMET_CONFIG=%{_builddir}/alumet-config.toml %{_builddir}/bin/release/alumet-agent --plugins csv,perf,procfs,socket-control config regen 

%install
mkdir -p %{buildroot}%{_exec_prefix}/lib/
mkdir -p %{buildroot}%{_exec_prefix}/bin/
install -D -m 0755 "%{_builddir}/bin/release/alumet-agent" "%{buildroot}%{_exec_prefix}/lib/alumet-agent"
ls -al %{_builddir}/
install -D -m 0755 "%{_builddir}/alumet-agent" "%{buildroot}%{_bindir}/alumet-agent"
mkdir -p %{buildroot}%{_sysconfdir}/alumet
chmod 777 %{buildroot}%{_sysconfdir}/alumet
install -D -m 0644 "%{_builddir}/alumet-config.toml" "%{buildroot}%{_sysconfdir}/alumet/alumet-config.toml"
install -D -m 0644 "%{_builddir}/alumet.service" "%{buildroot}%{_exec_prefix}/lib/systemd/system/alumet.service"

%files
%{_bindir}/alumet-agent
%{_exec_prefix}/lib/alumet-agent
%dir %{_sysconfdir}/alumet/
%{_sysconfdir}/alumet/alumet-config.toml
%{_exec_prefix}/lib/systemd/system/alumet.service

%post
KERNEL_VERSION=$(uname -r)
KERNEL_MAJOR=$(echo $KERNEL_VERSION | cut -d'.' -f1)
KERNEL_MINOR=$(echo $KERNEL_VERSION | cut -d'.' -f2)
# Check for correct integer value
if ! [[ "$KERNEL_MAJOR" =~ ^[0-9]+$ ]] || ! [[ "$KERNEL_MINOR" =~ ^[0-9]+$ ]]; then
    echo "Error: KERNEL_MAJOR or KERNEL_MINOR is not a valid integer."
    exit 1  # Exit or handle as needed
fi
# Add capabilities to alumet binary
setcap 'cap_sys_nice+ep' %{_exec_prefix}/lib/alumet-agent
if [ "$KERNEL_MAJOR" -gt 5 ] || { [ "$KERNEL_MAJOR" -eq 5 ] && [ "$KERNEL_MINOR" -ge 8 ]; }; then
    setcap 'cap_perfmon=ep cap_sys_nice+ep' %{_exec_prefix}/lib/alumet-agent
fi

%changelog 
* Wed Sep 18 2024 Cyprien cyprien.pelisse-verdoux@eviden.com - 0.0.1
- Initial package
