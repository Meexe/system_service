Name:           ssh-monitoring
Version:        0.2
Release:        1%{?dist}
Summary:        Monitor ssh

Group:          Testing
License:        GPL
URL:            https://github.com/Meexe/system-service
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  /bin/mkdir, /bin/cp, /bin/rm, /bin/sudo
Requires:       /bin/bash, /usr/bin/ps, /usr/bin/logger, /usr/bin/awk, /usr/bin/echo, /usr/bin/grep, /usr/bin/tr, /usr/bin/cut
BuildArch: noarch

%description
Test version 0.2

%prep
%setup -q


%install
mkdir -p %{buildroot}%{_mandir}/man7
mkdir -p %{buildroot}%{_unitdir}
sudo cp ssh-monitoring.7.gz %{buildroot}%{_mandir}/man7
sudo cp ssh-monitoring.service %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_bindir}/ssh-monitoring
install -m 755 ssh-monitoring.sh %{buildroot}%{_bindir}/ssh-monitoring
install -m 755 ssh-monitoring-lib.sh %{buildroot}%{_bindir}/ssh-monitoring
install -m 755 ssh-monitoring-test.sh %{buildroot}%{_bindir}/ssh-monitoring


%files
%{_bindir}/ssh-monitoring/ssh-monitoring.sh
%{_bindir}/ssh-monitoring/ssh-monitoring-lib.sh
%{_bindir}/ssh-monitoring/ssh-monitoring-test.sh
%{_unitdir}/ssh-monitoring.service
%{_mandir}/man7/ssh-monitoring.7.gz

%changelog
* Sun May 19 2019 <Chesnov>
- Added %{_bindir}/ssh-monitoring-0.2

