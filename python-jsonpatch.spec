%global pypi_name jsonpatch

Name:           python-%{pypi_name}
Version:	1.32
Release:	1
Summary:        Library to apply JSON patches according to RFC 6902
Group:          Development/Python
License:        MIT
URL:            https://pypi.python.org/pypi/jsonpatch
Source0:	https://files.pythonhosted.org/packages/source/j/jsonpatch/jsonpatch-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:	python3dist(setuptools-scm)

%description
Library to apply JSON Patches according to RFC 6902

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python-%{pypi_name}
%{_bindir}/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py*.*.egg-info
