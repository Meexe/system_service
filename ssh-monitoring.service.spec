Name:           ssh-monitoring.service
Version:        1.0
Release:        1%{?dist}
Summary:        Monitoring of ssh connections

License:        GPLv3+
URL:            https://github.com/Meexe/system_service
Source0:        ssh-monitoring.service-1.0.tar.gz
BuildRequires: /bin/rm, /bin/mkdir, /bin/cp

Requires:       /bin/bash, /bin/netstat

BuildArch:      noarch

%description
System service for monitoring connection via ssh.

%prep

%setup -q

%build

%install

mkdir -p $RPM_BUILD_ROOT/usr/lib/ssh-monitoring
cp service.sh %{buildroot}/usr/lib/ssh-monitoring/service.sh
cp ssh-monitoring.service %{buildroot}/usr/lib/systemd/system/ssh-monitoring.service

%files
%license LICENSE
$RPM_BUILD_ROOT/usr/lib/ssh-monitoring/service.sh
$RPM_BUILD_ROOT/usr/lib/systemd/system/ssh-monitoring.service

%changelog
* Tue May 31 2016 B16-505  <mrchurilov@mail.ru> - 0.1-1
- System ssh monitoring
