#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cliff
Version  : 1.15.0
Release  : 17
URL      : https://pypi.python.org/packages/source/c/cliff/cliff-1.15.0.tar.gz
Source0  : https://pypi.python.org/packages/source/c/cliff/cliff-1.15.0.tar.gz
Summary  : Command Line Interface Formulation Framework
Group    : Development/Tools
License  : Apache-2.0
Requires: cliff-python
BuildRequires : PyYAML
BuildRequires : cmd2
BuildRequires : funcsigs-python
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
Requires: unicodecsv-python

%description python
python components for the cliff package.


%prep
%setup -q -n cliff-1.15.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python -m nose
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
