Name:           sjasmplus
Version:        1.21.0
Release:        1%{?dist}
Summary:        Cross-assembler for Z80 CPU

License:        MIT
URL:            https://github.com/z00m128/sjasmplus
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-unbundle-LuaBridge.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  LuaBridge-devel
BuildRequires:  unittest-cpp-devel


%description
Command-line cross-compiler of assembly language for Z80 CPU.


%prep
%autosetup -p1


%build
%cmake -DSYSTEM_LUA=ON
%cmake_build %{?_smp_mflags}


%install
%cmake_install


%check
cd %__cmake_builddir
LANG=en_US.UTF-8 make tests


%files
%license LICENSE.md
%doc README.md CHANGELOG.md
%{_bindir}/%{name}


%changelog
* Mon Mar 17 2025 Dan Horák <dan@danny.cz> - 1.21.0-1
- updated to 1.21.0

* Wed Jun 28 2023 Dan Horák <dan@danny.cz> - 1.20.3-1
- updated to 1.20.3

* Thu Feb 16 2023 Dan Horák <dan@danny.cz> - 1.20.2-1
- updated to 1.20.2

* Fri Jul 29 2022 Dan Horák <dan@danny.cz> - 1.20.1-1
- updated to 1.20.1

* Fri Jul 08 2022 Dan Horák <dan@danny.cz> - 1.20.0-1
- initial Fedora version
