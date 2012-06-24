Summary:	Fontcache protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu Fontcache i pomocnicze
Name:		xorg-proto-fontcacheproto
Version:	0.1.2
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/fontcacheproto-%{version}.tar.bz2
# Source0-md5:	60df6b625074a9790e28543dcea71651
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fontcache protocol and ancillary headers.

%description -l pl.UTF-8
Nagłówki protokołu Fontcache i pomocnicze.

%package devel
Summary:	Fontcache protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu Fontcache i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
Fontcache protocol and ancillary headers.

%description devel -l pl.UTF-8
Nagłówki protokołu Fontcache i pomocnicze.

%prep
%setup -q -n fontcacheproto-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/fontcacheproto.pc
