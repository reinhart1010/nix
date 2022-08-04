---
layout: page
title: windows/reg-compare (English)
description: "Compare keys and their values in the registry."
content_hash: d80d4df43fd1d93c34190422c8254a191276f3c5
related_topics:
  - title: 中文 version
    url: /zh/windows/reg-compare.html
    icon: bi bi-globe
---
# reg compare

Compare keys and their values in the registry.
More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/reg-compare>.

- Compare all values under a specific key with a second key:

`reg compare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">first_key_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">second_key_name</span>

- Compare a specific value under two keys:

`reg compare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">first_key_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">second_key_name</span>` /v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Compare all sub keys and values for two keys:

`reg compare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">first_key_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">second_key_name</span>` /s`

- Only output the matches between the specified keys:

`reg compare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">first_key_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">second_key_name</span>` /os`

- Output the differences and matches between the specified keys:

`reg compare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">first_key_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">second_key_name</span>` /oa`
