---
layout: page
title: linux/cgclassify (English)
description: "Move running task(s) to given `cgroups`."
content_hash: 7c20f5f0b9d174d97719b62b3efc618596dafca3
last_modified_at: 2023-11-26
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/cgclassify.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cgclassify

Move running task(s) to given `cgroups`.
More information: <https://manned.org/cgclassify>.

- Move the process with a specific PID to the control group student in the CPU hierarchy:

`cgclassify -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu:student</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>

- Move the process with a specific PID to control groups based on the `/etc/cgrules.conf` configuration file:

`cgclassify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>

- Move the process with a specific PID to the control group student in the CPU hierarchy. Note: The daemon of the service `cgred` does not change `cgroups` of the specific PID and its children (based on `/etc/cgrules.conf`):

`cgclassify --sticky -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu:/student</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>
