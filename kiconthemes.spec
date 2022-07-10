%define major 5
%define libname %mklibname KF5IconThemes %{major}
%define devname %mklibname KF5IconThemes -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kiconthemes
Version:	5.96.0
Release:	1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 Icon theme library
URL: http://kde.org/
License: LGPL v2.1
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5ItemViews)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: cmake(Qt5UiPlugin)
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant
Requires: %{libname} = %{EVRD}
Requires: hicolor-icon-theme

%description
The KDE Frameworks 5 Icon theme library.

%package -n %{libname}
Summary: The KDE Frameworks 5 Icon theme library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
The KDE Frameworks 5 Icon theme library.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Requires: %{name} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%package designer
Summary: Qt Designer plugin for handling %{name} widgets
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description designer
Qt Designer plugin for handling %{name} widgets

%files designer
%{_libdir}/qt5/plugins/designer/*.so

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kiconthemes%{major}

%files -f kiconthemes%{major}.lang
%{_bindir}/*
%{_datadir}/qlogging-categories5/*.*categories

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}
%{_libdir}/qt5/plugins/iconengines/*.so

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
