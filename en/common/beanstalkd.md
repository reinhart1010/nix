---
layout: page
title: common/beanstalkd (English)
description: "A simple and generic work-queue server."
content_hash: faf32020054f1381bc24e5a0be7f6b1e62a4f00c
related_topics:
  - title: italiano version
    url: /it/common/beanstalkd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/beanstalkd.html
    icon: bi bi-globe
---
# beanstalkd

A simple and generic work-queue server.
More information: <https://beanstalkd.github.io/>.

- Start beanstalkd, listening on port 11300:

`beanstalkd`

- Start beanstalkd listening on a custom port and address:

`beanstalkd -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_number</span>

- Persist work queues by saving them to disk:

`beanstalkd -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/persistence_directory</span>

- Sync to the persistence directory every 500 milliseconds:

`beanstalkd -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/persistence_directory</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">500</span>
