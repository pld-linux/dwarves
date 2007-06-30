Summary:	Dwarf Tools
Name:		dwarves
Version:	1.0
Release:	1
License:	GPL
Group:		Development/Tools
URL:		http://oops.ghostprotocols.net:81/blog
Source0:	http://userweb.kernel.org/~acme/%{name}-%{version}.tar.bz2
# Source0-md5:	d23bbf3a7fd6f084883c1071dd921267
BuildRequires:	cmake
BuildRequires:	elfutils-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dwarves is a set of tools that use the DWARF debugging information
inserted in ELF binaries by compilers such as GCC, used by well known
debuggers such as GDB, and more recent ones such as systemtap.

Utilities in the dwarves suite include pahole, that can be used to
find alignment holes in structs and classes in languages such as C,
C++, but not limited to these, and other information such as CPU
cacheline alignment, helping pack those structures to achieve more
cache hits, codiff, a diff like tool to compare the effects changes in
source code generate on the resulting binaries, pfunct, that can be
used to find all sorts of information about functions, inlines,
decisions made by the compiler about inlining, etc.

%package libs
Summary:	DWARF processing library
Group:		Development/Libraries

%description libs
DWARF processing library

%package devel
Summary:	DWARF processing library development files
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
DWARF processing library development files

%prep
%setup -q -c

%build
cmake \
	-D__LIB=%{_lib} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_BUILD_TYPE="MinSizeRel" .
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.ctracer
%attr(755,root,root) %{_bindir}/*
%{_datadir}/dwarves

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%doc MANIFEST README
%{_includedir}/*.h
%attr(755,root,root) %{_libdir}/*.so
