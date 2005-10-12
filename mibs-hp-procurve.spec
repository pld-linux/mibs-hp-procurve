Summary:	MIBs for HP ProCurve
Summary(pl):	MIB-y dla HP ProCurve
Name:		net-snmp-mibs-hp-procurve
Version:	0.Feb.2005
Release:	1
License:	Unknown
Group:		Applications/System
Source0:	ftp://ftp.hp.com/pub/networking/software/mibs_feb05.tar.Z
# Source0-md5:	73d3da7c89eb35f9a727ddb527f16561
URL:		http://www.hp.com/rnd/software/MIBs.htm
Requires:	net-snmp-mibs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MIBs for HP ProCurve Family Hardware.

%description -l pl
MIB-y dla sprzêtu z rodziny HP ProCurve.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/snmp/mibs

rm -f H2R07604c.mib

for file in *.mib; do
	b=$(basename "$file" .mib)
	install "$file" $RPM_BUILD_ROOT%{_datadir}/snmp/mibs/mib-${b}.txt
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.htm *.txt
%{_datadir}/snmp/mibs/*.*
