---
layout: page
title: windows/choice (English)
description: "Prompt user to select a choice and return the selected choice index."
content_hash: 67221db8113f14d217fa398bc8de9ee5a6434d3d
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/windows/choice.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choice.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choice

Prompt user to select a choice and return the selected choice index.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/choice>.

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
