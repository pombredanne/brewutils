%if 0%{?fedora}
%global _with_python3 1
%else
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print (get_python_lib())")}
%endif

%global srcname brewutils

Name:           python-%{srcname}
Version:        1.0.2
Release:        1%{?dist}
Summary:        Brew Utilities CLI

License:        GPLv2
URL:            http://python-brewutils-cli/
Source0:        http://python-brewutils-cli/brewutils-%{version}.tar.gz

BuildArch:      noarch


%description
%{summary}.

%package -n python2-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{srcname}}
BuildRequires:  python2-devel
Requires:       python2-devel
Requires:       nodejs-packaging
Requires:       rpmdevtools
Requires:       redhat-rpm-config
Requires:       rpm-build
Requires:       koji
Requires:       python-requests >= 2.7.0
Requires:       python-jsonschema
Requires:       python-unidiff


%description -n python2-%{srcname}
%{summary}.

Python 2 version.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build

%install
%py2_install

%check
#PYTHONPATH=. %{__python} -c "import brewutils"

%files -n python2-%{srcname}
%{python2_sitelib}/%{srcname}-*.egg-info/
%{python2_sitelib}/%{srcname}/
%{_bindir}/brew-utils-cli


%changelog
* Fri Dec 09 2016 Nick Coghlan <ncoghlan@redhat.com> - 1.0.2-1
- fix import error that was breaking patch analysis

* Tue Nov 29 2016 Slavek Kabrda <bkabrda@redhat.com> - 1.0.1-1
- updated to version 1.0.1

* Tue Sep 20 2016 Jiri Popelka <jpopelka@redhat.com> - 1.0.0-2
- use macros
- python2-brewutils subpackage

* Mon Sep 19 2016 Pavel Odvody <podvody@redhat.com> - 1.0.0-1
- new version
