---
layout: page
title: common/argocd (English)
description: "Command-line interface to control a Argo CD server."
content_hash: 164f5ae1ba5a6c9cba5e843571a2a31e2b0d1421
last_modified_at: 2024-10-05
related_topics:
  - title: français version
    url: /fr/common/argocd.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/argocd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/argocd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# argocd

Command-line interface to control a Argo CD server.
Some subcommands such as `app` have their own usage documentation.
More information: <https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd/>.

- Login to Argo CD server:

`argocd login --insecure --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argocd_server:port</span>

- List applications:

`argocd app list`
