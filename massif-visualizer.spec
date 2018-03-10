Name:           massif-visualizer
Summary:        Tool for visualizing massif data
Version:        0.7.0
Release:        1
License:        GPLv2
Group:          Graphical desktop/KDE
Url:            https://cgit.kde.org/massif-visualizer.git
Source0:        http://download.kde.org/stable/massif-visualizer/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  cmake(ECM)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KChart)
BuildRequires:  cmake(KGraphViewerPart)
BuildRequires:  qt5-qttools
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5XmlPatterns)

BuildRequires:  pkgconfig(shared-mime-info)

%description
Massif Visualizer is a tool that - *who would guess that* - visualizes massif
data. You run your application in Valgrind with `--tool=massif` and the open
the generated `massif.out.pid` in this application. You can also compress the
log with Gzip or Bzip2 and open it transparently with the visualizer.


%files -f %{name}.lang
%doc AUTHORS COPYING
%{_kde5_bindir}/%{name}
%{_kde5_datadir}/applications/org.kde.%{name}.desktop
%{_kde5_datadir}/metainfo/org.kde.%{name}.appdata.xml
%{_kde5_datadir}/%{name}/
%{_kde5_datadir}/kxmlgui5/%{name}/
%{_kde5_configdir}.kcfg/%{name}-settings.kcfg
%{_kde5_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_kde5_datadir}/mime/packages/massif.xml

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build

%find_lang %{name} --all-name

