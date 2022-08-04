---
layout: page
title: common/csvgrep (English)
description: "Filter CSV rows with string and pattern matching."
content_hash: 9c383b0e5c84ce273d83031e401b693fd7332ab6
related_topics:
  - title: italiano version
    url: /it/common/csvgrep.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/csvgrep.html
    icon: bi bi-globe
---
# csvgrep

Filter CSV rows with string and pattern matching.
Included in csvkit.
More information: <https://csvkit.readthedocs.io/en/latest/scripts/csvgrep.html>.

- Find rows that have a certain string in column 1:

`csvgrep -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string_to_match</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>

- Find rows in which columns 3 or 4 match a certain regular expression:

`csvgrep -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3,4</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>

- Find rows in which the "name" column does NOT include the string "John Doe":

`csvgrep -i -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">John Doe</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>
