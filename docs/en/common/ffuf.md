---
layout: page
title: common/ffuf (English)
description: "A fast web fuzzer written in Go."
content_hash: be8f069ca6c7b826d02a0ab044bb9f6e01469e04
last_modified_at: 2024-04-02
related_topics:
  - title: français version
    url: /fr/common/ffuf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ffuf

A fast web fuzzer written in Go.
The `FUZZ` keyword is used as a placeholder. `ffuf` will try to hit the URL by replacing the word `FUZZ` with every word in the wordlist.
More information: <https://github.com/ffuf/ffuf#usage>.

- Enumerate directories using [c]olored output and a [w]ordlist specifying a target [u]RL:

`ffuf -c -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/wordlist.txt</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://target/FUZZ</span>

- Enumerate webservers of subdomains by changing the position of the keyword:

`ffuf -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/subdomains.txt</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://FUZZ.target.com</span>

- Fuzz with specified [t]hreads (default: 40) and pro[x]ying the traffic and save [o]utput to a file:

`ffuf -o -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/wordlist.txt</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://target/FUZZ</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">500</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://127.0.0.1:8080</span>

- Fuzz a specific [H]eader ("Name: Value") and [m]atch HTTP status [c]odes:

`ffuf -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/wordlist.txt</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://target.com</span>` -H "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Host: FUZZ</span>`" -mc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">200</span>

- Fuzz with specified HTTP method and [d]ata, while [f]iltering out comma separated status [c]odes:

`ffuf -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/postdata.txt</span>` -X `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">POST</span>` -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username=admin\&password=FUZZ</span>`" -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://target/login.php</span>` -fc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">401,403</span>

- Fuzz multiple positions with multiple wordlists using different modes:

`ffuf -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/keys:KEY</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/values:VALUE</span>` -mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pitchfork|clusterbomb</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://target.com/id?KEY=VALUE</span>

- Proxy requests through a HTTP MITM pro[x]y (such as Burp Suite or `mitmproxy`):

`ffuf -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/wordlist</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://127.0.0.1:8080</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://target.com/FUZZ</span>
