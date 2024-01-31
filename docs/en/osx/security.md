---
layout: page
title: osx/security (English)
description: "Administer keychains, keys, certificates and the Security framework."
content_hash: e2f3774b99c291df554d98e3ce5c87ecaa61a173
last_modified_at: 2024-01-31
related_topics:
  - title: polski version
    url: /pl/osx/security.html
    icon: bi bi-globe
tldri18n_status: 2
---
# security

Administer keychains, keys, certificates and the Security framework.
More information: <https://keith.github.io/xcode-man-pages/security.1.html>.

- List all available keychains:

`security list-keychains`

- Delete a specific keychain:

`security delete-keychain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.keychain</span>

- Create a keychain:

`security create-keychain -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.keychain</span>

- Set a certificate to use with a website or [s]ervice by its [c]ommon name (fails if several certificates with the same common name exist):

`security set-identity-preference -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">URL|hostname|service</span>` -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">common_name</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.keychain</span>

- Add a certificate from file to a [k]eychain (if -k isn't specified, the default keychain is used):

`security add-certificates -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.keychain</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/cert_file.pem</span>

- Add a CA certificate to the per-user Trust Settings:

`security add-trusted-cert -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/user-keychain.keychain-db</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/ca-cert_file.pem</span>

- Remove a CA certificate from the per-user Trust Settings:

`security remove-trusted-cert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/ca-cert_file.pem</span>
