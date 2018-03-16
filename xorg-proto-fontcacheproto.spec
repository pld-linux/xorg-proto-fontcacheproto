# NOTE: now maintained in xorg-proto-xorgproto.spec
Summary:	Fontcache extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia Fontcache
Name:		xorg-proto-fontcacheproto
Version:	0.1.3
Release:	2.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/proto/fontcacheproto-%{version}.tar.bz2
# Source0-md5:	a8a50e5e995bfacb0359575faf7f6906
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fontcache extension headers.

%description -l pl.UTF-8
Nagłówki rozszerzenia Fontcache.

%package devel
Summary:	Fontcache extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia Fontcache
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
Fontcache extension headers.

%description devel -l pl.UTF-8
Nagłówki rozszerzenia Fontcache.

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
%doc COPYING ChangeLog README
%{_includedir}/X11/extensions/fontcach*.h
%{_pkgconfigdir}/fontcacheproto.pc
