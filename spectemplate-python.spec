%global %pypi_name ...
Name:           python-%{pypi_name}
Version:        
Release:        1%{?dist}
Summary:        
License:        
URL:            
Source0:        %{pypi_source}

BuildArch:      

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%{?python_enable_dependency_generator}

%description
...


%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%if %{defined epel}
# Put manual requires here:
Requires:       python%{python3_pkgversion}-foo
%endif

%description -n python%{python3_pkgversion}-%{pypi_name}
...


%prep
%autosetup -p1


%build
%py3_build


%install
%py3_install


%check
# use what your upstream is using
%{__python3} setup.py test
%{__python3} -m pytest
%{__python3} -m nose
...


%files -n  python%{python3_pkgversion}-%{pypi_name}
%license add-license-file-here
%doc add-docs-here
# For noarch packages: sitelib
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
# For arch-specific packages: sitearch
%{python3_sitearch}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/


%changelog
