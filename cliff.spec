#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cliff
Version  : 2.2.0
Release  : 31
URL      : http://pypi.debian.net/cliff/cliff-2.2.0.tar.gz
Source0  : http://pypi.debian.net/cliff/cliff-2.2.0.tar.gz
Summary  : Command Line Interface Formulation Framework
Group    : Development/Tools
License  : Apache-2.0
Requires: cliff-python
BuildRequires : PyYAML
BuildRequires : cliff
BuildRequires : cmd2
BuildRequires : nose
BuildRequires : pbr
BuildRequires : pip
BuildRequires : prettytable-python
BuildRequires : pyparsing
BuildRequires : python-dev
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : stevedore
BuildRequires : unicodecsv-python

%description
=======================================================
cliff -- Command Line Interface Formulation Framework
=======================================================

%package python
Summary: python components for the cliff package.
Group: Default
Requires: stevedore
Requires: unicodecsv-python

%description python
python components for the cliff package.


%prep
%setup -q -n cliff-2.2.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484539078
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python -m nose || :
%install
export SOURCE_DATE_EPOCH=1484539078
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
