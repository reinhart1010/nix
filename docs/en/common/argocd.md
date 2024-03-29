---
layout: page
title: common/argocd (English)
description: "Command-line interface to control a Argo CD server."
content_hash: d431358b57e6e80c8af6a031567ba5fadbb7ef9b
last_modified_at: 2023-11-12
related_topics:
  - title: 한국어 version
    url: /ko/common/argocd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# argocd

Command-line interface to control a Argo CD server.
Some subcommands such as `argocd app` have their own usage documentation.
More information: <https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd/>.

- Login to Argo CD server:

`argocd login --insecure --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argocd_server:port</span>

- List applications:

`argocd app list`
