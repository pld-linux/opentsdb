Summary:	A scalable, distributed Time Series Database
Name:		opentsdb
Version:	2.1.0
Release:	0.1
License:	LGPL v2.1+
Group:		Applications/Databases
Source0:	https://github.com/OpenTSDB/opentsdb/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8438173a0b0ddfcbd49b731870ca9f4c
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
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/cache/%{name}
%{__make} install -j1 \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_datadir}/%{name}/bin/mygnuplot.bat

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README THANKS NEWS AUTHORS
%attr(755,root,root) %{_bindir}/tsdb
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/bin
%attr(755,root,root) %{_datadir}/%{name}/bin/*.sh
%attr(755,root,root) %{_datadir}/%{name}/bin/tsdb
%{_datadir}/%{name}/tools
%{_datadir}/%{name}/static

# third_party
%dir %{_datadir}/%{name}/lib
%{_datadir}/%{name}/lib/async-1.4.0.jar
%{_datadir}/%{name}/lib/asynchbase-1.6.0.jar
%{_datadir}/%{name}/lib/guava-18.0.jar
%{_datadir}/%{name}/lib/jackson-annotations-2.4.3.jar
%{_datadir}/%{name}/lib/jackson-core-2.4.3.jar
%{_datadir}/%{name}/lib/jackson-databind-2.4.3.jar
%{_datadir}/%{name}/lib/log4j-over-slf4j-1.7.7.jar
%{_datadir}/%{name}/lib/logback-classic-1.0.13.jar
%{_datadir}/%{name}/lib/logback-core-1.0.13.jar
%{_datadir}/%{name}/lib/netty-3.9.4.Final.jar
%{_datadir}/%{name}/lib/protobuf-java-2.5.0.jar
%{_datadir}/%{name}/lib/slf4j-api-1.7.7.jar
%{_datadir}/%{name}/lib/tsdb-2.1.0.jar
%{_datadir}/%{name}/lib/zookeeper-3.3.6.jar

%dir %{_localstatedir}/cache/%{name}

# this looks like install error
%dir %{_datadir}/%{name}/etc
%dir %{_datadir}/%{name}/etc/opentsdb
%dir %{_datadir}/%{name}/etc/init.d
%{_datadir}/%{name}/etc/opentsdb/logback.xml
%{_datadir}/%{name}/etc/opentsdb/opentsdb.conf
%attr(754,root,root) %{_datadir}/%{name}/etc/init.d/opentsdb
