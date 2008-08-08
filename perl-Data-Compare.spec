%define	module	Data-Compare
%define	name	perl-%{module}
%define	version	1.19
%define	release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Compare perl data structures
Url:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Data/%{module}-%{version}.tar.gz
Buildrequires:  perl-File-Find-Rule
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Compare two perl data structures recursively. Returns 0 if the structures
differ, else returns 1.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc TODO README CHANGES
%{perl_vendorlib}/Data
%{_mandir}/*/*
