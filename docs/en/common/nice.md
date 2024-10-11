---
layout: page
title: common/nice (English)
description: "Execute a program with a custom scheduling priority (niceness)."
content_hash: 76e6d516daa63d5c01765716c2273945d391fb92
last_modified_at: 2024-10-11
related_topics:
  - title: Nederlands version
    url: /nl/common/nice.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nice

Execute a program with a custom scheduling priority (niceness).
Niceness values range from -20 (the highest priority) to 19 (the lowest).
More information: <https://www.gnu.org/software/coreutils/nice>.

- Launch a program with altered priority:

`nice -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">niceness_value</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Define the priority with an explicit option:

`nice `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--adjustment</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">niceness_value</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
