---
layout: page
title: common/atoum (English)
description: "A simple, modern and intuitive unit testing framework for PHP."
content_hash: 6c77b7d28f53558bb678db0d0adec7a53047b19a
last_modified_at: 2023-11-12
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
More information: <http://atoum.org>.

- Initialize a configuration file:

`atoum --init`

- Run all tests:

`atoum`

- Run tests using the specified configuration file:

`atoum -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Run a specific test file:

`atoum -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Run a specific directory of tests:

`atoum -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Run all tests under a specific namespace:

`atoum -ns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Run all tests with a specific tag:

`atoum -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Load a custom bootstrap file before running tests:

`atoum --bootstrap-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
