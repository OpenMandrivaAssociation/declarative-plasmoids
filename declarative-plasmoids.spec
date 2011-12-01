Name:    declarative-plasmoids
Summary: Declarative plasmoids for the plasma desktop and mobile
Version: 4.8
Release: 1
Group:   Graphical desktop/KDE
License: LGPLv2
URL:     http://www.kde.org/
Source:  ftp://ftp.kde.org/pub/kde/stable/active/1.0/src/%{name}-%version.tar.bz2

BuildArch: noarch


%description
Declarative plasmoids for the plasma desktop and mobile

%files
%_kde_datadir/applications/kde4/active-microblog.desktop
%_kde_datadir/applications/kde4/active-news-reader.desktop
%_kde_appsdir/plasma/plasmoids/org.kde.analogclock
%_kde_appsdir/plasma/plasmoids/org.kde.dictionary-qml
%_kde_appsdir/plasma/plasmoids/org.kde.knowledgebase
%_kde_appsdir/plasma/plasmoids/org.kde.microblog-qml
%_kde_appsdir/plasma/plasmoids/org.kde.news-qml
%_kde_appsdir/plasma/plasmoids/org.kde.rssnow-qml
%_kde_appsdir/plasma/plasmoids/org.kde.social-news-qml
%_kde_datadir/icons/hicolor/128x128/apps/active-news.png
%_kde_datadir/icons/hicolor/16x16/apps/active-news.png
%_kde_datadir/icons/hicolor/32x32/apps/active-news.png
%_kde_datadir/icons/hicolor/48x48/apps/active-news.png
%_kde_datadir/icons/hicolor/64x64/apps/active-news.png
%_kde_datadir/icons/hicolor/scalable/apps/active-news.svgz
%_kde_datadir/kde4/services/plasma-applet-analog-clock.desktop
%_kde_datadir/kde4/services/plasma-applet-dictionary-qml.desktop
%_kde_datadir/kde4/services/plasma-applet-knowledgebase-qml.desktop
%_kde_datadir/kde4/services/plasma-applet-microblog-qml.desktop
%_kde_datadir/kde4/services/plasma-applet-news-qml.desktop
%_kde_datadir/kde4/services/plasma-applet-social-news-qml.desktop
%_kde_datadir/kde4/services/plasma-applet-rssnow-qml.desktop

#----------------------------------------------------------------------

%prep
%setup -q 
%apply_patches

%build
%cmake_kde4
	
%make

%install
%makeinstall_std -C build

