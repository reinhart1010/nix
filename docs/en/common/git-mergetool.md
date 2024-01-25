---
layout: page
title: common/git-mergetool (English)
description: "Run merge conflict resolution tools to resolve merge conflicts."
content_hash: 5702bd3748031993044754786a2af0f95d27b2ca
last_modified_at: 2024-01-25
related_topics:
  - title: français version
    url: /fr/common/git-mergetool.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-mergetool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git mergetool

Run merge conflict resolution tools to resolve merge conflicts.
More information: <https://git-scm.com/docs/git-mergetool>.

- Launch the default merge tool to resolve conflicts:

`git mergetool`

- List valid merge tools:

`git mergetool --tool-help`

- Launch the merge tool identified by a name:

`git mergetool --tool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tool_name</span>

- Don't prompt before each invocation of the merge tool:

`git mergetool --no-prompt`

- Explicitly use the GUI merge tool (see the `merge.guitool` configuration variable):

`git mergetool --gui`

- Explicitly use the regular merge tool (see the `merge.tool` configuration variable):

`git mergetool --no-gui`
