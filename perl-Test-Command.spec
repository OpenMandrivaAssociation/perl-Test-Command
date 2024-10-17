%define upstream_name    Test-Command
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.11
Release:	4

Summary:	Test routines for external commands
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/Test-Command-0.11.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::Simple)
BuildArch:	noarch

%description
'Test::Command' intends to bridge the gap between the well tested functions
and objects you choose and their usage in your programs. By examining the
exit status, terminating signal, STDOUT and STDERR of your program you can
determine if it is behaving as expected.

This includes testing the various combinations and permutations of options
and arguments as well as the interactions between the various functions and
objects that make up your program.

The various test functions below can accept either a command string or an
array reference for the first argument. If the command is expressed as a
string it is passed to 'system' as is. If the command is expressed as an
array reference it is dereferenced and passed to 'system' as a list. See
''perldoc -f system'' for how these may differ.

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
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.80.0-2mdv2011.0
+ Revision: 657840
- rebuild for updated spec-helper

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.80.0-1mdv2011.0
+ Revision: 602043
- import perl-Test-Command


