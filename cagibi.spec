Summary:	An experimental cache/proxy system for the SSDPpart of UPnP
Name:		cagibi
Version:	0.2.0
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.kde.org
Source0:	http://fr2.rpmfind.net/linux/KDE/stable/cagibi/%{name}-%{version}.tar.bz2

BuildRequires:	automoc4
BuildRequires:	kde4-macros
BuildRequires:	qt4-devel

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
%{_kde_bindir}/cagibid
%{_kde_datadir}/dbus-1/services/org.kde.Cagibi.service
%{_sysconfdir}/%{name}.conf
%{_sysconfdir}/dbus-1/system.d/org.kde.Cagibi.conf
%{datadir}/dbus-1/interfaces/org.kde.Cagibi.*
%{_datadir}/dbus-1/system-services/org.kde.Cagibi.service

#--------------------------------------------------------------------
%package	devel
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{name} = %{version}

# %description devel
# This package contains development files for %{name}.

# %files devel
#% {_kde_libdir}/pkgconfig/*.pc

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

