Summary:	redirect TCP connections
Summary(pl):	Przekieruj po³±czenia TCP
Summary(pt_BR):	Redir é um redirecionador de conexões
Name:		redir
Version:	2.2.1
Release:	1
License:	GPL
Vendor:		Sammy <sammy@oh.verio.com>
Group:		Applications/Networking
Source0:	http://sammy.net/~sammy/hacks/%{name}-%{version}.tar.gz
Patch0:		%{name}-debian.patch
Patch1:		%{name}-passive-ftp.patch
URL:		http://sammy.net/~sammy/hacks/
BuildRequires:	libwrap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Redir redirects tcp connections coming in to a local port to a
specified address/port combination.

%description -l pl
Redir przekierowuje po³±czenia tcp przychodz±ce na okre¶lony lokalnyt
port na podany inny adres oraz port.

%description -l pt_BR
Redir é um redirecionador de conexões.

%prep
%setup  -q
%patch0 -p1

%build
%{__make} OPT_FLAGS="%{rpmcflags}" CC=%{__cc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1}

install redir $RPM_BUILD_ROOT%{_sbindir}
install redir.man $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README trans*.txt
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man*/*
