%define _destdir %_datadir/PolicyDefinitions

Name: admx-basealt
Version: 0.6.0
Release: alt1

Summary: BaseALT-specific ADMX policy templates
License: AGPLv3+
Group: System/Configuration/Other
Url: https://github.com/altlinux/admx-basealt
BuildArch: noarch

BuildRequires: admx-lint

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

%check
for file in *.admx *-*/*.adml; do
    admx-lint --input_file "$file"
done

%files
%dir %_destdir
%_destdir

%changelog
* Thu Aug 14 2025 Valentin Sokolov <sova@altlinux.org> 0.6.0-alt1
- Added disable cifsacl policy for user
- Improved name Gnome -> GNOME in all policies
- Improved LAPS policy description
- Removed dbus.service policy
- Fix bugs (closes: 54884, 54929, 54944, 54945, 55365, 54400, 55550, 54402, 53920)

* Mon Jun 02 2025 Valentin Sokolov <sova@altlinux.org> 0.5.0-alt1
- Added a group of settings for Gnome
- Added a group of settings for Apperance Gnome
- Added a group of settings for Enviroment Gnome
- Added a group of settings for PowerManagement Gnome
- Added a group of settings for Multitasking Gnome
- Added a group of settings for Accessibility Gnome
- Added a group of settings for LockScreen Gnome
- Added a group of settings for Vision Gnome
- Added pam_canonicalize_user control policy
- Improved description of decryption policy
- Improved local administrator name policy
- Improved screensaver mode policy (closes: 44055)

* Thu Mar 06 2025 Valentin Sokolov <sova@altlinux.org> 0.4.0-alt1
- Initial group policies for LAPS
- Added enable LAPS applier policy
- Added chortcuts merge policy

* Fri Feb 28 2025 Valentin Sokolov <sova@altlinux.org> 0.3.1-alt1
- Fix typos in Russian and English translations

* Wed Jan 22 2025 Valentin Sokolov <sova@altlinux.org> 0.3.0-alt1
- Added policies to manage WinBind DNSUpdate service

* Sat Dec 28 2024 Valentin Sokolov <sova@altlinux.org> 0.2.2-alt1
- Changed valuename of TimeoutAutofs policy

* Fri Dec 13 2024 Valentin Sokolov <sova@altlinux.org> 0.2.1-alt1
- Updated setters name in mate_session policies

* Tue Dec 03 2024 Valentin Sokolov <sova@altlinux.org> 0.2.0-alt1
- Added new group policies for Systemd1 polkit actions
- Added new group policies for Machine1 polkit actions
- Added new group policies for TimeDate1 polkit actions
- Added new group policies for ColorManager polkit actions
- Added thunderbird mechanism policy
- Added enviroment variables mechanism policy
- Added policy to enable network directory creation mechanism
- Added KDE screenlocker policy (closes: 50126)
- Added network directories timer unmounted policy
- Added name of drive mount directory policies for machine and user
- Added policy to disable .net prefix in network drive mount directory name
- Added plasma-update policy
- Added force update policy
- Added a policy group to manage the mate session
- Changed descriptions in Polkit sections
- Fix bugs (closes: 50612, 50340, 50012, 49790)

* Mon Mar 04 2024 Valentin Sokolov <sova@altlinux.org> 0.1.13.6-alt1
- Added new group policies for Machine1 polkit actions
- Added new group policies for Login1 polkit actions
- Added new group policies for Realmd polkit actions
- Added new group policies for Udisks2 polkit actions
- Drop policy for /dev/kvm. Drop udev rules and control for /dev/kvm in qemo-8.0.0-alt1
- Drop policy "Vino Vnc password". This functionality is being removed because the password was stored insecurely
- The "package update" policy has been temporarily removed for full analysis and possible implementation
- Fix typos (closes: 46380, 47756, 49263, 49274, 47756, 49302, 49106, 49107, 49139, 49202, 49220, 47138, 49325)

* Tue Jan 16 2024 Valentin Sokolov <sova@altlinux.org> 0.1.13.5-alt1
- Fixed typos in Russian-language policy descriptions (closes: 47671, 46379, 47756, 45808, 42367, 45596)

* Mon Dec 18 2023 Valery Sinelnikov <greh@altlinux.org> 0.1.13.4-alt1
- Fixed language KDE policy blocking key (closes: 48833)

* Thu Nov 30 2023 Valery Sinelnikov <greh@altlinux.org> 0.1.13.3-alt1
- Fix bugs KDE policy (closes: 47996, 47998)

* Tue Oct 31 2023 Valery Sinelnikov <greh@altlinux.org> 0.1.13.2-alt1
- Edited description of blocking
- Edited English version of adml GSettings
- Fixed bugs in ModemManager policies

* Thu Oct 19 2023 Valery Sinelnikov <greh@altlinux.org> 0.1.13.1-alt1
- Polkit-restrictions of ModemManager1 in admx-templates
- Fix polkit translate in russian language
- Fix bugs (closes: 47973, 47985, 47987, 47743, 47990, 47818, 48002)

* Tue Sep 19 2023 Valery Sinelnikov <greh@altlinux.org> 0.1.13.0-alt1
- Added a section for user and machine policies to configure
  the graphical environment of KDE Plasma
- Added KDE Applier Enable policy
- Fix supportedOn defenitions to use ranges instead of references
- Added closure policy in admx-basealt

* Thu Jun 15 2023 Valery Sinelnikov <greh@altlinux.org> 0.1.12.6-alt1
- Added new admx-files for polkit-actions to NetworkManager and pcsc_lite

* Thu May 11 2023 Valery Sinelnikov <greh@altlinux.org> 0.1.12.5-alt1
- Fix typos in PolKit adml files
- Fixed descriptions for samba usershares policies

* Mon Apr 03 2023 Valery Sinelnikov <greh@altlinux.org> 0.1.12.4-alt1
- Fix typos in adml files (closes: 42365)
- Changed policy definition to "Mechanism for copying files"
- Fixed policy "General mount policy".

* Thu Mar 09 2023 Evgeny Sinelnikov <sin@altlinux.org> 0.1.12.3-alt1
- Fix typos in adml files (closes: 42355, 42365, 42358).

* Fri Mar 03 2023 Valery Sinelnikov <greh@altlinux.org> 0.1.12.2-alt1
- Added new admx for samba usershare controls
- Added new group policies for PackageKit polkit actions
- Added new group policies for Udisks2 polkit actions
- Add machine policies for drive maps
- Added file copy mechanism configuration policy

* Thu Dec 29 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.1.12.1-alt1
- Add user policies for drive maps symlinks in home directory.
- Add warning when disabling network manager.
- Fix correction of option name open ldap tls connections in russian.
- Fix typo in cups.service

* Tue Dec 13 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.1.12-alt1
- Add control for Yandex Browser group policies mechanism.
- Improve group policies mechanisms display names and help descriptions.

* Mon Oct 24 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.1.11.2-alt1
- Fix en_US adml for script execution module for users policy.

* Wed Sep 07 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.1.11.1-alt1
- Fix machine part of file-copy group policy engine.

* Fri Aug 26 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.1.11-alt1
- Fix ability to block a disabled Mate policies.
- Fix error loading templates in gpedit.
- Add file-copy, ini-files and script policies gpupdate engines.
- Add ScrollSysvolDC policy.

* Wed Mar 02 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.1.10-alt1
- Correct adml definitions for controls and group policies.
- Update machine and user packages settings.
- Add Gsettings for windows manager Marco.
- Add policies for local users support.
- Add Simply Linux 10 as BaseALT product.

* Fri Oct 22 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.1.9-alt1
- Fixed typo in screensaver setting in Russian translations
- Improve English translation of gsettings strings
- Fix authetication method bug for gsetting oprtion:
  org.gnome.Vino.authentication-methods

* Mon Oct 04 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.1.8-alt1
- Fix typos in Russian translations

* Mon Sep 20 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.1.7-alt1
- Added remote settings category and Vino settngs:
 + authentication-methods and vnc-password;
 + use-alternative-port and alternative-port;
 + view-only, prompt-enabled, icon-visibility and enabled.

* Sun Sep 12 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.1.6-alt1
- Added new categories and policies for Mate settings:
 + background;
 + screensaver;
 + user restrictions.

* Sun Jul 18 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.1.5-alt1
- Add new categories and policies:
 + SSHD and Systemd categories
 + Windows policies mapping support (applied for GSettings only yet)
- Add admx and adml files checking via admx-lint

* Tue Mar 23 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.1.4-alt1
- Add sssd controls in separate category

* Sat Sep 12 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.1.3-alt1
- Add sshd-allow-groups-list
- Fix authentication method (system-auth) selection and some number of typos

* Wed Sep 09 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.1.2-alt1
- Add sshd-permit-root-login control
- Fix in basealtcontrol ADML
- Fix tcb_chkpwd_restricted to root
- Fix duplicate naming (Accounts service)
- NTP Applier switch added

* Wed Jul 01 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.1.1-alt1
- Update admx according to gpupdate-0.7.0 release

* Mon May 18 2020 Rustem Bapin <rbapin@altlinux.org> 0.1.0-alt1
- Initial release
