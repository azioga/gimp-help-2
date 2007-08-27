%define gimp_help_dir %{_datadir}/gimp/2.0/help

Summary: Help files for Gimp2
Name:    gimp-help-2
Version: 0.13
Release: %mkrel 3
Source0: ftp://ftp.gimp.org/pub/gimp/help/%name-%version.tar.bz2
License: GFDL
Group: Books/Other
Url: http://docs.gimp.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libxslt-proc
BuildRequires: libxml2-utils
BuildRequires: docbook-style-xsl
BuildRequires: docbook-dtd43-xml
BuildRequires: gnome-doc-utils
BuildArch: noarch

%description
This is the new HTML help for Gimp 2.

# -----------------------------------------------------
%package common
Summary: Common files for Gimp2 help
Group: Books/Other
Conflicts: %name < 0.13-2

%description common
This package contains common files for Gimp2 help.

%files common
%defattr(-,root,root)
%doc AUTHORS NEWS README HACKING TERMINOLOGY
%dir %gimp_help_dir/images
%gimp_help_dir/images/*.png
%gimp_help_dir/images/callouts/

%dir %gimp_help_dir/images/dialogs/
%gimp_help_dir/images/dialogs/*.png
%gimp_help_dir/images/dialogs/examples/

%dir %gimp_help_dir/images/filters/
%gimp_help_dir/images/filters/*.*

%dir %gimp_help_dir/images/filters/examples/
%gimp_help_dir/images/filters/examples/*.*

%gimp_help_dir/images/glossary/

%dir %gimp_help_dir/images/math
%gimp_help_dir/images/math/*.png

%dir %gimp_help_dir/images/menus/
%gimp_help_dir/images/menus/*.png

%dir %gimp_help_dir/images/preferences/
%gimp_help_dir/images/preferences/*.png

%dir %gimp_help_dir/images/tool-options/
%gimp_help_dir/images/tool-options/*.png

%dir %gimp_help_dir/images/toolbox
%gimp_help_dir/images/toolbox/*.png

%dir %gimp_help_dir/images/tutorials
%gimp_help_dir/images/tutorials/*.*

%dir %gimp_help_dir/images/using
%gimp_help_dir/images/using/*.*

# -----------------------------------------------------
%package cs
Summary: Czech translation of Gimp2 help
Group: Books/Other
Requires: locales-cs
Requires: %name-common = %version-%release
Provides: %name = %version-%release
Obsoletes: %name < 0.13
Conflicts: %name < 0.13-2

%description cs
This package conatians Czech translation of Gimp2 help.

%files cs
%defattr(-,root,root)
%gimp_help_dir/images/*/cs
%gimp_help_dir/cs

# -----------------------------------------------------
%package de
Summary: German translation of Gimp2 help
Group: Books/Other
Requires: locales-de
Requires: %name-common = %version-%release
Provides: %name = %version-%release
Obsoletes: %name < 0.13
Conflicts: %name < 0.13-2

%description de
This package conatians German translation of Gimp2 help.

%files de
%defattr(-,root,root)
%gimp_help_dir/images/*/de
%gimp_help_dir/images/filters/examples/de
%gimp_help_dir/de

# -----------------------------------------------------
%package en
Summary: English translation of Gimp2 help
Group: Books/Other
Requires: locales-en
Requires: %name-common = %version-%release
Provides: %name = %version-%release
Obsoletes: %name < 0.13
Conflicts: %name < 0.13-2

%description en
This package conatians Spanish translation of Gimp2 help.

%files en
%defattr(-,root,root)
%gimp_help_dir/images/filters/examples/en
%gimp_help_dir/en

# -----------------------------------------------------
%package es
Summary: Spanish translation of Gimp2 help
Group: Books/Other
Requires: locales-es
Requires: %name-common = %version-%release
Provides: %name = %version-%release
Obsoletes: %name < 0.13
Conflicts: %name < 0.13-2

%description es
This package conatians Spanish translation of Gimp2 help.

%files es
%defattr(-,root,root)
%gimp_help_dir/images/*/es
%gimp_help_dir/es

# -----------------------------------------------------
%package fr
Summary: French translation of Gimp2 help
Group: Books/Other
Requires: locales-fr
Requires: %name-common = %version-%release
Provides: %name = %version-%release
Obsoletes: %name < 0.13
Conflicts: %name < 0.13-2

%description fr
This package conatians French translation of Gimp2 help.

%files fr
%defattr(-,root,root)
%gimp_help_dir/images/*/fr
%gimp_help_dir/images/filters/examples/fr
%gimp_help_dir/fr

# -----------------------------------------------------
%package hr
Summary: Croatian translation of Gimp2 help
Group: Books/Other
Requires: locales-hr
Requires: %name-common = %version-%release
Provides: %name = %version-%release
Obsoletes: %name < 0.13
Conflicts: %name < 0.13-2

%description hr
This package conatians Croatian translation of Gimp2 help.

%files hr
%defattr(-,root,root)
%gimp_help_dir/images/*/hr
%gimp_help_dir/hr

# -----------------------------------------------------
%package it
Summary: Italian translation of Gimp2 help
Group: Books/Other
Requires: locales-it
Requires: %name-common = %version-%release
Provides: %name = %version-%release
Obsoletes: %name < 0.13
Conflicts: %name < 0.13-2

%description it
This package conatians Italian translation of Gimp2 help.

%files it
%defattr(-,root,root)
%gimp_help_dir/images/*/it
%gimp_help_dir/images/filters/examples/it
%gimp_help_dir/it

# -----------------------------------------------------
%package ko
Summary: Korean translation of Gimp2 help
Group: Books/Other
Requires: locales-ko
Requires: %name-common = %version-%release
Provides: %name = %version-%release
Obsoletes: %name < 0.13
Conflicts: %name < 0.13-2

%description ko
This package conatians Korean translation of Gimp2 help.

%files ko
%defattr(-,root,root)
%gimp_help_dir/images/*/ko
%gimp_help_dir/ko

# -----------------------------------------------------
%package nl
Summary: Dutch translation of Gimp2 help
Group: Books/Other
Requires: locales-nl
Requires: %name-common = %version-%release
Provides: %name = %version-%release
Obsoletes: %name < 0.13
Conflicts: %name < 0.13-2

%description nl
This package conatians Dutch translation of Gimp2 help.

%files nl
%defattr(-,root,root)
%gimp_help_dir/images/*/nl
%gimp_help_dir/nl

# -----------------------------------------------------
%package no
Summary: Norwegian translation of Gimp2 help
Group: Books/Other
Requires: locales-no
Requires: %name-common = %version-%release
Provides: %name = %version-%release
Obsoletes: %name < 0.13
Conflicts: %name < 0.13-2

%description no
This package conatians Norwegian translation of Gimp2 help.

%files no
%defattr(-,root,root)
%gimp_help_dir/images/*/no
%gimp_help_dir/images/filters/examples/no
%gimp_help_dir/no

# -----------------------------------------------------
%package ru
Summary: Russian translation of Gimp2 help
Group: Books/Other
Requires: locales-ru
Requires: %name-common = %version-%release
Provides: %name = %version-%release
Obsoletes: %name < 0.13
Conflicts: %name < 0.13-2

%description ru
This package conatians Russian translation of Gimp2 help.

%files ru
%defattr(-,root,root)
%gimp_help_dir/images/*/ru
%gimp_help_dir/ru

# -----------------------------------------------------
%package sv
Summary: Swidish translation of Gimp2 help
Group: Books/Other
Requires: locales-sv
Requires: %name-common = %version-%release
Provides: %name = %version-%release
Obsoletes: %name < 0.13
Conflicts: %name < 0.13-2

%description sv
This package conatians Swedish translation of Gimp2 help.

%files sv
%defattr(-,root,root)
#%gimp_help_dir/images/*/sv
%gimp_help_dir/sv

# -----------------------------------------------------
%package zh_CN
Summary: Simplified Chinese translation of Gimp2 help
Group: Books/Other
Requires: locales-zh
Requires: %name-common = %version-%release
Provides: %name = %version-%release
Obsoletes: %name < 0.13
Conflicts: %name < 0.13-2

%description zh_CN
This package conatians Simplified Chinese translation of Gimp2 help.

%files zh_CN
%defattr(-,root,root)
%gimp_help_dir/images/*/zh_CN
%gimp_help_dir/zh_CN

# -----------------------------------------------------

%prep
%setup -q

%build
%configure2_5x --without-gimp
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT
