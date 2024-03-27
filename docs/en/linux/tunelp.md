---
layout: page
title: linux/tunelp (English)
description: "Set various parameters for parallel port devices for troubleshooting or for better performance."
content_hash: 8ea16ad46dec81e764f28b431fdeb2335644a225
last_modified_at: 2024-03-27
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/tunelp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tunelp

Set various parameters for parallel port devices for troubleshooting or for better performance.
Part of `util-linux`.
More information: <https://manned.org/tunelp>.

- Check the [s]tatus of a parallel port device:

`tunelp --status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/lp0</span>

- [r]eset a given parallel port:

`tunelp --reset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/lp0</span>

- Use a given [i]RQ for a device, each one representing an interrupt line:

`tunelp -i 5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/lp0</span>

- Try a given number of times to output a [c]haracter to the printer before sleeping for a given [t]ime:

`tunelp --chars `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">times</span>` --time `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">time_in_centiseconds</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/lp0</span>

- Enable or disable [a]borting on error (disabled by default):

`tunelp --abort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>
