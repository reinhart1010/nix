---
layout: page
title: common/whatweb (English)
description: "Next-generation web scanner."
content_hash: 9c3d8eb0d38430c256bac3f79262c05560e20774
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/whatweb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# whatweb

Next-generation web scanner.
More information: <https://morningstarsecurity.com/research/whatweb>.

- Scan websites/targets for web technologies:

`whatweb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">website1 website2 ...</span>

- Read targets/websites from a file:

`whatweb -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">targets_file</span>

- Scan a website/target in verbose mode:

`whatweb -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Run an aggressive scan on a website:

`whatweb -a 3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Scan a network and suppress errors:

`whatweb --no-errors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.0/24</span>

- List plugins:

`whatweb -l`

- List plugin details:

`whatweb -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plugin_name</span>
