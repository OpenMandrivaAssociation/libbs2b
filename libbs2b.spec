%define major	0
%define libname %mklibname bs2b %{major}
%define devname %mklibname -d bs2b

Summary:	Bauer stereophonic-to-binaural DSP library
Name:		libbs2b
Version:	3.1.0
Release:	11
License:	MIT
Group:		Sound
Url:		http://bs2b.sourceforge.net/
Source0:	http://downloads.sourceforge.net/sourceforge/bs2b/%{name}-%{version}.tar.lzma
Patch0:		libbs2b-3.1.0-fix-format-strings.patch
BuildRequires:	pkgconfig(sndfile)

%description
The Bauer stereophonic-to-binaural DSP (bs2b) library and plugins is
designed to improve headphone listening of stereo audio
records. Recommended for headphone prolonged listening to disable
superstereo fatigue without essential distortions.

%package utils
Summary:	Bauer stereophonic-to-binaural DSP library - sample tools
Group:		Sound

%description utils
The Bauer stereophonic-to-binaural DSP (bs2b) library and plugins is
designed to improve headphone listening of stereo audio
records. Recommended for headphone prolonged listening to disable
superstereo fatigue without essential distortions.

This contains the command line example tools.

%package -n %{libname}
Summary:	Bauer stereophonic-to-binaural DSP library
Group:		System/Libraries

%description -n %{libname}
This package contains a shared library for %{name}.

%package -n %{devname}
Summary:	Bauer stereophonic-to-binaural DSP library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development files for %{name}.

%prep
%setup -q
%apply_patches

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files utils
%doc README AUTHORS
%{_bindir}/*

%files -n %{libname}
%{_libdir}/libbs2b.so.%{major}*

%files -n %{devname}
%doc ChangeLog doc/readme.txt
%{_libdir}/*.so
%{_includedir}/bs2b
%{_libdir}/pkgconfig/*

