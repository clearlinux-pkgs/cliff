#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cliff
Version  : 3.1.0
Release  : 62
URL      : https://files.pythonhosted.org/packages/21/4e/0edfaf74a40cffe66de8ae8b9704420696ed37238dd57ce0935c9a341077/cliff-3.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/21/4e/0edfaf74a40cffe66de8ae8b9704420696ed37238dd57ce0935c9a341077/cliff-3.1.0.tar.gz
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
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : cliff
BuildRequires : cmd2
BuildRequires : pbr
BuildRequires : pyparsing
BuildRequires : six
BuildRequires : stevedore
Patch1: 0001-Drop-strict-version-requirements-for-cmd2.patch

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
Provides: pypi(cliff)
Requires: pypi(cmd2)
Requires: pypi(pbr)
Requires: pypi(prettytable)
Requires: pypi(pyparsing)
Requires: pypi(pyyaml)
Requires: pypi(six)
Requires: pypi(stevedore)

%description python3
python3 components for the cliff package.


%prep
%setup -q -n cliff-3.1.0
cd %{_builddir}/cliff-3.1.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1585315114
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
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
cp %{_builddir}/cliff-3.1.0/LICENSE %{buildroot}/usr/share/package-licenses/cliff/2b8b815229aa8a61e483fb4ba0588b8b6c491890
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cliff/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
