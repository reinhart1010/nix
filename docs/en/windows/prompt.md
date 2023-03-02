---
layout: page
title: windows/prompt (English)
description: "Change the default DOS style prompt in a command window."
content_hash: ade81f8c7b279da57dcd702dc268d11ef1f607ef
last_modified_at: 2023-03-02
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># prompt

Change the default DOS style prompt in a command window.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/prompt>.

- Reset the prompt to the default setting:

`prompt`

- Set a specific prompt:

`prompt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt</span>

- Change the prompt to show the current date first:

`prompt $D $P$G`

- Change the prompt to show the current time first:

`prompt $T $P$G`

- Change the prompt by adding a specific text first:

`prompt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>` $P$G`
