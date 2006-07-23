Summary:	FLESSD - Free Library for Effects and Synthetic Sample Dynamics
Summary(pl):	FLESSD - wolnodostêpna biblioteka do efektów i d¼wiêku syntetycznego
Name:		flessd
Version:	0.0
Release:	1
License:	WTFPL
Group:		Libraries
Source0:	http://sam.zoy.org/flessd/%{name}-%{version}.tar.gz
# Source0-md5:	ec3ecdc01a51eebbb7171398f441afa0
URL:		http://sam.zoy.org/flessd/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FLESSD is a free reimplementation of FMOD (http://www.fmod.org/), a
very commonly used music playing and sound effects library.
Unfortunately FMOD is not free, and its author is extremely reluctant
to opensourcing it. Moreover, it only supports a limited number of
platforms. FLESSD aims to fix these two problems.

%description -l pl
FLESSD to wolnodostêpna reimplementacja biblioteki FMOD
(http://www.fmod.org/) - popularnej biblioteki do odtwarzania muzyki i
efektów d¼wiêkowych. Niestety FMOD nie jest wolnodostêpn± bibliotek±,
a autor jest bardzo oporny, je¶li chodzi o uwolnienie ¼róde³. Co
wiêcej FMOD obs³uguje tylko bardzo ograniczon± liczbê platform. Celem
FLESSD jest usuniêcie tych problemów.

%package devel
Summary:	Header files for FLESSD library
Summary(pl):	Pliki nag³ówkowe biblioteki FLESSD
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for FLESSD library.

%description devel -l pl
Pliki nag³ówkowe biblioteki FLESSD.

%package static
Summary:	Static FLESSD library
Summary(pl):	Statyczna biblioteka FLESSD
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static FLESSD library.

%description static -l pl
Statyczna biblioteka FLESSD.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NOTES README
%attr(755,root,root) %{_libdir}/libfmod-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfmod-*.so
%{_libdir}/libfmod-*.la
%{_includedir}/fmod*.h
%{_includedir}/flessd

%files static
%defattr(644,root,root,755)
%{_libdir}/libfmod-*.a
