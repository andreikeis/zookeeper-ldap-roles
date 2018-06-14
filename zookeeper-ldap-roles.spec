Name:           zookeeper_ldap_roles
Version:        %{_version} 
Release:        %{_release}%{?dist}
Summary:        Plugin for Zookeeper

License:        Apache 2.0
URL:            https://github.com/Morgan-Stanley/zookeeper-ldap-roles
Prefix:         /opt/zookeeper
AutoReqProv:    no
Requires:       zookeeper >= 3.4.12, zookeeper < 3.5


%description
Zookeeper LDAP Roles plugin

%prep
%build
%install
mkdir -p %{buildroot}/opt/zookeeper
cp -r %{_builddir}/zookeeper-ldap-roles.jar %{buildroot}/opt/zookeeper/zookeeper-ldap-roles-%{_version}-%{_release}.jar

%post
%files
%defattr(-,root,root,-)
/opt/zookeeper/*

%changelog

