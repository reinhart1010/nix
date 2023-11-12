---
layout: page
title: common/beanstalkd (English)
description: "A simple and generic work-queue server."
content_hash: 1a916aa45d70cae88b2955163af8fde7dfd3814b
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/common/beanstalkd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/beanstalkd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# beanstalkd

A simple and generic work-queue server.
More information: <https://beanstalkd.github.io/>.

- Start Beanstalk, listening on port 11300:

`beanstalkd`

- Start Beanstalk listening on a custom port and address:

`beanstalkd -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_number</span>

- Persist work queues by saving them to disk:

`beanstalkd -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/persistence_directory</span>

- Sync to the persistence directory every 500 milliseconds:

`beanstalkd -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/persistence_directory</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">500</span>
