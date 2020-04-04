%{?scl:%scl_package perl-parent}

Name:		%{?scl_prefix}perl-parent
Epoch:		1
Version:	0.237
Release:	451%{?dist}
Summary:	Establish an ISA relationship with base classes at compile time
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/parent
Source0:	https://cpan.metacpan.org/authors/id/C/CO/CORION/parent-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	%{?scl_prefix}perl-generators
BuildRequires:	%{?scl_prefix}perl-interpreter
BuildRequires:	%{?scl_prefix}perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	%{?scl_prefix}perl(strict)
# Test Suite
BuildRequires:	%{?scl_prefix}perl(lib)
BuildRequires:	%{?scl_prefix}perl(Test::More) >= 0.4
# Dependencies
Requires:	%{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))

%description
Allows you to both load one or more modules, while setting up inheritance
from those modules at the same time. Mostly similar in effect to:

	package Baz;

	BEGIN {
		require Foo;
		require Bar;

		push @ISA, qw(Foo Bar);
	}

%prep
%setup -q -n parent-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot}%{?scl:'}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc Changes
%{perl_vendorlib}/parent.pm
%{_mandir}/man3/parent.3*

%changelog
* Fri Dec 20 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.237-451
- SCL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.237-439
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.237-438
- Increase release to favour standalone package

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.237-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.237-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul  7 2018 Paul Howarth <paul@city-fan.org> - 1:0.237-1
- Update to 0.237
  - Don't load vars.pm (CPAN RT#132077)
- Drop legacy Group: tag
- Drop buildroot cleaning in %%install section

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.236-416
- Increase release to favour standalone package

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.236-395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.236-394
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.236-393
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.236-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 10 2016 Paul Howarth <paul@city-fan.org> - 1:0.236-1
- Update to 0.236
  - Add Travis test configuration
  - Make test for PMC availability more reliable
  - Disable benchmark test rt62341.t as it runs out of memory on many smoker
    systems (CPAN RT#118310)
- Simplify find command using -delete

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.234-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.234-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.234-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.234-2
- Perl 5.22 rebuild

* Thu May 28 2015 Paul Howarth <paul@city-fan.org> - 1:0.234-1
- Update to 0.234
  - Fix the test for PMC loading to work on versions on Perl that don't have
    Config::non_bincompat_options (CPAN RT#102626)

* Tue May 26 2015 Paul Howarth <paul@city-fan.org> - 1:0.233-1
- Update to 0.233
  - The diagnostic about inheriting from ourselves was removed; it served no
    purpose as Perl already warns if we try to inherit in a circular way

* Fri Mar 20 2015 Paul Howarth <paul@city-fan.org> - 1:0.232-1
- Update to 0.232
  - Change line-endings in parent-pmc.t to unix EOLs so that bleadperl is happy

* Tue Mar 10 2015 Paul Howarth <paul@city-fan.org> - 1:0.231-1
- Update to 0.231
  - Restore test compatibility where Perl does not provide
    &Config::non_bincompat_options (CPAN RT#102626)

* Sat Mar  7 2015 Paul Howarth <paul@city-fan.org> - 1:0.229-1
- Update to 0.229
  - Add link to (Github) repository
  - Guard tests against PERL_DISABLE_PMC

* Tue Jan 13 2015 Petr Pisar <ppisar@redhat.com> - 1:0.228-311
- Specify all dependencies

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.228-310
- Increase release to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.228-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.228-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 17 2013 Paul Howarth <paul@city-fan.org> - 1:0.228-1
- Update to 0.228
  - Install in site/ by default for 5.12+ (CPAN RT#88450)

* Sun Sep  1 2013 Paul Howarth <paul@city-fan.org> - 1:0.227-1
- Update to 0.227
  - Restore tests passing for 5.17.5+ (CPAN RT#88320)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.226-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 29 2013 Paul Howarth <paul@city-fan.org> - 1:0.226-1
- Update to 0.226
  - Fix tests for Perl 5.18 (CPAN RT#86890)

* Mon Jul 15 2013 Petr Pisar <ppisar@redhat.com> - 1:0.225-290
- Increase release to favour standalone package

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1:0.225-245
- Link minimal build-root packages against libperl.so explicitly

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1:0.225-244
- Adjust tests to perl-5.18 (CPAN RT#86890)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.225-243
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 25 2012 Paul Howarth <paul@city-fan.org> - 1:0.225-242
- Don't need to remove empty directories from the buildroot
- Drop %%defattr, redundant since rpm 4.4

* Wed Aug 15 2012 Petr Pisar <ppisar@redhat.com> - 1:0.225-241
- Specify all dependencies

* Mon Aug 13 2012 Marcela Mašláňová <mmaslano@redhat.com> - 1:0.225-240
- Bump release to override sub-package from perl.spec

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.225-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 1:0.225-7
- Perl 5.16 rebuild

* Tue Feb  7 2012 Paul Howarth <paul@city-fan.org> - 1:0.225-6
- Reinstate compatibility with old distributions like EL-5
  - Add back buildroot definition and cleaning
- Use DESTDIR rather than PERL_INSTALL_ROOT
- Make %%files list more explicit
- Drop redundant %%{?perl_default_filter}
- Don't use macros for commands
- Use tabs

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.225-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1:0.225-4
- Install to vendor directories rather than perl core directories so as to
  avoid conflicts between our debuginfo and the main perl-debuginfo package

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1:0.225-3
- Perl mass rebuild

* Tue Jun 14 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1:0.225-2
- Perl mass rebuild

* Sat May 07 2011 Iain Arnell <iarnell@gmail.com> - 1:0.225-1
- Update to latest upstream version
- Clean up spec for modern rpmbuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.224-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 21 2010 Iain Arnell <iarnell@gmail.com> - 1:0.224-1
- Update to latest upstream version

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:0.223-4
- Mass rebuild with perl-5.12.0

* Sat Mar 27 2010 Iain Arnell <iarnell@gmail.com> - 1:0.223-3
- Dual-life module
- Add epoch to match that of parent in core
- Use core macros, not vendor

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.223-2
- Rebuild against perl 5.10.1

* Fri Sep 11 2009 Chris Weyl <cweyl@alumni.drew.edu> - 0.223-1
- Update filtering
- Auto-update to 0.223 (by cpan-spec-update 0.01)
- Altered br on perl(Test::More) (0 => 0.4)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.221-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.221-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jun 19 2008 Chris Weyl <cweyl@alumni.drew.edu> - 0.221-2
- Bump

* Wed May 28 2008 Chris Weyl <cweyl@alumni.drew.edu> - 0.221-1
- Specfile autogenerated by cpanspec 1.75
