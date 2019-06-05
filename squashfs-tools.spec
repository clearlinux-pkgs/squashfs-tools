#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : squashfs-tools
Version  : 4.3
Release  : 3
URL      : http://http.debian.net/debian/pool/main/s/squashfs-tools/squashfs-tools_4.3.orig.tar.gz
Source0  : http://http.debian.net/debian/pool/main/s/squashfs-tools/squashfs-tools_4.3.orig.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: squashfs-tools-bin
Requires: squashfs-tools-license
BuildRequires : lz4-dev
BuildRequires : lzo-dev
BuildRequires : xz-dev
BuildRequires : zlib-dev

%description
SQUASHFS 4.3 - A squashed read-only filesystem for Linux
Released under the GPL licence (version 2 or later).

%package bin
Summary: bin components for the squashfs-tools package.
Group: Binaries
Requires: squashfs-tools-license

%description bin
bin components for the squashfs-tools package.


%package license
Summary: license components for the squashfs-tools package.
Group: Default

%description license
license components for the squashfs-tools package.


%prep
%setup -q -n squashfs4.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1529673484
pushd squashfs-tools
make  %{?_smp_mflags} LZO_SUPPORT=1 LZ4_SUPPORT=1 XZ_SUPPORT=1
popd

%install
export SOURCE_DATE_EPOCH=1529673484
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/squashfs-tools
cp COPYING %{buildroot}/usr/share/doc/squashfs-tools/COPYING
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
%defattr(-,root,root,-)
/usr/share/doc/squashfs-tools/COPYING
