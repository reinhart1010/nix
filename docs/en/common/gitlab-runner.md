---
layout: page
title: common/gitlab-runner (English)
description: "Manage GitLab runners."
content_hash: 2c32f5607d66b084e642454583b81efc13268bd9
last_modified_at: 2023-07-16
related_topics:
  - title: Türkçe version
    url: /tr/common/gitlab-runner.html
    icon: bi bi-globe
---
# gitlab-runner

Manage GitLab runners.
More information: <https://docs.gitlab.com/runner/>.

- Register a runner:

`sudo gitlab-runner register --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://gitlab.example.com</span>` --registration-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Register a runner with a Docker executor:

`sudo gitlab-runner register --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://gitlab.example.com</span>` --registration-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --executor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">docker</span>

- Unregister a runner:

`sudo gitlab-runner unregister --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Display the status of the runner service:

`sudo gitlab-runner status`

- Restart the runner service:

`sudo gitlab-runner restart`

- Check if the registered runners can connect to GitLab:

`sudo gitlab-runner verify`
