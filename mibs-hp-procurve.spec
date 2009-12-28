Summary:	MIBs for HP ProCurve
Summary(pl.UTF-8):	MIB-y dla HP ProCurve
Name:		mibs-hp-procurve
Version:	2006.02
Release:	1
License:	Unknown
Group:		Applications/System
Source0:	ftp://ftp.hp.com/pub/networking/software/mibs-feb06.tar
# Source0-md5:	273e93b8aca517b27cba35d7229a435b
URL:		http://www.hp.com/rnd/software/MIBs.htm
Requires:	mibs-dirs
Obsoletes:	net-snmp-mibs-hp-procurve
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		mibdir	%{_datadir}/mibs

%description
MIBs for HP ProCurve Family Hardware.

%description -l pl.UTF-8
MIB-y dla sprzętu z rodziny HP ProCurve.

%prep
%setup -q -c

rm -f H2R07604c.mib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{mibdir}
cp -a *.mib $RPM_BUILD_ROOT%{mibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.htm *.txt
%{mibdir}/*
