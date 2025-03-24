%global debug_package ${nil}
%global __os_install_post ${nil}
%define _build_id_links none

Name: sass
Version: 1.86.0
Release: 1
Summary: The reference implementation of Sass, written in Dart
License: MIT
URL: https://sass-lang.com/dart-sass
Source0: https://github.com/sass/dart-sass/archive/refs/tags/%{version}.tar.gz
Source1: dart-pub-cache.tar.gz

BuildRequires: dart git lib64buf

%description
Dart Sass is the primary implementation of Sass, which means it gets new
features before any other implementation. It's fast, easy to install, and it
compiles to pure JavaScript which makes it easy to integrate into modern web
development workflows.

%prep
%setup -q -n dart-sass-%{version}
tar -zxf %{SOURCE1} -C .
dart pub get --offline

%build

dart run grinder protobuf
dart compile exe ./bin/sass.dart -o sass

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 sass %{buildroot}%{_bindir}/sass

%files
%{_bindir}/sass
%license LICENSE
%doc README.md
