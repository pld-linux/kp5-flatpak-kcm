#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	5.27.9
%define		qtver		5.15.2
%define		kpname		flatpak-kcm

Summary:	KDE Config Module for flatpak
Name:		kp5-%{kpname}
Version:	5.27.9
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	1f6c592fcab06f8043c0dbd95f87633f
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 3.16.0
BuildRequires:	flatpak-devel
BuildRequires:	kf5-kauth-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KDE Config Module for flatpak.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir}
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_flatpak.so
%{_desktopdir}/kcm_flatpak.desktop
%dir %{_datadir}/kpackage/kcms/kcm_flatpak
%dir %{_datadir}/kpackage/kcms/kcm_flatpak/contents
%dir %{_datadir}/kpackage/kcms/kcm_flatpak/contents/ui
%{_datadir}/kpackage/kcms/kcm_flatpak/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_flatpak/contents/ui/permissions.qml
%{_datadir}/kpackage/kcms/kcm_flatpak/contents/ui/KcmPopupModal.qml
%{_datadir}/kpackage/kcms/kcm_flatpak/contents/ui/AddEnvironmentVariableDialog.qml
%{_datadir}/kpackage/kcms/kcm_flatpak/contents/ui/TextPromptDialog.qml
