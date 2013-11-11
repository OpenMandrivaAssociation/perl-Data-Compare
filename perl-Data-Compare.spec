%define	upstream_name	 Data-Compare
%define upstream_version 1.23

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	Compare perl data structures
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Data/Data-Compare-%{upstream_version}.tar.gz

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

%check
%make test

%install
%makeinstall_std

%files
%doc TODO README 
%{perl_vendorlib}/Data
%{_mandir}/*/*


%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 1.220.0-2mdv2011.0
+ Revision: 681370
- mass rebuild

* Mon Feb 15 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.220.0-1mdv2011.0
+ Revision: 506235
- update to 1.22

* Tue Feb 02 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.210.200-1mdv2010.1
+ Revision: 499488
- update to 1.2102

* Wed Jul 08 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.210.100-1mdv2010.0
+ Revision: 393690
- update to 1.2101
- using %%perl_convert_version
- fixed license field

* Fri Sep 05 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.21-1mdv2009.0
+ Revision: 281101
- update to new version 1.21

* Sun Aug 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.20-1mdv2009.0
+ Revision: 277943
- update to new version 1.20

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.19-2mdv2009.0
+ Revision: 268408
- rebuild early 2009.0 package (before pixel changes)

* Tue May 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.19-1mdv2009.0
+ Revision: 206815
- update to new version 1.19

* Tue Jan 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.18-1mdv2008.1
+ Revision: 156176
- update to new version 1.18
- update to new version 1.18

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 30 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.17-1mdv2008.0
+ Revision: 75272
- new version

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 0.16-1mdv2008.0
+ Revision: 19843
- 0.16


* Tue Aug 15 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/15/06 01:32:23 (56127)
- put test in %%check section

* Tue Aug 15 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/15/06 01:30:10 (56126)
Import perl-Data-Compare

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.13-2mdk
- Fix buildrequires

* Wed Nov 24 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.13-1mdk
- 0.13
- Add docs

* Fri Jun 04 2004 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 0.11-1mdk
- 0.1
- drop Prefix tag
- cosmetics

* Wed Feb 11 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.02-5mdk
- own dir


