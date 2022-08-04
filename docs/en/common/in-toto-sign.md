---
layout: page
title: common/in-toto-sign (English)
description: "Sign in-toto link or layout metadata or verify their signatures."
content_hash: f71f90922d1e776569b0a59d3f28c01e3fdd0b09
---
# in-toto-sign

Sign in-toto link or layout metadata or verify their signatures.
More information: <https://in-toto.readthedocs.io/en/latest/command-line-tools/in-toto-sign.html>.

- Sign 'unsigned.layout' with two keys and write it to 'root.layout':

`in-toto-sign -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unsigned.layout</span>` -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">priv_key1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">priv_key2</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">root.layout</span>

- Replace signature in link file and write to default filename:

`in-toto-sign -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package.2f89b927.link</span>` -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">priv_key</span>

- Verify a layout signed with 3 keys:

`in-toto-sign -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">root.layout</span>` -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pub_key0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pub_key1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pub_key2</span>` --verify`

- Sign a layout with the default GPG key in default GPG keyring:

`in-toto-sign -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">root.layout</span>` --gpg`

- Verify a layout with a GPG key identified by keyid '...439F3C2':

`in-toto-sign -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">root.layout</span>` --verify --gpg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">...439F3C2</span>
