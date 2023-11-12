---
layout: page
title: common/pprof (English)
description: "Command-line tool for visualization and analysis of profile data."
content_hash: ce6389e253295bc2b130e0a8e2673cb57f023c0d
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pprof

Command-line tool for visualization and analysis of profile data.
More information: <https://github.com/google/pprof>.

- Generate a text report from a specific profiling file, on fibbo binary:

`pprof -top `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./fibbo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./fibbo-profile.pb.gz</span>

- Generate a graph and open it on a web browser:

`pprof -svg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./fibbo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./fibbo-profile.pb.gz</span>

- Run pprof in interactive mode to be able to manually launch `pprof` on a file:

`pprof `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./fibbo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./fibbo-profile.pb.gz</span>

- Run a web server that serves a web interface on top of `pprof`:

`pprof -http=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">localhost:8080</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./fibbo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./fibbo-profile.pb.gz</span>

- Fetch a profile from an HTTP server and generate a report:

`pprof `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://localhost:8080/debug/pprof</span>
