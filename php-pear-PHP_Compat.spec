%define		_class		PHP
%define		_subclass	Compat
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.6.0a3
Release:	1
Summary:	Provides missing functionality for older versions of PHP
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/PHP_Compat/
Source0:	http://download.pear.php.net/package/PHP_Compat-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

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
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.5.0-8mdv2011.0
+ Revision: 667638
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5.0-7mdv2011.0
+ Revision: 607138
- rebuild

* Sat Nov 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.0-6mdv2010.1
+ Revision: 467952
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.5.0-5mdv2010.0
+ Revision: 426666
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.5.0-4mdv2009.1
+ Revision: 321896
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.5.0-3mdv2009.0
+ Revision: 224867
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.5.0-2mdv2008.1
+ Revision: 178535
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.5.0-1mdv2007.0
+ Revision: 81210
- Import php-pear-PHP_Compat

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.5.0-1mdk
- 1.5.0
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.4.1-4mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.4.1-3mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.4.1-2mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.4.1-1mdk
- 1.4.1
- drop redundant patches (P0)

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-1mdk
- initial Mandriva package (PLD import)


