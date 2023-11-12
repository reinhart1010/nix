---
layout: page
title: windows/if (English)
description: "Performs conditional processing in batch scripts."
content_hash: 8e6ad27feeeee5d91fc986abdfe17ea3f2e22908
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# if

Performs conditional processing in batch scripts.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/if>.

- Execute the specified commands if the condition is true:

`if `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">condition</span>` (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Condition is true</span>`)`

- Execute the specified commands if the condition is false:

`if not `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">condition</span>` (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Condition is true</span>`)`

- Execute the first specified commands if the condition is true otherwise execute the second specified commands:

`if `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">condition</span>` (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Condition is true</span>`) else (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Condition is false</span>`)`

- Check whether `%errorlevel%` is greater than or equal to the specified exit code:

`if errorlevel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Condition is true</span>`)`

- Check whether two strings are equal:

`if %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>`% == `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>` (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Condition is true</span>`)`

- Check whether two strings are equal without respecting letter case:

`if /i %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>`% == `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>` (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Condition is true</span>`)`

- Check whether a file exist:

`if exist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>` (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Condition is true</span>`)`
