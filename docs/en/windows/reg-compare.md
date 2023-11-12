---
layout: page
title: windows/reg-compare (English)
description: "Compare keys and their values in the registry."
content_hash: af18162c32d97ad3f376d52d08500049ccaed81a
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/windows/reg-compare.html
    icon: bi bi-globe
tldri18n_status: 2
---
# reg compare

Compare keys and their values in the registry.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-compare>.

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
