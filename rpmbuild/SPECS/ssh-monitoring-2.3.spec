%global selinuxtype	targeted
%global moduletype	services
%global modulenames	ssh-monitoring

# Usage: _format var format
#   Expand 'modulenames' into various formats as needed
#   Format must contain '$x' somewhere to do anything useful
%global _format() export %1=""; for x in %{modulenames}; do %1+=%2; %1+=" "; done;

# Relabel files
%global relabel_files() \ # ADD files in *.fc file


# Version of distribution SELinux policy package 
%global selinux_policyver 3.13.1-128.6.fc22 

Name:           ssh-monitoring
Version:        2.3
Release:        1%{?dist}
Summary:        Monitor ssh

Group:          ssh-monitor
License:        GPL
URL:            https://github.com/Meexe/system-service
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  /bin/mkdir, /bin/cp, /bin/rm, /bin/sudo, selinux-policy, selinux-policy-devel, systemd
Requires:       /bin/bash, /usr/bin/ps, /usr/bin/logger, /usr/bin/awk, /usr/bin/echo, /usr/bin/grep, /usr/bin/tr, /usr/bin/cut
Requires(post):		selinux-policy-base >= %{selinux_policyver}, selinux-policy-targeted >= %{selinux_policyver}, policycoreutils, policycoreutils-python libselinux-utils

BuildArch: noarch

%description
Service with own SELinux policy, that check ssh-connections and warn users.

%prep
%setup -q


%build
make SHARE="%{_datadir}" TARGETS="%{modulenames}"


%install
mkdir -p %{buildroot}%{_mandir}/man7
mkdir -p %{buildroot}%{_unitdir}
sudo cp ssh-monitoring.7.gz %{buildroot}%{_mandir}/man7
sudo cp ssh-monitoring.service %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_bindir}/ssh-monitoring
install -m 755 ssh-monitoring.sh %{buildroot}%{_bindir}/ssh-monitoring
install -m 755 ssh-monitoring-lib.sh %{buildroot}%{_bindir}/ssh-monitoring
install -m 755 ssh-monitoring-test.sh %{buildroot}%{_bindir}/ssh-monitoring
# Install policy modules
%_format MODULES $x.pp.bz2
install -d %{buildroot}%{_datadir}/selinux/packages
install -m 0644 $MODULES \
	%{buildroot}%{_datadir}/selinux/packages
sudo useradd -r ssh-monitoring


%post
%systemd_post %{name}.service
#
# Install all modules in a single transaction
#
%_format MODULES %{_datadir}/selinux/packages/$x.pp.bz2
%{_sbindir}/semodule -n -s %{selinuxtype} -i $MODULES
if %{_sbindir}/selinuxenabled ; then
    %{_sbindir}/load_policy
    %relabel_files
fi


%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/semodule -n -r %{modulenames} &> /dev/null || :
	if %{_sbindir}/selinuxenabled ; then
		%{_sbindir}/load_policy
		%relabel_files
	fi
fi


%files
%{_bindir}/ssh-monitoring/ssh-monitoring.sh
%{_bindir}/ssh-monitoring/ssh-monitoring-lib.sh
%{_bindir}/ssh-monitoring/ssh-monitoring-test.sh
%{_unitdir}/ssh-monitoring.service
%{_mandir}/man7/ssh-monitoring.7.gz
%defattr(-,root,root,0755)
%attr(0644,root,root) %{_datadir}/selinux/packages/*.pp.bz2


%changelog
* Sun May 19 2019 <Chesnov>
- Added %{_bindir}/ssh-monitoring-0.2
