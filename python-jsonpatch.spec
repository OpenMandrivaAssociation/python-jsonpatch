%global pypi_name jsonpatch

Name:           python-%{pypi_name}
Version:	1.35
Release:	1
Summary:        Library to apply JSON patches according to RFC 6902
Group:          Development/Python
License:        MIT
URL:            https://pypi.python.org/pypi/jsonpatch
Source0:	https://files.pythonhosted.org/packages/source/j/jsonpatch/jsonpatch-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:	python
BuildRequires:	python%{pyver}dist(jsonpointer) >= 3.2
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Library to apply JSON Patches according to RFC 6902

%files
%{_bindir}/jsondiff
%{_bindir}/jsonpatch
%{python_sitelib}/%{pypi_name}.py
%{python_sitelib}/%{pypi_name}_cli.py
%{python_sitelib}/__pycache__/%{pypi_name}*.pyc
%{python_sitelib}/%{pypi_name}-%{version}.dist-info
