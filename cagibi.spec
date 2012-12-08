Name: cagibi
Summary: An experimental cache/proxy system for the SSDPpart of UPnP
Version: 0.1.1
Release: %mkrel 2
Url: http://www.kde.org
License: LGPLv2+
Group: System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Source0: http://fr2.rpmfind.net/linux/KDE/stable/cagibi/%name-%version.tar.bz2
BuildRequires: qt4-devel
BuildRequires: kde4-macros
BuildRequires: automoc4

%description
Cagibi aims to be to SSDP what Avahi is to DNS-SD/Zeroconf:
a cache caching all service/device announcements on the network in a
local process as well as being a broker serving local announcements to
the network.
Both should be done by a single daemon process, accessable via D-Bus
on the system bus. The cache should offer active queries, so another
process is only informed about changes about UPnP devices it is
interested in.

%files
%defattr(-,root,root)
%{_kde_bindir}/cagibid
%{_kde_datadir}/dbus-1/services/org.kde.Cagibi.service

#--------------------------------------------------------------------
%package devel
Summary: Development files for %name
Group: Development/KDE and Qt
Requires: %name = %version

%description devel
This package contains development files for %name.

%files devel
%defattr(-,root,root)
%{_kde_libdir}/pkgconfig/*.pc

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf %{buildroot}


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-2mdv2011.0
+ Revision: 663351
- mass rebuild

* Mon Aug 09 2010 Funda Wang <fwang@mandriva.org> 0.1.1-1mdv2011.0
+ Revision: 567816
- New version 0.1.1

* Thu Jul 29 2010 Funda Wang <fwang@mandriva.org> 0.1.0-1mdv2011.0
+ Revision: 563163
- import cagibi


