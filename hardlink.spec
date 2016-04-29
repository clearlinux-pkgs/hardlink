#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hardlink
Version  : 0.3.0
Release  : 3
URL      : http://jak-linux.org/projects/hardlink/hardlink_0.3.0.tar.xz
Source0  : http://jak-linux.org/projects/hardlink/hardlink_0.3.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: hardlink-bin
Requires: hardlink-doc
BuildRequires : attr-dev

%description
=====================
hardlink is a tool which replaces multiple copies of a file with hardlinks.
Inspiration came from http://code.google.com/p/hardlinkpy/, but no code has
been used.

%package bin
Summary: bin components for the hardlink package.
Group: Binaries

%description bin
bin components for the hardlink package.


%package doc
Summary: doc components for the hardlink package.
Group: Documentation

%description doc
doc components for the hardlink package.


%prep
%setup -q -n hardlink-0.3.0

%build
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/hardlink

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
