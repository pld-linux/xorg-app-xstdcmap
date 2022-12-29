Summary:	xstdcmap application - X standard colormap utility
Summary(pl.UTF-8):	Aplikacja xstdcmap - narzędzie do standardowej palety kolorów X
Name:		xorg-app-xstdcmap
Version:	1.0.5
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/xstdcmap-%{version}.tar.xz
# Source0-md5:	86c9c5292a0810255cbd8767373b0f81
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.17
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xstdcmap utility can be used to selectively define standard
colormap properties. It is intended to be run from a user's X startup
script to create standard colormap definitions in order to facilitate
sharing of scarce colormap resources among clients using PseudoColor
visuals.

%description -l pl.UTF-8
Narzędzie xstdcmap służy do wybiórczego definiowania standardowych
właściwości palet kolorów. Jest przeznaczone do uruchamiania ze
skryptu startowego X użytkownika w celu stworzenia standardowych
definicji palet kolorów w celu ułatwienia współdzielenia
niewystarczającej liczby kolorów między klientami na ekranach
PseudoColor.

%prep
%setup -q -n xstdcmap-%{version}

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
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/xstdcmap
%{_mandir}/man1/xstdcmap.1*
