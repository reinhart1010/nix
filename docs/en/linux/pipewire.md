---
layout: page
title: linux/pipewire (English)
description: "Start the PipeWire daemon."
content_hash: fdd898aed0f3b727050870a3598d73cf2604a1be
last_modified_at: 2023-12-27
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pipewire.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pipewire

Start the PipeWire daemon.
More information: <https://docs.pipewire.org/page_man_pipewire_1.html>.

- Start the PipeWire daemon:

`pipewire`

- Use a different configuration file:

`pipewire --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.conf</span>

- Set the verbosity level (error, warn, info, debug or trace):

`pipewire -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">v|vv|...|vvvvv</span>

- Display help:

`pipewire --help`
