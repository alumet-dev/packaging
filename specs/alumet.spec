Name:           alumet
Version:        0.5.0
Release:        %{release}
Summary:        A tool for measuring the energy consumption and performance metrics
License:        EUPL
Url:            https://github.com/alumet-dev/alumet
Source:         %{name}.tar.gz
BuildArch:      x86_64

%package alumet-local-agent
Summary:        alumet-local-agent package
%description alumet-local-agent
This package contains the alumet app agent.

%package alumet-relay-server
Summary:        alumet-relay-server package
%description alumet-relay-server
This package contains the alumet alumet-relay-server.

%package alumet-relay-client
Summary:        alumet-relay-client package
%description alumet-relay-client
This package contains the alumet alumet-relay-client.
 
%description
Customizable and efficient tool for measuring the energy consumption and performance metrics of software on HPC, Cloud and Edge devices. 
 
%prep
%autosetup -n %{name}

 
%build
cd alumet/app-agent
json=$(CARGO_TARGET_DIR=%{_builddir} cargo build --bins --release --all-features --message-format=json-render-diagnostics "$@")
executables=$(echo "$json" | grep -oP '"executable":"\K[^"]+' | tr '\n' ' ')
echo "$executables" > %{_builddir}/executables.txt



%install
mkdir -p %{buildroot}%{_bindir}
ls -al %{_builddir}
ls -al %{_builddir}/release/
ls -al %{_builddir}/release/build/
ls -al %{_builddir}/release/incremental
ls -al  %{buildroot}%{_bindir}
executables=$(cat %{_builddir}/executables.txt)
for binary in $executables; do
    filename=$(basename "$binary")
    install -D -m 0755 "$binary" %{buildroot}%{_bindir}/"$filename"
done


%files alumet-local-agent
%{_bindir}/alumet-local-agent

%files alumet-relay-server
%{_bindir}/alumet-relay-server

%files alumet-relay-client
%{_bindir}/alumet-relay-client

 
%changelog 
* Wed Sep 18 2024 Cyprien cyprien.pelisse-verdoux@eviden.com - 0.0.1
- Initial package
