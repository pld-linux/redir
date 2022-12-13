Summary:	redirect TCP connections
Summary(pl.UTF-8):	Przekierowywanie połączeń TCP
Summary(pt_BR.UTF-8):	Redir é um redirecionador de conexões
Name:		redir
Version:	3.3
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	https://github.com/troglobit/redir/releases/download/v%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	b452e1ca6faded7bab9c76dd61d9d983
URL:		https://github.com/troglobit/redir/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libwrap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Redir redirects tcp connections coming in to a local port to a
specified address/port combination.

%description -l pl.UTF-8
Redir przekierowuje połączenia tcp przychodzące na określony lokalny
port na podany inny adres oraz port.

%description -l pt_BR.UTF-8
Redir é um redirecionador de conexões.

%prep
%setup  -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
    DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md trans*.txt
%attr(755,root,root) %{_bindir}/redir
%{_mandir}/man1/redir.1*
