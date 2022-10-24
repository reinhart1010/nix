---
layout: page
title: windows/date (English)
description: "Displays or sets the system date."
content_hash: 4ce8a38fd9dcdc05e394b93508c3f7e10e7f9b96
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># date

Displays or sets the system date.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/date>.

- Display the current system date and prompt to enter a new date (leave empty to keep unchanged):

`date`

- Display the current system date without prompting for a new date:

`date /t`

- Change the current system date to a specific date:

`date `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">month</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">day</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">year</span>
