%global debug_package %{nil}
%define _build_name_fmt %%{ARCH}/%%{NAME}-%%{VERSION}-%%{RELEASE}.%{osr}.%%{ARCH}.rpm


Name:           alumet
Version:        %{version}
Release:        %{release}
Summary:        A tool for measuring the energy consumption and performance metrics
License:        EUPL
Url:            https://github.com/alumet-dev/alumet
Source:         %{name}.tar.gz
BuildArch:      x86_64

Requires: glibc >= 2.2.5
Requires: gcc >= 3.0
Requires: gnu-hash
Requires: rpmlib(CompressedFileNames) <= 3.0.4-1
Requires: rpmlib(FileDigests) <= 4.6.0-1
Requires: rpmlib(PayloadFilesHavePrefix) <= 4.0-1
Requires: rpmlib(PayloadIsXz) <= 5.2-1

%package agent
Summary:        alumet-agent package
%description agent
This package contains the alumet app agent.
 
%description
Customizable and efficient tool for measuring the energy consumption and performance metrics of software on HPC, Cloud and Edge devices. 
 
%prep
%autosetup -n %{name}
 
%build
mkdir -p %{_builddir}/bin/
cp packaging/alumet.sh %{_builddir}/alumet-agent
cd alumet/agent
CARGO_TARGET_DIR=%{_builddir}/bin/ ALUMET_AGENT_RELEASE=true cargo build --release -p alumet-agent --bins --all-features
ALUMET_CONFIG=%{_builddir}/alumet-config.toml %{_builddir}/bin/release/alumet-agent config regen 

%install
mkdir -p %{buildroot}%{_exec_prefix}/lib/
mkdir -p %{buildroot}%{_exec_prefix}/bin/
install -D -m 0555 "%{_builddir}/bin/release/alumet-agent" "%{buildroot}%{_exec_prefix}/lib/"
install -D -m 0755 "%{_builddir}/alumet-agent" "%{buildroot}%{_bindir}/"
mkdir -p %{buildroot}%{_sysconfdir}/alumet
chmod 777 %{buildroot}%{_sysconfdir}/alumet
install -D -m 0755 "%{_builddir}/alumet-config.toml" "%{buildroot}%{_sysconfdir}/alumet/alumet-config.toml"

%files agent
%{_bindir}/alumet-agent
%{_exec_prefix}/lib/alumet-agent
%dir %{_sysconfdir}/alumet/
%{_sysconfdir}/alumet/alumet-config.toml

%changelog 
* Wed Feb 05 2025 Cyprien cyprien.pelisse-verdoux@eviden.com - 0.0.2
- Unified package
* Wed Sep 18 2024 Cyprien cyprien.pelisse-verdoux@eviden.com - 0.0.1
- Initial package
