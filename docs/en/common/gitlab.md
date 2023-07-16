---
layout: page
title: common/gitlab (English)
description: "Ruby wrapper for the GitLab API."
content_hash: 1c60e8cadbf349bb4751e3d0f16b6aac731b7211
last_modified_at: 2023-07-16
related_topics:
  - title: Türkçe version
    url: /tr/common/gitlab.html
    icon: bi bi-globe
---
# gitlab

Ruby wrapper for the GitLab API.
Some subcommands such as `gitlab ctl` have their own usage documentation.
More information: <https://narkoz.github.io/gitlab/>.

- Create a new project:

`gitlab create_project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>

- Get info about a specific commit:

`gitlab commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_hash</span>

- Get info about jobs in a CI pipeline:

`gitlab pipeline_jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pipeline_id</span>

- Start a specific CI job:

`gitlab job_play `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>
