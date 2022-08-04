---
layout: page
title: common/gitlab-ctl (English)
description: "CLI tool for managing the GitLab omnibus."
content_hash: 44c40c75a812f5a34edb4f2d18a880d36153116c
---
# gitlab-ctl

CLI tool for managing the GitLab omnibus.
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
