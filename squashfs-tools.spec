#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : squashfs-tools
Version  : 4.4
Release  : 8
URL      : https://mirrors.kernel.org/debian/pool/main/s/squashfs-tools/squashfs-tools_4.4.orig.tar.gz
Source0  : https://mirrors.kernel.org/debian/pool/main/s/squashfs-tools/squashfs-tools_4.4.orig.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: squashfs-tools-bin = %{version}-%{release}
Requires: squashfs-tools-license = %{version}-%{release}
BuildRequires : lz4-dev
BuildRequires : lzo-dev
BuildRequires : xz-dev
BuildRequires : zlib-dev
Patch1: backport-gcc10.patch

%description
GitHub
This is now the main development repository for Squashfs-Tools.
There are older repositories on Sourceforge and kernel.org.  These
are currently out of date, but should be updated in the near future.

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


%prep
%setup -q -n squashfs-tools-4.4
cd %{_builddir}/squashfs-tools-4.4
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589808951
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
pushd squashfs-tools
make  %{?_smp_mflags}  LZO_SUPPORT=1 LZ4_SUPPORT=1 XZ_SUPPORT=1
popd


%install
export SOURCE_DATE_EPOCH=1589808951
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/squashfs-tools
cp %{_builddir}/squashfs-tools-4.4/COPYING %{buildroot}/usr/share/package-licenses/squashfs-tools/4cc77b90af91e615a64ae04893fdffa7939db84c
pushd squashfs-tools
%make_install INSTALL_DIR=%{buildroot}/usr/bin
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mksquashfs
/usr/bin/unsquashfs

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/squashfs-tools/4cc77b90af91e615a64ae04893fdffa7939db84c
