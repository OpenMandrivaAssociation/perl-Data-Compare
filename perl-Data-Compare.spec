%define	module	Data-Compare
%define	name	perl-%{module}
%define	version	0.13
%define	release	%mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Summary:	%{module} module for perl
Source0:	ftp.perl.org:/pub/CPAN/modules/by-module/Data/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
%if %{mdkversion} < 1010
Buildrequires: perl-devel
%endif
Buildrequires:  perl-File-Find-Rule
Requires:	perl >= 5.004
BuildArch:	noarch

%description
%{module} module for perl

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc TODO README CHANGES
%{perl_vendorlib}/Data
%{_mandir}/*/*

