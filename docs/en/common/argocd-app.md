---
layout: page
title: common/argocd-app (English)
description: "Command-line interface to manage applications by Argo CD."
content_hash: 06e07acec2623cca81da274370e6835272586d9a
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/argocd-app.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/argocd-app.html
    icon: bi bi-globe
tldri18n_status: 2
---
# argocd app

Command-line interface to manage applications by Argo CD.
More information: <https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd_app/>.

- List applications:

`argocd app list --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json|yaml|wide</span>` `

- Get application details:

`argocd app get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json|yaml|wide</span>

- Deploy application internally (to the same cluster that Argo CD is running in):

`argocd app create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>` --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git_repo_url</span>` --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repo</span>` --dest-server https://kubernetes.default.svc --dest-namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ns</span>

- Delete an application:

`argocd app delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>

- Enable application auto-sync:

`argocd app set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>` --sync-policy auto --auto-prune --self-heal`

- Preview app synchronization without affecting cluster:

`argocd app sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>` --dry-run --prune`

- Show application deployment history:

`argocd app history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wide|id</span>

- Rollback application to a previous deployed version by history ID (deleting unexpected resources):

`argocd app rollback `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">history_id</span>` --prune`
