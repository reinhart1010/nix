---
layout: page
title: linux/dbus-daemon (English)
description: "The D-Bus message daemon, allowing multiple programs to exchange messages."
content_hash: 7d966a7d62f7e34dccc795a47fcf25b07fa28573
---
# dbus-daemon

The D-Bus message daemon, allowing multiple programs to exchange messages.
More information: <https://www.freedesktop.org/wiki/Software/dbus/>.

- Run the daemon with a configuration file:

`dbus-daemon --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Run the daemon with the standard per-login-session message bus configuration:

`dbus-daemon --session`

- Run the daemon with the standard systemwide message bus configuration:

`dbus-daemon --system`

- Set the address to listen on and override the configuration value for it:

`dbus-daemon --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address</span>

- Output the process ID to stdout:

`dbus-daemon --print-pid`

- Force the message bus to write to the system log for messages:

`dbus-daemon --syslog`
