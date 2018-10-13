#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-CSS-Minifier-XS
Version  : 0.09
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/G/GT/GTERMARS/CSS-Minifier-XS-0.09.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GT/GTERMARS/CSS-Minifier-XS-0.09.tar.gz
Summary  : 'XS based CSS minifier'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-CSS-Minifier-XS-lib = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
CSS::Minifier::XS minifies CSS documents by removing un-necessary whitespace
This is free software; you can redistribute it and/or modify it under the same
terms as Perl itself.

%package dev
Summary: dev components for the perl-CSS-Minifier-XS package.
Group: Development
Requires: perl-CSS-Minifier-XS-lib = %{version}-%{release}
Provides: perl-CSS-Minifier-XS-devel = %{version}-%{release}

%description dev
dev components for the perl-CSS-Minifier-XS package.


%package lib
Summary: lib components for the perl-CSS-Minifier-XS package.
Group: Libraries

%description lib
lib components for the perl-CSS-Minifier-XS package.


%prep
%setup -q -n CSS-Minifier-XS-0.09

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
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
/usr/lib/perl5/vendor_perl/5.26.1/x86_64-linux-thread-multi/CSS/Minifier/XS.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/CSS::Minifier::XS.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.26.1/x86_64-linux-thread-multi/auto/CSS/Minifier/XS/XS.so
