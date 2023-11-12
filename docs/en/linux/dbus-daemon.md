---
layout: page
title: linux/dbus-daemon (English)
description: "The D-Bus message daemon, allowing multiple programs to exchange messages."
content_hash: 052eca8c4b1e6d5ad84105bd3fd7e11d72894283
last_modified_at: 2023-11-12
tldri18n_status: 2
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

- Output the process ID to `stdout`:

`dbus-daemon --print-pid`

- Force the message bus to write to the system log for messages:

`dbus-daemon --syslog`
