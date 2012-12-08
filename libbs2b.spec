%define major 0
%define libname %mklibname bs2b %{major}
%define develname %mklibname -d bs2b

Summary:	Bauer stereophonic-to-binaural DSP library
Name:		libbs2b
Version:	3.1.0
Release:	6
License:	MIT
Group:		Sound
Url:		http://bs2b.sourceforge.net/
Source0:	http://downloads.sourceforge.net/sourceforge/bs2b/%{name}-%{version}.tar.lzma
Patch:		libbs2b-3.1.0-fix-format-strings.patch
BuildRequires:	pkgconfig(sndfile)


%description
The Bauer stereophonic-to-binaural DSP (bs2b) library and plugins is
designed to improve headphone listening of stereo audio
records. Recommended for headphone prolonged listening to disable
superstereo fatigue without essential distortions.

%package utils
Group:		Sound
Summary:	Bauer stereophonic-to-binaural DSP library - sample tools

%description utils
The Bauer stereophonic-to-binaural DSP (bs2b) library and plugins is
designed to improve headphone listening of stereo audio
records. Recommended for headphone prolonged listening to disable
superstereo fatigue without essential distortions.

This contains the command line example tools.

%package -n %{libname}
Group:		System/Libraries
Summary:	Bauer stereophonic-to-binaural DSP library

%description -n %{libname}
The Bauer stereophonic-to-binaural DSP (bs2b) library and plugins is
designed to improve headphone listening of stereo audio
records. Recommended for headphone prolonged listening to disable
superstereo fatigue without essential distortions.

%package -n %{develname}
Group:		Development/C
Summary:	Bauer stereophonic-to-binaural DSP library
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
The Bauer stereophonic-to-binaural DSP (bs2b) library and plugins is
designed to improve headphone listening of stereo audio
records. Recommended for headphone prolonged listening to disable
superstereo fatigue without essential distortions.

%prep
%setup -q
%patch -p1

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libbs2b.so.%{major}*

%files utils
%doc README AUTHORS
%{_bindir}/*

%files -n %{develname}
%doc ChangeLog doc/readme.txt
%{_libdir}/*.so
%{_includedir}/bs2b
%{_libdir}/pkgconfig/*


%changelog
* Wed May 02 2012 Götz Waschk <waschk@mandriva.org> 3.1.0-5mdv2012.0
+ Revision: 794935
- update libsndfile build dep
- yearly rebuild

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 3.1.0-4
+ Revision: 660221
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 3.1.0-3mdv2011.0
+ Revision: 602526
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 3.1.0-2mdv2010.1
+ Revision: 520757
- rebuilt for 2010.1

* Tue Jul 21 2009 Götz Waschk <waschk@mandriva.org> 3.1.0-1mdv2010.0
+ Revision: 398318
- import libbs2b


