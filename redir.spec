Summary:	redirect TCP connections
Summary(pl):	Przekieruj po³±czenia TCP
Name:		redir
Version:	2.2
Release:	GPL
License:	BSD
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	ftp://metalab.unc.edu:/pub/linux/system/network/daemons/%{name}-%{version}.tar.gz
Patch0:		%{name}-debian.patch
Vendor:		Sammy <sammy@oh.verio.com>
BuildRequires:	libwrap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Redir redirects tcp connections coming in to a local port to a
specified address/port combination.

%description -l pl
Redir przekierowuje po³±czenia tcp przychodz±ce na okre¶lony lokalnyt
port na podany inny adres oraz port.

%prep
%setup  -q
%patch0 -p1

%build
%{__make} OPT_FLAGS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1}

install redir		$RPM_BUILD_ROOT%{_sbindir}
install redir.man	$RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf README trans*.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man*/*
