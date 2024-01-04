#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v3
# autospec commit: ab27b0e7ad12
#
Name     : squashfs-tools
Version  : 4.6.1
Release  : 12
URL      : https://mirrors.kernel.org/debian/pool/main/s/squashfs-tools/squashfs-tools_4.6.1.orig.tar.gz
Source0  : https://mirrors.kernel.org/debian/pool/main/s/squashfs-tools/squashfs-tools_4.6.1.orig.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: squashfs-tools-bin = %{version}-%{release}
Requires: squashfs-tools-license = %{version}-%{release}
Requires: squashfs-tools-man = %{version}-%{release}
BuildRequires : help2man
BuildRequires : lz4-dev
BuildRequires : lzo-dev
BuildRequires : xz-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
These pre-generated manpages are built using the Squashfs-tools Makefile
defaults with the gzip, lzo, lz4, xz, and zstd compression algorithms
selected.

%package bin
Summary: bin components for the squashfs-tools package.
Group: Binaries
Requires: squashfs-tools-license = %{version}-%{release}

%description bin
bin components for the squashfs-tools package.


%package license
Summary: license components for the squashfs-tools package.
Group: Default

%description license
license components for the squashfs-tools package.


%package man
Summary: man components for the squashfs-tools package.
Group: Default

%description man
man components for the squashfs-tools package.


%prep
%setup -q -n squashfs-tools-4.6.1
cd %{_builddir}/squashfs-tools-4.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1704411919
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
pushd squashfs-tools
make  %{?_smp_mflags}  LZO_SUPPORT=1 LZ4_SUPPORT=1 XZ_SUPPORT=1
popd


%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1704411919
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/squashfs-tools
cp %{_builddir}/squashfs-tools-%{version}/COPYING %{buildroot}/usr/share/package-licenses/squashfs-tools/4cc77b90af91e615a64ae04893fdffa7939db84c || :
pushd squashfs-tools
%make_install INSTALL_PREFIX=%{buildroot}/usr INSTALL_DIR=%{buildroot}/usr/bin INSTALL_MANPAGES_DIR=%{buildroot}/usr/share/man/man1
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mksquashfs
/usr/bin/sqfscat
/usr/bin/sqfstar
/usr/bin/unsquashfs

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/squashfs-tools/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mksquashfs.1.gz
/usr/share/man/man1/sqfscat.1.gz
/usr/share/man/man1/sqfstar.1.gz
/usr/share/man/man1/unsquashfs.1.gz
