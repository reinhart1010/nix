---
layout: page
title: common/kubectl-wait (English)
description: "Wait for resource(s) to reach a certain state."
content_hash: d8b6971f3f67b7f1572e0c431a736eac8679a1af
last_modified_at: 2025-01-04
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/kubectl-wait.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kubectl wait

Wait for resource(s) to reach a certain state.
More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#wait>.

- Wait for a deployment to become available:

`kubectl wait --for=condition=available deployment/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deployment_name</span>

- Wait for all pods with a certain [l]abel to be ready:

`kubectl wait --for=condition=ready pod -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">label_key</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">label_value</span>

- Wait for a pod to be deleted:

`kubectl wait --for=delete pod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_name</span>

- Wait for a job to complete, within 120 seconds (if the condition isn't met on time, the exit status will be unsuccessful):

`kubectl wait --for=condition=complete job/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_name</span>` --timeout 120s`
