Summary:	redirect TCP connections
Summary(pl.UTF-8):	Przekierowywanie połączeń TCP
Summary(pt_BR.UTF-8):	Redir é um redirecionador de conexões
Name:		redir
Version:	2.2.1
Release:	4
License:	GPL
Group:		Applications/Networking
Source0:	http://sammy.net/~sammy/hacks/%{name}-%{version}.tar.gz
# Source0-md5:	4342fadac30504c86c8db7beefe01995
Patch0:		%{name}-debian.patch
Patch1:		%{name}-passive-ftp.patch
URL:		http://sammy.net/~sammy/hacks/
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
%patch0 -p1

%build
%{__make} \
	EXTRA_CFLAGS="%{rpmcflags} %{rpmcppflags}" \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install redir $RPM_BUILD_ROOT%{_bindir}
install redir.man $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README trans*.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
