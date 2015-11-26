%define		pkgname	phar-utils
Summary:	PHAR file format utilities
Name:		php-seld-%{pkgname}
Version:	1.0.1
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	https://github.com/Seldaek/phar-utils/archive/%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	f8d6acf6eae6c29ec7c139f224f92664
URL:		https://github.com/Seldaek/phar-utils
BuildRequires:	php(core) >= 5.3
Requires:	php(core) >= 5.3.0
Requires:	php(date)
Requires:	php(hash)
Requires:	php(pcre)
Requires:	php(spl)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHAR file format utilities, for when PHP phars you up.

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Seld/PharUtils
cp -a src/* $RPM_BUILD_ROOT%{php_data_dir}/Seld/PharUtils

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%dir %{php_data_dir}/Seld
%{php_data_dir}/Seld/PharUtils
