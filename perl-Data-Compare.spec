%define	upstream_name	 Data-Compare
%define upstream_version 1.29

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	Compare perl data structures


Url:		https://github.com/DrHyde/perl-modules-Data-Compare
Source0:	https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/Data-Compare-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:  perl-devel
BuildRequires:  perl(File::Find::Rule)
BuildArch:	noarch

%description
Compare two perl data structures recursively. Returns 0 if the structures
differ, else returns 1.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc README 
%{perl_vendorlib}/Data
%{_mandir}/*/*




