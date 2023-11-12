---
layout: page
title: linux/goaccess (English)
description: "An open source real-time web log analyzer."
content_hash: bb5fb57a0cfc4fc6b7b224d503e539f0eeb0acd8
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# goaccess

An open source real-time web log analyzer.
More information: <https://goaccess.io>.

- Analyze one or more log files in interactive mode:

`goaccess `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/logfile1 path/to/file2 ...</span>

- Use a specific log-format (or pre-defined formats like "combined"):

`goaccess `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/logfile</span>` --log-format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">format</span>

- Analyze a log from `stdin`:

`tail -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/logfile</span>` | goaccess -`

- Analyze a log and write it to an HTML file in real-time:

`goaccess `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/logfile</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.html</span>` --real-time-html`
