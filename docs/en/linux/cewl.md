---
layout: page
title: linux/cewl (English)
description: "URL spidering tool for making a cracking wordlist from web content."
content_hash: f4f4a2ad85be0f6e04e86ab54ace195a7a6ad691
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# cewl

URL spidering tool for making a cracking wordlist from web content.
More information: <https://digi.ninja/projects/cewl.php>.

- Create a wordlist file from the given URL up to 2 links depth:

`cewl --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` --write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/wordlist.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Output an alphanumeric wordlist from the given URL with words of minimum 5 characters:

`cewl --with-numbers --min_word_length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Output a wordlist from the given URL in debug mode including email addresses:

`cewl --debug --email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Output a wordlist from the given URL using HTTP Basic or Digest authentication:

`cewl --auth_type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">basic|digest</span>` --auth_user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --auth_pass `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Output a wordlist from the given URL through a proxy:

`cewl --proxy_host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` --proxy_port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>
