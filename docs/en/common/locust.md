---
layout: page
title: common/locust (English)
description: "Load-testing tool to determine number of concurrent users a system can handle."
content_hash: 7c86ea230225853da7a75f394052e13ffc3849e3
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# locust

Load-testing tool to determine number of concurrent users a system can handle.
More information: <https://locust.io>.

- Load-test "example.com" with web interface using locustfile.py:

`locust --host=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>

- Use a different test file:

`locust --locustfile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test_file.py</span>` --host=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>

- Run test without web interface, spawning 1 user a second until there are 100 users:

`locust --no-web --clients=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --hatch-rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` --host=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>

- Start Locust in master mode:

`locust --master --host=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>

- Connect Locust slave to master:

`locust --slave --host=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>

- Connect Locust slave to master on a different machine:

`locust --slave --master-host=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master_hostname</span>` --host=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>
