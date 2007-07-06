Summary:	Dwarf Tools
Summary(pl.UTF-8):	Narzędzia Dwarf
Name:		dwarves
Version:	1.0
Release:	1
License:	GPL v2
Group:		Development/Tools
URL:		http://oops.ghostprotocols.net:81/blog
Source0:	http://userweb.kernel.org/~acme/%{name}-%{version}.tar.bz2
# Source0-md5:	d23bbf3a7fd6f084883c1071dd921267
BuildRequires:	cmake
BuildRequires:	elfutils-devel
BuildRequires:	rpmbuild(macros) >= 1.293
Requires:	%{name}-libs = %{version}-%{release}
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

%description -l pl.UTF-8
dwarves to zestaw narzędzi wykorzystujących informacje dla debuggera
w formacie DWARF umieszczane w binariach ELF przez kompilatory takie
jak GCC, używane przez dobrze znane debuggery takie jak GDB czy nowsze
takie jak systemtap.

Narzędzia ze zestawie dwarves zawierają pahole (do wyszukiwania dziur
wyrównań w strukturach i klasach w językach takich jak C czy C++ oraz
uzyskiwania innych informacji takich jak wyrównanie linii cache'a CPU,
co pomaga przy pakowaniu struktur dla osiągnięcia lepszej wydajności),
codiff (narzędzie podobne do diffa do porównywania wpływu zmian w
kodzie źródłowym na pliki wynikowe), pfunct (do znajdowania różnego
rodzaju informacji o funkcjach, funkcjach inline, decyzjach
dotyczących inline podejmowanych przez kompilator itp.).

%package libs
Summary:	DWARF processing library
Summary(pl.UTF-8):	Biblioteka do przetwarzania informacji DWARF
Group:		Libraries

%description libs
DWARF processing library.

%description libs -l pl.UTF-8
Biblioteka do przetwarzania informacji DWARF.

%package devel
Summary:	DWARF processing library development files
Summary(pl.UTF-8):	Pliki programistyczne biblioteki do przetwarzania informacji DWARF
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
DWARF processing library development files.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki do przetwarzania informacji DWARF.

%prep
%setup -q -c

%build
%cmake \
	-D__LIB=%{_lib} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_BUILD_TYPE="MinSizeRel" .
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.ctracer
%attr(755,root,root) %{_bindir}/*
%{_datadir}/dwarves

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdwarves*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdwarves*.so.?

%files devel
%defattr(644,root,root,755)
%doc MANIFEST README
%attr(755,root,root) %{_libdir}/libdwarves*.so
%{_includedir}/dwarves*.h
