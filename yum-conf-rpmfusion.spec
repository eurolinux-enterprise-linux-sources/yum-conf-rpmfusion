Name:           yum-conf-rpmfusion       
Version:        6
Release:        0.1
Summary:        RPMfusion release file and RPM repository configuration
Group:          System Environment/Base 
License:        GPL 
URL:            http://rpmforge.net/
Requires:       rpmfusion-free-release
Requires:	yum-plugin-fastestmirror
BuildArch:	noarch

%description
This package pulls in rpmfusion-free-release which contains the
yum configuration for the RPMfusion RPM Repository, as well as the
public GPG keys used to sign them.

It is the responsibility of the end user to verify their compliance
with the licensing of the rpms in this repository.


%files


%changelog
* Fri Jul 13 2012 Pat Riehecky <riehecky@fnal.gov> - 6-0.1
- The rpm only pulls in the appropriate release package

