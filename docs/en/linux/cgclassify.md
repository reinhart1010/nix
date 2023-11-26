---
layout: page
title: linux/cgclassify (English)
description: "Move running task(s) to given `cgroups`."
content_hash: 7c20f5f0b9d174d97719b62b3efc618596dafca3
last_modified_at: 2023-11-26
related_topics:
  - title: Nederlands version
    url: /nl/linux/cgclassify.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cgclassify

Move running task(s) to given `cgroups`.
More information: <https://manned.org/cgclassify>.

- Move the process with a specific PID to the control group student in the CPU hierarchy:

`cgclassify -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu:student</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>

- Move the process with a specific PID to control groups based on the `/etc/cgrules.conf` configuration file:

`cgclassify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>

- Move the process with a specific PID to the control group student in the CPU hierarchy. Note: The daemon of the service `cgred` does not change `cgroups` of the specific PID and its children (based on `/etc/cgrules.conf`):

`cgclassify --sticky -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu:/student</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>
