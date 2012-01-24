#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	CatalystX
%define	pnam	Component-Traits
Summary:	CatalystX::Component::Traits - Automatic Trait Loading and Resolution for Catalyst Components
Summary(pl.UTF-8):	CatalystX::Component::Traits - automatyczne ładowanie Trait oraz rozwiązywanie dla komponentów Catalyst
Name:		perl-CatalystX-Component-Traits
Version:	0.16
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CatalystX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7165156a9ebc786146c710d2939f9c06
URL:		http://search.cpan.org/dist/CatalystX-Component-Traits/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Moose::Autobox)
BuildRequires:	perl(MooseX::Traits::Pluggable) >= 0.08
BuildRequires:	perl-Catalyst >= 5.80005
BuildRequires:	perl-List-MoreUtils
BuildRequires:	perl-Module-Pluggable >= 3.9
BuildRequires:	perl-namespace-autoclean
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Adds a Catalyst::Component/COMPONENT method to your Catalyst component
base class that reads the optional traits parameter from app and
component config and instantiates the component subclass with those
traits using MooseX::Traits/new_with_traits from
MooseX::Traits::Pluggable.

# %description -l pl.UTF-8 # TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/CatalystX
%dir %{perl_vendorlib}/CatalystX/Component
%{perl_vendorlib}/CatalystX/Component/*.pm
%{_mandir}/man3/*
