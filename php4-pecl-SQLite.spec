%define		_modname	SQLite
%define		_status		stable
%define		_smodname	sqlite

Summary:	%{_modname} - database bindings
Summary(pl):	%{_modname} - powi±zania z baz± danych
Name:		php4-pecl-%{_modname}
Version:	1.0.3
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	3741cb211f9eb3f77de086e96d232e95
URL:		http://pecl.php.net/package/SQLite/
BuildRequires:	libtool
BuildRequires:	php4-devel >= 4.0.0
Requires:	php-common
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php4
%define		extensionsdir	%{_libdir}/php4

%description
%{_modname} is a C library that implements an embeddable SQL database
engine. Programs that link with the %{_modname} library can have SQL
database access without running seperate RDBMS process. This extension
allows you to access %{_modname} databases from within PHP.

In PECL status of this package is: %{_status}.

%description -l pl
%{_modname} jest napisan± w C bibliotek± implementuj±c± osadzon± bazê
SQL. Programy konsolidowane z %{_modname} mog± mieæ dostêp do bazy SQL
bez potrzeby uruchamiana kolejnego procesu RDBMS. To rozszerzenie
pozwala na dostêp do baz SQLite z poziomu PHP.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
cd %{_modname}-%{version}
chmod 755 build/shtool
%{__make} install INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_smodname} %{_sysconfdir}/php.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_smodname} %{_sysconfdir}/php.ini
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/README %{_modname}-%{version}/TODO %{_modname}-%{version}/CREDITS
%doc %{_modname}-%{version}/sqlite.php %{_modname}-%{version}/tests
%attr(755,root,root) %{extensionsdir}/%{_smodname}.so
