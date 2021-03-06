%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           whisper
Version:        1.0.2
Release:        1
Summary:        Fixed size round-robin style database
Group:          Applications/Databases
License:        Apache Software License 2.0
URL:            https://graphiteapp.org/
Vendor:         Ryan McKern <ryan@orangefort.com>
Packager:       Ryan McKern <ryan@orangefort.com>
# Source0:        https://github.com/graphite-project/%{name}/archive/%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python python-devel python-setuptools
Requires:       python

%description
Whisper is a fixed-size database, similar in design to RRD.  It provides fast,
reliable storage of numeric data over time.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} -c 'import setuptools; execfile("setup.py")' build

%install
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}
%{__python} -c 'import setuptools; execfile("setup.py")' install --skip-build --root %{buildroot}

%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE
%doc contrib/*

%{python_sitelib}/*
/usr/bin/*

%changelog
* Tue Oct 24 2017 Ryan McKern <ryan@orangefort.com> 1.0.2-1
- New upstream version

* Fri Jun 1 2012 Ben P <ben@g.megatron.org> - 0.9.10-1
- New upstream version.

* Sat Oct 8 2011 Dan Carley <dan.carley@gmail.com> - 0.9.9-1
- New upstream version.

* Mon May 23 2011 Dan Carley <dan.carley@gmail.com> - 0.9.8-2
- Repackage with minor changes.

* Tue Apr 20 2011 Chris Abernethy <cabernet@chrisabernethy.com> - 0.9.8-1
- Update source to upstream v0.9.8
- Minor updates to spec file

* Thu Mar 17 2011 Daniel Aharon <daharon@sazze.com> - 0.9.7-1
- Add dependencies and description.
