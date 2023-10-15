---
layout: page
title: common/git-paste (English)
description: "Send commits to a pastebin site using `pastebinit`."
content_hash: 30f129b5c41ee623efe5856b80c9c0a21b8177f7
last_modified_at: 2023-10-15
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git paste

Send commits to a pastebin site using `pastebinit`.
Part of `git-extras`.
More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-paste>.

- Send the patches between the current branch and its upstream to a pastebin using `pastebinit`:

`git paste`

- Pass options to `git format-patch` in order to select a different set of commits (`@^` selects the parent of HEAD, and so the currently checked out commit is sent):

`git paste `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@^</span>
