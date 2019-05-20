Name:		ssh-monitoring
Version:	0.1
Release:	1%{?dist}
Summary:	Monitor ssh

Group:		Testing
License:	GPL
URL:		https://github.com/Meexe/system-service
Source0:	%{name}-%{version}.tar.gz

BuildRequires:  /bin/mkdir, /bin/cp, /bin/rm, /bin/sudo	
Requires:	/bin/bash, /usr/bin/ps, /usr/bin/logger, /usr/bin/awk, /usr/bin/echo, /usr/bin/grep, /usr/bin/tr, /usr/bin/cut
BuildArch: noarch

%description
Test version 0.1

%prep
%setup -q


%install
mkdir -p %{buildroot}%{_mandir}/man7
mkdir -p %{buildroot}%{_unitdir}
sudo cp ssh-monitoring.7.gz %{buildroot}%{_mandir}/man7
sudo cp ssh-monitoring.service %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_bindir}
install -m 755 ssh-monitoring.sh %{buildroot}%{_bindir}


%files
%{_bindir}/ssh-monitoring.sh
%{_unitdir}/ssh-monitoring.service
%{_mandir}/man7/ssh-monitoring.7.gz

%changelog
* Sun May 19 2019 <Chesnov>
- Added %{_bindir}/ssh-monitoring
