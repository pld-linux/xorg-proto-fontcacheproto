Summary:	Fontcache protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u Fontcache i pomocnicze
Name:		xorg-proto-fontcacheproto
Version:	0.1
Release:	0.02
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/proto/fontcacheproto-%{version}.tar.bz2
# Source0-md5:	9ff9d0d855b365517b8ad7397f68a907
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fontcache protocol and ancillary headers.

%description -l pl
Nag³ówki protoko³u Fontcache i pomocnicze.

%package devel
Summary:	Fontcache protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u Fontcache i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
Fontcache protocol and ancillary headers.

%description devel -l pl
Nag³ówki protoko³u Fontcache i pomocnicze.

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
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/fontcacheproto.pc
