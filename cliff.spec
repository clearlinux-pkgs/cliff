#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cliff
Version  : 2.15.0
Release  : 53
URL      : https://files.pythonhosted.org/packages/bb/3d/225750bee763d6f15edddf9fad8119e2e90a34a1941ca56ed069c9196e47/cliff-2.15.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/bb/3d/225750bee763d6f15edddf9fad8119e2e90a34a1941ca56ed069c9196e47/cliff-2.15.0.tar.gz
Summary  : Command Line Interface Formulation Framework
Group    : Development/Tools
License  : Apache-2.0
Requires: cliff-license = %{version}-%{release}
Requires: cliff-python = %{version}-%{release}
Requires: cliff-python3 = %{version}-%{release}
Requires: PyYAML
Requires: cliff
Requires: cmd2
Requires: pbr
Requires: pyparsing
Requires: six
Requires: stevedore
Requires: unicodecsv
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : cliff
BuildRequires : cmd2
BuildRequires : pbr
BuildRequires : pyparsing
BuildRequires : six
BuildRequires : stevedore
BuildRequires : unicodecsv

%description
========================
Team and repository tags
========================
.. image:: https://governance.openstack.org/tc/badges/cliff.svg
:target: https://governance.openstack.org/tc/reference/tags/index.html

%package license
Summary: license components for the cliff package.
Group: Default

%description license
license components for the cliff package.


%package python
Summary: python components for the cliff package.
Group: Default
Requires: cliff-python3 = %{version}-%{release}

%description python
python components for the cliff package.


%package python3
Summary: python3 components for the cliff package.
Group: Default
Requires: python3-core

%description python3
python3 components for the cliff package.


%prep
%setup -q -n cliff-2.15.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1560480290
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cliff
cp LICENSE %{buildroot}/usr/share/package-licenses/cliff/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cliff/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
