---
layout: page
title: linux/protonvpn (English)
description: "Unofficial third-party ProtonVPN client."
content_hash: 8345d4038b8f045c6463732bc3983e81bff4ec11
last_modified_at: 2024-10-02
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/protonvpn.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># protonvpn

Unofficial third-party ProtonVPN client.
See also: `protonvpn-connect`.
More information: <https://github.com/Rafficer/linux-cli-community>.

- Initialize ProtonVPN profile:

`protonvpn init`

- Connect to ProtonVPN interactively:

`protonvpn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c|connect</span>

- Display connection status:

`protonvpn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s|status</span>

- Disconnect from ProtonVPN:

`protonvpn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">d|disconnect</span>

- Reconnect or connect to the last server used:

`protonvpn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">r|reconnect</span>

- Refresh OpenVPN configuration and server data:

`protonvpn refresh`

- Display help for a subcommand:

`protonvpn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` --help`
