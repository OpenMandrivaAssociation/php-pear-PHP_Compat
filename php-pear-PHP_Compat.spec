%define	_class	PHP
%define	_subclass	Compat
%define	modname	%{_class}_%{_subclass}

Summary:	Provides missing functionality for older versions of PHP
Name:		php-pear-%{modname}
Version:	1.6.0a3
Release:	4
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/PHP_Compat/
Source0:	http://download.pear.php.net/package/PHP_Compat-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

%description
PHP_Compat provides missing functionality in the form of Constants and
Functions for older versions of PHP.

Constants:
- E_STRICT
- PATH_SEPERATOR
- ...

Functions:
- file_get_contents
- file_put_contents
- is_a
- scandir
- array_combine
- ...

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{modname}.xml

