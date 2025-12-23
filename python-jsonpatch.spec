%global pypi_name jsonpatch

Name:           python-%{pypi_name}
Version:	1.33
Release:	2
Summary:        Library to apply JSON patches according to RFC 6902
Group:          Development/Python
License:        MIT
URL:            https://pypi.python.org/pypi/jsonpatch
Source0:	https://files.pythonhosted.org/packages/source/j/jsonpatch/jsonpatch-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:	python
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)

%description
Library to apply JSON Patches according to RFC 6902

%files
%{_bindir}/*
%{python_sitelib}/%{pypi_name}.py
%{python_sitelib}/%{pypi_name}-%{version}-py*.*.egg-info
