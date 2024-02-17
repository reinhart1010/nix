---
layout: page
title: common/httpx (English)
description: "A fast and multi-purpose HTTP toolkit written in Go to run multiple probes at once."
content_hash: 581a3449b1c6ca14075ab9937a3b6afa80b77655
last_modified_at: 2024-02-17
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/httpx.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># httpx

A fast and multi-purpose HTTP toolkit written in Go to run multiple probes at once.
Note: not to be confused with the unrelated Python's HTTPX which has the same command name.
More information: <https://github.com/projectdiscovery/httpx>.

- Run a probe against a [u]RL, host, IP Address or subnet (CIDR notation) showing probe status:

`httpx -probe -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|host|ipaddress|subnet_with_cidr</span>

- Run a probe against multiple hosts showing [s]tatus [c]ode with input from `subfinder`:

`subfinder -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` | httpx -sc`

- Run a [r]ate [l]imited probe against a [l]ist of hosts from a file showing [t]echnology [d]etected and [r]esponse [t]ime:

`httpx -rl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">150</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/newline_separated_hosts_list</span>` -td -rt`

- Run a probe against a [u]RL showing its webpage title, CDN/WAF in use, and page content hash:

`httpx -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` -title -cdn -hash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sha256</span>

- Run a probe against a list of hosts with custom defined [p]orts and timeout after certain seconds:

`httpx -probe -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host1,host2,...</span>` -p http:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80,8000-8080</span>`,https:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">443,8443</span>` -timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Run a probe against a list of hosts [f]iltering out [c]odes of certain responses:

`httpx -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host1,host2,...</span>` -fc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">400,401,404</span>

- Run a probe against a list of hosts [m]atching [c]odes of certain responses:

`httpx -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host1,host2,...</span>` -mc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">200,301,304</span>

- Run a probe against a URL [s]aving [s]creenshots of certain paths, with [s]creenshot [t]imeouts (assets are saved in `./output`):

`httpx -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.github.com</span>` -path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/tldr-pages/tldr,/projectdiscovery/httpx</span>` -ss -st `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>
