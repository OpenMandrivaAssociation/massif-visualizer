Name:           massif-visualizer
Summary:        Tool for visualizing massif data
Version:        25.08.1
Release:        1
License:        GPLv2
Group:          Graphical desktop/KDE
Url:            https://cgit.kde.org/massif-visualizer.git
Source0:        http://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  cmake(ECM)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Parts)
BuildRequires:	cmake(KChart6)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Core5Compat)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6PrintSupport)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Test)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(shared-mime-info)
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Massif Visualizer is a tool that - *who would guess that* - visualizes massif
data. You run your application in Valgrind with `--tool=massif` and the open
the generated `massif.out.pid` in this application. You can also compress the
log with Gzip or Bzip2 and open it transparently with the visualizer.


%files -f %{name}.lang
%doc AUTHORS COPYING
%{_bindir}/%{name}
%{_datadir}/applications/org.kde.%{name}.desktop
%{_datadir}/metainfo/org.kde.%{name}.appdata.xml
%{_datadir}/%{name}/
%{_datadir}/config.kcfg/%{name}-settings.kcfg
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/mime/packages/massif.xml
