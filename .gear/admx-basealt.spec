%define _destdir %_datadir/PolicyDefinitions

Name: admx-basealt
Version: 0.1.0
Release: alt1

Summary: BaseALT-specific ADMX policy templates
License: AGPLv3+
Group: System/Configuration/Other
Url: https://github.com/altlinux/admx-basealt
BuildArch: noarch

Source0: %name-%version.tar

%description
BaseALT-specific ADMX files, which are registry-based policy settings provide
an XML-based structure for defining the display of the Administrative Template
policy settings in the Group Policy Object Editor.

%prep
%setup -q

%install
mkdir -p %buildroot%_destdir
cp -r ru-RU/ en-US/ BaseALT*.admx %buildroot%_destdir/

%files
%dir %_destdir
%_destdir

%changelog
* Mon May 18 2020 Rustem Bapin <rbapin@altlinux.org> 0.1.0-alt1
- Initial release


