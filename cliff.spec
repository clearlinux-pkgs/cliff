#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cliff
Version  : 2.14.0
Release  : 49
URL      : https://files.pythonhosted.org/packages/90/2a/232a69a1f1fe3bdf9a05fd4ec6072c44b63849771d10b6f21a6be701c943/cliff-2.14.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/90/2a/232a69a1f1fe3bdf9a05fd4ec6072c44b63849771d10b6f21a6be701c943/cliff-2.14.0.tar.gz
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
BuildRequires : buildreq-distutils3
BuildRequires : cliff
BuildRequires : pbr

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
%setup -q -n cliff-2.14.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551029546
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
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
