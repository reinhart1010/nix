---
layout: page
title: common/git-check-attr (English)
description: "For every pathname, list if each attribute is unspecified, set, or unset as a gitattribute on that pathname."
content_hash: 44126e101f59e8228c6382b1b46d54eaf9ee7635
last_modified_at: 2023-11-12
related_topics:
  - title: Türkçe version
    url: /tr/common/git-check-attr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git check-attr

For every pathname, list if each attribute is unspecified, set, or unset as a gitattribute on that pathname.
More information: <https://git-scm.com/docs/git-check-attr>.

- Check the values of all attributes on a file:

`git check-attr --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Check the value of a specific attribute on a file:

`git check-attr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">attribute</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Check the value of a specific attribute on files:

`git check-attr --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Check the value of a specific attribute on one or more files:

`git check-attr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">attribute</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>
