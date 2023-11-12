---
layout: page
title: common/qdbus (English)
description: "Inter-Process Communication (IPC) and Remote Procedure Calling (RPC) mechanism originally developed for Linux."
content_hash: 7cf03447a47e6c563cd87604a14517bb43b72053
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# qdbus

Inter-Process Communication (IPC) and Remote Procedure Calling (RPC) mechanism originally developed for Linux.
More information: <https://doc.qt.io/qt-5/qtdbus-index.html>.

- List available service names:

`qdbus`

- List object paths for a specific service:

`qdbus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>

- List methods, signals and properties available on a specific object:

`qdbus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/object</span>

- Execute a specific method passing arguments and display the returned value:

`qdbus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/object</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">method_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument2</span>

- Display the current brightness value in a KDE Plasma session:

`qdbus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.kde.Solid.PowerManagement</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/org/kde/Solid/PowerManagement/Actions/BrightnessControl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.kde.Solid.PowerManagement.Actions.BrightnessControl.brightness</span>

- Set a specific brightness to a KDE Plasma session:

`qdbus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.kde.Solid.PowerManagement</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/org/kde/Solid/PowerManagement/Actions/BrightnessControl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.kde.Solid.PowerManagement.Actions.BrightnessControl.setBrightness</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5000</span>

- Invoke volume up shortcut in a KDE Plasma session:

`qdbus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.kde.kglobalaccel</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/component/kmix</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">invokeShortcut</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">increase_volume</span>`"`

- Gracefully log out and then do nothing, reboot or shut down:

`qdbus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.kde.Shutdown</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/Shutdown</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">logout|logoutAndReboot|logoutAndShutdown</span>
