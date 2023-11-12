---
layout: page
title: common/gitlab-ctl (English)
description: "Manage the GitLab omnibus."
content_hash: d1336b348581407cfc5506f67634a12156d89270
last_modified_at: 2023-11-12
related_topics:
  - title: Türkçe version
    url: /tr/common/gitlab-ctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gitlab-ctl

Manage the GitLab omnibus.
More information: <https://docs.gitlab.com/omnibus/maintenance/>.

- Display the status of every service:

`sudo gitlab-ctl status`

- Display the status of a specific service:

`sudo gitlab-ctl status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nginx</span>

- Restart every service:

`sudo gitlab-ctl restart`

- Restart a specific service:

`sudo gitlab-ctl restart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nginx</span>

- Display the logs of every service and keep reading until `Ctrl + C` is pressed:

`sudo gitlab-ctl tail`

- Display the logs of a specific service:

`sudo gitlab-ctl tail `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nginx</span>
