---
layout: page
title: common/wfuzz (English)
description: "A web application bruteforcer."
content_hash: d285b7d406682ff4bfd043f6f3caf8f07a54d22c
last_modified_at: 2024-04-01
tldri18n_status: 2
---
# wfuzz

A web application bruteforcer.
More information: <https://wfuzz.readthedocs.io/en/latest/user/basicusage.html>.

- Directory and file bruteforce using the specified [w]ordlist and also [p]roxying the traffic:

`wfuzz -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.1:8080:HTTP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/FUZZ</span>

- Save the results to a [f]ile:

`wfuzz -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/FUZZ</span>

- Show [c]olorized output while only showing the declared response codes in the output:

`wfuzz -c -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --sc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">200,301,302</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/FUZZ</span>

- Use a custom [H]eader to fuzz subdomains while [h]iding specific response [c]odes and word counts. Increase the [t]hreads to 100 and include the target ip/domain:

`wfuzz -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"Host: FUZZ.example.com"</span>` --hc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">301</span>` --hw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">222</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Brute force Basic Authentication using a list of usernames and passwords from files for each FUZ[z] keyword, [h]iding response [c]odes of unsuccessful attempts:

`wfuzz -c --hc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">401</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">delay_between_requests_in_seconds</span>` -z file,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/usernames</span>` -z file,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/passwords</span>` --basic 'FUZZ:FUZ2Z' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Provide wordlist directly from the command line and use POST request for fuzzing:

`wfuzz -z list,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">word1-word2-...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://api.example.com</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"id=FUZZ&showwallet=true"</span>

- Provide wordlists from a file applying base64 and md5 encoding on them (`wfuzz -e encoders` lists all available encoders):

`wfuzz -z file,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`,none-base64-md5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/FUZZ</span>

- List available encoders/payloads/iterators/printers/scripts:

`wfuzz -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encoders|payloads|iterators|printers|scripts</span>
