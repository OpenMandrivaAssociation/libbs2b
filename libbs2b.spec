%define name libbs2b
%define version 3.1.0
%define release %mkrel 1

%define major 0
%define libname %mklibname bs2b %major
%define develname %mklibname -d bs2b

Summary: Bauer stereophonic-to-binaural DSP library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://downloads.sourceforge.net/sourceforge/bs2b/%{name}-%{version}.tar.lzma
Patch: libbs2b-3.1.0-fix-format-strings.patch
License: MIT
Group: Sound
Url: http://bs2b.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libsndfile-devel


%description
The Bauer stereophonic-to-binaural DSP (bs2b) library and plugins is
designed to improve headphone listening of stereo audio
records. Recommended for headphone prolonged listening to disable
superstereo fatigue without essential distortions.

%package utils
Group: Sound
Summary: Bauer stereophonic-to-binaural DSP library - sample tools

%description utils
The Bauer stereophonic-to-binaural DSP (bs2b) library and plugins is
designed to improve headphone listening of stereo audio
records. Recommended for headphone prolonged listening to disable
superstereo fatigue without essential distortions.

This contains the command line example tools.

%package -n %libname
Group: System/Libraries
Summary: Bauer stereophonic-to-binaural DSP library

%description -n %libname
The Bauer stereophonic-to-binaural DSP (bs2b) library and plugins is
designed to improve headphone listening of stereo audio
records. Recommended for headphone prolonged listening to disable
superstereo fatigue without essential distortions.

%package -n %develname
Group: Development/C
Summary: Bauer stereophonic-to-binaural DSP library
Requires: %libname = %version-%release
Provides: %name-devel = %version-%release

%description -n %develname
The Bauer stereophonic-to-binaural DSP (bs2b) library and plugins is
designed to improve headphone listening of stereo audio
records. Recommended for headphone prolonged listening to disable
superstereo fatigue without essential distortions.

%prep
%setup -q
%patch -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files -n %libname
%defattr(-,root,root)
%_libdir/libbs2b.so.%{major}*

%files utils
%defattr(-,root,root)
%doc README AUTHORS
%_bindir/*

%files -n %develname
%defattr(-,root,root)
%doc ChangeLog doc/readme.txt
%_libdir/*.so
%_libdir/*a
%_includedir/bs2b
%_libdir/pkgconfig/*
