%global debug_package %{nil}
%define _build_name_fmt %%{ARCH}/%%{NAME}-%%{VERSION}-%%{RELEASE}.%{osr}.%%{ARCH}.rpm


Name:           alumet
Version:        %{version}
Release:        %{release}
Summary:        A tool for measuring the energy consumption and performance metrics
License:        EUPL-1.2
Url:            https://github.com/alumet-dev/alumet
Source:         %{name}.tar.gz
BuildArch:      x86_64

BuildRequires:  openssl-devel >= 3.0.0

Requires: glibc >= 2.2.5
Requires: openssl >= 3.0.0


%package agent
Summary:        alumet-agent package
%description agent
This package contains the alumet app agent.
 
%description
Customizable and efficient tool for measuring the energy consumption and performance metrics of software on HPC, Cloud and Edge devices. 
 
%pre
KERNEL_VERSION=$(uname -r)
KERNEL_MAJOR=$(echo $KERNEL_VERSION | cut -d'.' -f1)
KERNEL_MINOR=$(echo $KERNEL_VERSION | cut -d'.' -f2)

%prep
%autosetup -n %{name}
 
%build
mkdir -p %{_builddir}/bin/
cp packaging/rpm/alumet.sh %{_builddir}/alumet-agent
cp packaging/alumet.service %{_builddir}/alumet.service
cd alumet/agent
CARGO_TARGET_DIR=%{_builddir}/bin/ ALUMET_AGENT_RELEASE=true cargo build --release -p alumet-agent --bins --all-features
ALUMET_CONFIG=%{_builddir}/alumet-config.toml %{_builddir}/bin/release/alumet-agent --plugins csv,perf,procfs,socket-control config regen 

%install
mkdir -p %{buildroot}%{_exec_prefix}/lib/
mkdir -p %{buildroot}%{_exec_prefix}/bin/
install -D -m 0555 "%{_builddir}/bin/release/alumet-agent" "%{buildroot}%{_exec_prefix}/lib/"
install -D -m 0755 "%{_builddir}/alumet-agent" "%{buildroot}%{_bindir}/"
mkdir -p %{buildroot}%{_sysconfdir}/alumet
chmod 777 %{buildroot}%{_sysconfdir}/alumet
install -D -m 0644 "%{_builddir}/alumet-config.toml" "%{buildroot}%{_sysconfdir}/alumet/alumet-config.toml"
install -D -m 0644 "%{_builddir}/alumet.service" "%{buildroot}%{_exec_prefix}/lib/systemd/system/alumet.service"

%files agent
%{_bindir}/alumet-agent
%{_exec_prefix}/lib/alumet-agent
%dir %{_sysconfdir}/alumet/
%{_sysconfdir}/alumet/alumet-config.toml
%{_exec_prefix}/lib/systemd/system/alumet.service

%post
# Add capabilities to alumet binary
%caps(cap_sys_nice+pe) %{_exec_prefix}/lib/alumet-agent
if [ "$KERNEL_MAJOR" -gt 5 ] || { [ "$KERNEL_MAJOR" -eq 5 ] && [ "$KERNEL_MINOR" -ge 8 ]; }; then
    %caps(cap_perfmon=pe) %{_exec_prefix}/lib/alumet-agent
fi


%changelog 
* Tue Mar 04 2025 Cyprien cyprien.pelisse-verdoux@eviden.com - 0.0.4
- Add dependencies about ssl
* Wed Feb 26 2025 Cyprien cyprien.pelisse-verdoux@eviden.com - 0.0.3
- Add capabilities to alumet binary
* Mon Feb 10 2025 Cyprien cyprien.pelisse-verdoux@eviden.com - 0.0.3
- Add service file
* Wed Feb 05 2025 Cyprien cyprien.pelisse-verdoux@eviden.com - 0.0.2
- Unified package
* Wed Sep 18 2024 Cyprien cyprien.pelisse-verdoux@eviden.com - 0.0.1
- Initial package
