---
layout: page
title: common/nuclei (English)
description: "Fast and customizable vulnerability scanner based on a simple YAML based DSL."
content_hash: bd4fe35c388efbce956d6d17a02c1c1d23687dc6
last_modified_at: 2024-02-15
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nuclei.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nuclei

Fast and customizable vulnerability scanner based on a simple YAML based DSL.
More information: <https://github.com/projectdiscovery/nuclei>.

- [u]pdate `nuclei` [t]emplates to the latest released version:

`nuclei -ut`

- [l]ist all [t]emplates with a specific [p]rotocol [t]ype:

`nuclei -tl -pt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dns|file|http|headless|tcp|workflow|ssl|websocket|whois|code|javascript</span>

- Run an [a]utomatic web [s]can using wappalyzer technology detection specifying a target [u]RL/host to scan:

`nuclei -as -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scanme.nmap.org</span>

- Run HTTP [p]rotocol [t]ype templates of high and critical severity, [e]xporting results to [m]arkdown files inside a specific directory:

`nuclei -severity high,critical -pt http -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://scanme.sh</span>` -me `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">markdown_directory</span>

- Run all templates using a different [r]ate [l]imit and maximum [b]ulk [s]ize with silent output (only showing the findings):

`nuclei -rl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">150</span>` -bs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">25</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">25</span>` -silent -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://scanme.sh</span>

- Run the WordPress [w]orkflow against a WordPress site:

`nuclei -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/nuclei-templates/workflows/wordpress-workflow.yaml</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://sample.wordpress.site</span>

- Run one or more specific [t]emplates or directory with [t]emplates with [v]erbose output in `stderr` and [o]utput detected issues/vulnerabilities to a file:

`nuclei -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/nuclei-templates/http</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://scanme.sh</span>` -v -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">results</span>

- Run scan based on one or more [t]emplate [c]onditions:

`nuclei -tc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"contains(tags, 'xss') && contains(tags, 'cve')"</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://vulnerable.website</span>
