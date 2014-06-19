Summary: Stanley reactor
Name: st2reactor
Version: 0.1.0
Release: 1
License: derp
Group: Applications/Engineering
Source: /opt/git/stanley/st2reactor-0.1.0.tar.gz
URL: https://github.com/StackStorm/stanley
Vendor: StackStorm
Packager: Stormin Stanley <stanley@stackstorm.com>
BuildRequires:	python-devel
Requires:   	python-pip
Requires:     mongodb
Requires:     mongodb-server
Requires:     st2common

%description
An automation plaform that needs a much better description than this.

%prep
%setup

%build

%install

mkdir -p %{buildroot}/etc/st2reactor/sensor
mkdir -p %{buildroot}%{python2_sitelib}
mkdir -p %{buildroot}/usr/bin/
cp -R st2reactor %{buildroot}%{python2_sitelib}/
cp -R st2reactor/sensor/samples %{buildroot}/etc/st2reactor/sensor/
cp -R conf/* %{buildroot}/etc/st2reactor
install -m755 bin/sensor_container %{buildroot}/usr/bin/sensor_container

%files

/usr/lib/python2.7/site-packages/st2reactor*
/usr/bin/sensor_container
/etc/st2reactor*
