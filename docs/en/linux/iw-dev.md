---
layout: page
title: linux/iw-dev (English)
description: "Show and manipulate wireless devices."
content_hash: da96e34d2747e0e5d7f876395e1a553ee4f29cb2
last_modified_at: 2024-10-12
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/iw-dev.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># iw dev

Show and manipulate wireless devices.
For a list of channels, frequencies and reg information: <https://wireless.docs.kernel.org/en/latest/en/developers/documentation/channellist.html>.
More information: <https://wireless.docs.kernel.org/en/latest/en/users/documentation/iw.html>.

- Set device to monitor mode (interface must be down first. See also `ip link`):

`sudo iw dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlp</span>` set type monitor`

- Set device to managed mode (interface must be down first):

`sudo iw dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlp</span>` set type managed`

- Set device WiFi channel (device must first be in monitor mode with the interface up):

`sudo iw dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlp</span>` set channel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">channel_number</span>

- Set device WiFi frequency in Mhz (device must first be in monitor mode with the interface up):

`sudo iw dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlp</span>` set freq `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">freq_in_mhz</span>

- Show all known station info:

`iw dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlp</span>` station dump`

- Create a virtual interface in monitor mode with a specific MAC address:

`sudo iw dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlp</span>` interface add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vif_name</span>`" type monitor addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">12:34:56:aa:bb:cc</span>

- Delete virtual interface:

`sudo iw dev "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vif_name</span>`" del`
