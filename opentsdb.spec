Summary:	A scalable, distributed Time Series Database
Name:		opentsdb
Version:	2.0.0
Release:	0.1
License:	LGPL v2.1+
Group:		Applications/Databases
Source0:	https://github.com/OpenTSDB/opentsdb/releases/download/v2.0.0RC1/%{name}-%{version}.tar.gz
# Source0-md5:	e486e8a60a24f8169eebb5c663c5c082
URL:		http://opentsdb.net/
Requires:	gnuplot
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenTSDB is a distributed, scalable Time Series Database (TSDB)
written on top of HBase. OpenTSDB was written to address a common
need: store, index and serve metrics collected from computer systems
(network gear, operating systems, applications) at a large scale, and
make this data easily accessible and graphable.

Thanks to HBase's scalability, OpenTSDB allows you to collect many
thousands of metrics from thousands of hosts and applications, at a
high rate (every few seconds). OpenTSDB will never delete or
downsample data and can easily store billions of data points.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/cache/opentsdb

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README THANKS NEWS AUTHORS
%attr(755,root,root) %{_bindir}/tsdb
%dir %{_datadir}/opentsdb
%attr(755,root,root) %{_datadir}/opentsdb/*.sh
%dir %{_localstatedir}/cache/opentsdb
