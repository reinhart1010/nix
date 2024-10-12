---
layout: page
title: common/atoum (English)
description: "A simple, modern and intuitive unit testing framework for PHP."
content_hash: 7d722810ee66ca8745f48dcca200e72decf1be9f
last_modified_at: 2024-10-12
related_topics:
  - title: español version
    url: /es/common/atoum.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/atoum.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/atoum.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/atoum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# atoum

A simple, modern and intuitive unit testing framework for PHP.
More information: <https://atoum.org>.

- Initialize a configuration file:

`atoum --init`

- Run all tests:

`atoum`

- Run tests using the specified [c]onfiguration file:

`atoum -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Run a specific test [f]ile:

`atoum -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Run a specific [d]irectory of tests:

`atoum -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Run all tests under a specific name[s]pace:

`atoum -ns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Run all tests with a specific [t]ag:

`atoum -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Load a custom bootstrap file before running tests:

`atoum --bootstrap-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
