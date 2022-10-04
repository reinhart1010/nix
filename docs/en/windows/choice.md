---
layout: page
title: windows/choice (English)
description: "Prompt user to select a choice and return the selected choice index."
content_hash: 00e6b063221f029280f85fb25275a103a4a7f44c
---
# choice

Prompt user to select a choice and return the selected choice index.
More information: <https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/choice>.

- Prompt the current user to select a `Y` or `N` choice:

`choice`

- Prompt the current user to select a [c]hoice from a specific set:

`choice /c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AB</span>

- Prompt the current user to select a choice with a specific [m]essage:

`choice /m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`"`

- Prompt the current user to select a [c]ase-[s]ensitive [c]hoice from a specific set:

`choice /cs /c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Ab</span>

- Prompt the current user to select a choice and prefer the [d]efault choice in a specific [t]ime:

`choice /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>

- Display help:

`choice /?`
