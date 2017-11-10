Name: googletest
Version: 0
Release: 0
Summary: Lib for unit testing
Source: %{name}-%{version}.tar.gz
License: TODO
BuildRequires: cmake

%description
Lib for unit testing

%prep

%setup -q -n %{name}-%{version}

%build
cmake \
 -DCMAKE_INSTALL_PREFIX=/usr \
 .

%__make

echo "TODO: make_install to preserve static lib"
rpm --eval '%make_install'
make install DESTDIR=%{buildroot}
touch debugsources.list

%clean

%files
%{_includedir}/*
%{_libdir}/*
