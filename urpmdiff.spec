%define name	urpmdiff
%define version	1.9
%define release	6

Name:		%{name}
Version:	%{version}
Release:	1
Summary:	A tool to show diffs between rpms
License:	GPL
Group:		Development/Other
Source0:	%{name}-%{version}.tar.bz2
Url:		http://cvs.mandriva.com/cgi-bin/cvsweb.cgi/soft/%{name}
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel

%description
%{name} shows the differences between two rpms. It's intended to help
packagers to know what has changed between an old and a new version of an rpm.
Its output is reminiscent of the unified diff format.

%prep
%setup -q -n %{name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog
%{_mandir}/*/*
%{_bindir}/*



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.9-5mdv2010.0
+ Revision: 434588
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.9-4mdv2009.0
+ Revision: 261810
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.9-3mdv2009.0
+ Revision: 255259
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.9-1mdv2008.1
+ Revision: 128812
- kill re-definition of %%buildroot on Pixel's request
- import urpmdiff


* Mon Apr 24 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.9-1mdk
- Fix problem in default options

* Tue Apr 18 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.8-1mdk
- Minor fix in -c implementation

* Wed Apr 05 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.7-1mdk
- New option -c

* Wed Jan 04 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.6-1mdk
- Bug fix in sorting file-related tags

* Fri Dec 23 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.5-1mdk
- Sort tag values before diffing

* Fri Dec 23 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.4-1mdk
- Don't write headers for empty chunks

* Tue Dec 13 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.3-1mdk
- -d now also compares "Conflicts" tags

* Wed Oct 19 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.2-1mdk
- New switches to compare versions from the command-line

* Tue Jun 14 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.1-1mdk
- Fix display of usage with -h

* Wed Mar 16 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.0-1mdk
- Initial version
