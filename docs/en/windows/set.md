---
layout: page
title: windows/set (English)
description: "Display or set environment variables for the current instance of CMD."
content_hash: 1e4666d8ca6b4a30703146a8a20f58b1f8691413
related_topics:
  - title: 中文 version
    url: /zh/windows/set.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/set.html
    icon: bi bi-globe
---
# set

Display or set environment variables for the current instance of CMD.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/set>.

- List all current environment variables:

`set`

- Set an environment variable to a specific value:

`set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- List environment variables starting with the specified string:

`set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Prompt the user for a value for the specified variable:

`set /p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt_string</span>
