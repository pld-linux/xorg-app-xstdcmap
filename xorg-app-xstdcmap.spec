# $Rev: 3423 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	xstdcmap application
Summary(pl):	Aplikacja xstdcmap
Name:		xorg-app-xstdcmap
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/xstdcmap-%{version}.tar.bz2
# Source0-md5:	57df81eda7d6f8224269e6ce5d6ad944
Patch0:		xstdcmap-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/xstdcmap-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
xstdcmap application.

%description -l pl
Aplikacja xstdcmap.


%prep
%setup -q -n xstdcmap-%{version}
%patch0 -p1


%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%attr(755,root,wheel) %{_bindir}/*
%{_mandir}/man1/*.1*
