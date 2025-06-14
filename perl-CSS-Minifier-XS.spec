#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-CSS-Minifier-XS
Version  : 0.13
Release  : 36
URL      : https://cpan.metacpan.org/authors/id/G/GT/GTERMARS/CSS-Minifier-XS-0.13.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GT/GTERMARS/CSS-Minifier-XS-0.13.tar.gz
Summary  : 'XS based CSS minifier'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-CSS-Minifier-XS-license = %{version}-%{release}
Requires: perl-CSS-Minifier-XS-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::DiagINC)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
CSS::Minifier::XS - XS based CSS minifier
SYNOPSIS
use CSS::Minifier::XS qw(minify);
my $css      = '...';
my $minified = minify($css);

%package dev
Summary: dev components for the perl-CSS-Minifier-XS package.
Group: Development
Provides: perl-CSS-Minifier-XS-devel = %{version}-%{release}
Requires: perl-CSS-Minifier-XS = %{version}-%{release}

%description dev
dev components for the perl-CSS-Minifier-XS package.


%package license
Summary: license components for the perl-CSS-Minifier-XS package.
Group: Default

%description license
license components for the perl-CSS-Minifier-XS package.


%package perl
Summary: perl components for the perl-CSS-Minifier-XS package.
Group: Default
Requires: perl-CSS-Minifier-XS = %{version}-%{release}

%description perl
perl components for the perl-CSS-Minifier-XS package.


%prep
%setup -q -n CSS-Minifier-XS-0.13
cd %{_builddir}/CSS-Minifier-XS-0.13

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
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
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-CSS-Minifier-XS
cp %{_builddir}/CSS-Minifier-XS-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-CSS-Minifier-XS/92e92d46bac9fa036a3d260671b6ce26398461d4 || :
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/CSS::Minifier::XS.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-CSS-Minifier-XS/92e92d46bac9fa036a3d260671b6ce26398461d4

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
