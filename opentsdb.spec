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
Requires:	jre
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
install -d $RPM_BUILD_ROOT/var/cache/%{name}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_datadir}/%{name}/mygnuplot.bat

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README THANKS NEWS AUTHORS
%attr(755,root,root) %{_bindir}/tsdb
%dir %{_datadir}/opentsdb
%attr(755,root,root) %{_datadir}/%{name}/*.sh
%{_datadir}/%{name}/logback.xml
%{_datadir}/%{name}/opentsdb.conf
%{_datadir}/%{name}/static

# third_party
%{_datadir}/%{name}/asynchbase-1.4.1.jar
%{_datadir}/%{name}/guava-13.0.1.jar
%{_datadir}/%{name}/jackson-annotations-2.1.4.jar
%{_datadir}/%{name}/jackson-core-2.1.4.jar
%{_datadir}/%{name}/jackson-databind-2.1.4.jar
%{_datadir}/%{name}/log4j-over-slf4j-1.7.2.jar
%{_datadir}/%{name}/logback-classic-1.0.9.jar
%{_datadir}/%{name}/logback-core-1.0.9.jar
%{_datadir}/%{name}/netty-3.6.2.Final.jar
%{_datadir}/%{name}/slf4j-api-1.7.2.jar
%{_datadir}/%{name}/suasync-1.4.0.jar
%{_datadir}/%{name}/tsdb-2.0.0.jar
%{_datadir}/%{name}/zookeeper-3.3.6.jar

%dir %{_localstatedir}/cache/%{name}
