%define		_modname	SQLite
%define		_status		stable
%define		_smodname	sqlite
%define		_sysconfdir	/etc/php4
%define		extensionsdir	%{_libdir}/php4
Summary:	%{_modname} - database bindings
Summary(pl.UTF-8):	%{_modname} - powiązania z bazą danych
Name:		php4-pecl-%{_modname}
Version:	1.0.3
Release:	9
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	3741cb211f9eb3f77de086e96d232e95
URL:		http://pecl.php.net/package/SQLite/
BuildRequires:	php4-devel >= 3:4.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
Requires:	php4-common >= 3:4.4.0-3
Provides:	php(sqlite)
Obsoletes:	php-pear-%{_modname}
%{?requires_php_extension}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_modname} is a C library that implements an embeddable SQL database
engine. Programs that link with the %{_modname} library can have SQL
database access without running seperate RDBMS process. This extension
allows you to access %{_modname} databases from within PHP.

In PECL status of this package is: %{_status}.

%description -l pl.UTF-8
%{_modname} jest napisaną w C biblioteką implementującą osadzoną bazę
SQL. Programy konsolidowane z %{_modname} mogą mieć dostęp do bazy SQL
bez potrzeby uruchamiana kolejnego procesu RDBMS. To rozszerzenie
pozwala na dostęp do baz SQLite z poziomu PHP.

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
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/conf.d,%{extensionsdir}}
%{__make} -C %{_modname}-%{version} install INSTALL_ROOT=$RPM_BUILD_ROOT
cat <<'EOF' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/%{_smodname}.ini
; Enable %{_modname} extension module
extension=%{_smodname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php4_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php4_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/README %{_modname}-%{version}/TODO %{_modname}-%{version}/CREDITS
%doc %{_modname}-%{version}/sqlite.php %{_modname}-%{version}/tests
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/%{_smodname}.ini
%attr(755,root,root) %{extensionsdir}/%{_smodname}.so
