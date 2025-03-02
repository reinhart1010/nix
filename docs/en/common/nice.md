---
layout: page
title: common/nice (English)
description: "Execute a program with a custom scheduling priority (niceness)."
content_hash: fc6c85716333739c188469ceace65ac5a5bf127f
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/common/nice.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/nice.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nice

Execute a program with a custom scheduling priority (niceness).
Niceness values range from -20 (the highest priority) to 19 (the lowest).
More information: <https://www.gnu.org/software/coreutils/manual/html_node/nice-invocation.html>.

- Launch a program with altered priority:

`nice -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">niceness_value</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Define the priority with an explicit option:

`nice `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--adjustment</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">niceness_value</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
