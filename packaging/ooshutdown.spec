Name:           ooshutdown
Version:        0.1.0
Release:        1%{?dist}
Summary:        Schedules system shutdown, poweroff, or halt via systemd logind IPC.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooshutdown
Source0:        ooshutdown-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooshutdown is a sovereign, capability-bounded POWER CONTROLLER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooshutdown
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooshutdown-uninstall

%files
/usr/bin/ooshutdown
/usr/bin/ooshutdown-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
