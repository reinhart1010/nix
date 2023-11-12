---
layout: page
title: linux/http_load (English)
description: "An HTTP benchmarking tool."
content_hash: 5bdedf540af85c321ae6b3425217712bf1b6ab92
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# http_load

An HTTP benchmarking tool.
Runs multiple HTTP fetches in parallel to test the throughput of a web server.
More information: <http://www.acme.com/software/http_load/>.

- Emulate 20 requests based on a given URL list file per second for 60 seconds:

`http_load -rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>` -seconds `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/urls.txt</span>

- Emulate 5 concurrent requests based on a given URL list file for 60 seconds:

`http_load -parallel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -seconds `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/urls.txt</span>

- Emulate 1000 requests at 20 requests per second, based on a given URL list file:

`http_load -rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>` -fetches `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/urls.txt</span>

- Emulate 1000 requests at 5 concurrent requests at a time, based on a given URL list file:

`http_load -parallel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -fetches `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/urls.txt</span>
