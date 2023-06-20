Name:           mimetic
Version:        0.9.8
Release:        2
Summary:        A full featured C++ MIME library
License:        MIT
URL:            http://www.codesink.org/mimetic_mime_library.html

Source0:        http://www.codesink.org/download/mimetic-%{version}.tar.gz
Patch0:         mimetic-%{version}-signedness-fix.patch
Patch1:         mimetic-gcc11.patch
%if "%toolchain"=="clang"
Patch2:         fix-clang.patch
%endif
BuildRequires:  gcc-c++
BuildRequires:  doxygen
BuildRequires:  findutils
BuildRequires:  make

%description
mimetic is an Email library (MIME) written in C++ designed to be easy to use 
and integrate but yet fast and efficient.

It has been built around the standard lib. This means that you'll not find yet
another string class or list implementation and that you'll feel comfortable 
in using this library from the very first time. 

Most classes functionalities and behavior will be clear if you ever studied 
MIME and its components; if you don't know anything about Internet messages 
you'll probably want to read some RFCs to understand the topic and, therefore,
easily use the library whose names, whenever possible, overlap terms adopted 
in the standard RFC documents. At the very least: RFC 822, RFC 2045 and RFC 
2046.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
export CFLAGS+="$CFLAGS -Wno-reserved-user-defined-literal"
%configure --disable-static
make %{?_smp_mflags}
make docs -C doc

%install
%make_install
find %{buildroot} -name '*.*a' -delete -print

%check
make check

%ldconfig_scriptlets

%files
%license COPYING LICENSE
%doc AUTHORS ChangeLog README
%{_libdir}/libmimetic.so.*

%files devel
%doc doc/html/*
%{_includedir}/mimetic/
%{_libdir}/libmimetic.so

%changelog
* Mon Jun 19 2023 zhangxiang <zhangxiang@iscas.ac.cn> - 0.9.8-2
- Fix clang build error

* Mon Jul 25 2022 loong_C <loong_c@yeah.net> - 0.9.8-1
- Initial Package.
