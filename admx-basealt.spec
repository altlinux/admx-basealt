%define _destdir %_datadir/PolicyDefinitions

Name: admx-basealt
Version: 0.1.0
Release: alt1

Summary: Altlinux-specific admx files
License: GPLv3+
Group: System/Configuration/Other
Url: https://github.com/altlinux/admx-basealt
BuildArch: noarch

Source0: %name-%version.tar

%description
ADMX files, which are registry-based policy settings provide
an XML-based structure for defining the display of the
Administrative Template policy settings in the
Group Policy Object Editor.

%prep
%setup -q

%install
mkdir -p %buildroot%_destdir
cp -r  . %buildroot%_destdir
rm %buildroot%_destdir/%name.spec
rm -rf %buildroot%_destdir/.gear

%files
%_destdir

%changelog
* Mon May 18 2020 Rustem Bapin <rbapin@altlinux.org> 0.1.0-alt1
- Initial release


