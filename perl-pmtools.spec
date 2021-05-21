#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-pmtools
Version  : 2.2.0
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/M/ML/MLFISHER/pmtools-2.2.0.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/ML/MLFISHER/pmtools-2.2.0.tar.gz
Summary  : 'Perl Module Tools'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-pmtools-bin = %{version}-%{release}
Requires: perl-pmtools-license = %{version}-%{release}
Requires: perl-pmtools-man = %{version}-%{release}
Requires: perl-pmtools-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution pmtools,
version 2.2.0:
Perl Module Tools

%package bin
Summary: bin components for the perl-pmtools package.
Group: Binaries
Requires: perl-pmtools-license = %{version}-%{release}

%description bin
bin components for the perl-pmtools package.


%package dev
Summary: dev components for the perl-pmtools package.
Group: Development
Requires: perl-pmtools-bin = %{version}-%{release}
Provides: perl-pmtools-devel = %{version}-%{release}
Requires: perl-pmtools = %{version}-%{release}

%description dev
dev components for the perl-pmtools package.


%package license
Summary: license components for the perl-pmtools package.
Group: Default

%description license
license components for the perl-pmtools package.


%package man
Summary: man components for the perl-pmtools package.
Group: Default

%description man
man components for the perl-pmtools package.


%package perl
Summary: perl components for the perl-pmtools package.
Group: Default
Requires: perl-pmtools = %{version}-%{release}

%description perl
perl components for the perl-pmtools package.


%prep
%setup -q -n pmtools-2.2.0
cd %{_builddir}/pmtools-2.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-pmtools
cp %{_builddir}/pmtools-2.2.0/LICENSE %{buildroot}/usr/share/package-licenses/perl-pmtools/e11f4604f3f41a5845dccf945d2d498a2957fb6d
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/basepods
/usr/bin/faqpods
/usr/bin/modpods
/usr/bin/pfcat
/usr/bin/plxload
/usr/bin/pmall
/usr/bin/pman
/usr/bin/pmcat
/usr/bin/pmcheck
/usr/bin/pmdesc
/usr/bin/pmeth
/usr/bin/pmexp
/usr/bin/pmfunc
/usr/bin/pminclude
/usr/bin/pminst
/usr/bin/pmload
/usr/bin/pmls
/usr/bin/pmpath
/usr/bin/pmvers
/usr/bin/podgrep
/usr/bin/podpath
/usr/bin/pods
/usr/bin/podtoc
/usr/bin/sitepods
/usr/bin/stdpods

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Devel::Loaded.3
/usr/share/man/man3/pmtools.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-pmtools/e11f4604f3f41a5845dccf945d2d498a2957fb6d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/basepods.1
/usr/share/man/man1/faqpods.1
/usr/share/man/man1/modpods.1
/usr/share/man/man1/pfcat.1
/usr/share/man/man1/plxload.1
/usr/share/man/man1/pmall.1
/usr/share/man/man1/pman.1
/usr/share/man/man1/pmcat.1
/usr/share/man/man1/pmcheck.1
/usr/share/man/man1/pmdesc.1
/usr/share/man/man1/pmeth.1
/usr/share/man/man1/pmexp.1
/usr/share/man/man1/pmfunc.1
/usr/share/man/man1/pminclude.1
/usr/share/man/man1/pminst.1
/usr/share/man/man1/pmload.1
/usr/share/man/man1/pmls.1
/usr/share/man/man1/pmpath.1
/usr/share/man/man1/pmvers.1
/usr/share/man/man1/podgrep.1
/usr/share/man/man1/podpath.1
/usr/share/man/man1/pods.1
/usr/share/man/man1/podtoc.1
/usr/share/man/man1/sitepods.1
/usr/share/man/man1/stdpods.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Devel/Loaded.pm
/usr/lib/perl5/vendor_perl/5.34.0/pmtools.pm
