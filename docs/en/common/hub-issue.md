---
layout: page
title: common/hub-issue (English)
description: "Manage Github issues."
content_hash: ae21de29a23d641e1962d164de4cded3970a1f5f
last_modified_at: 2023-12-27
tldri18n_status: 2
---
# hub issue

Manage Github issues.
More information: <https://hub.github.com/hub-issue.1.html>.

- List the last 10 issues with the `bug` label:

`hub issue list --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --labels "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bug</span>`"`

- Display a specific issue:

`hub issue show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">issue_number</span>

- List 10 closed issues assigneed to a specific user:

`hub issue --state `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">closed</span>` --assignee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>
