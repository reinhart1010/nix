---
layout: page
title: common/step (English)
description: "An easy-to-use CLI tool for building, operating, and automating Public Key Infrastructure (PKI) systems and workflows."
content_hash: 07f49267e74667efa73debf98f0955b5a20f15ad
last_modified_at: 2024-10-29
tldri18n_status: 2
---
# step

An easy-to-use CLI tool for building, operating, and automating Public Key Infrastructure (PKI) systems and workflows.
See also: `openssl`.
More information: <https://smallstep.com/docs/step-cli/>.

- Inspect the contents of a certificate:

`step certificate inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/certificate.crt</span>

- Create a root CA certificate and a key (append `--no-password --insecure` to skip private key password protection):

`step certificate create "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Example Root CA</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/root-ca.crt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/root-ca.key</span>` --profile root-ca`

- Generate a certificate for a specific hostname and sign it with the root CA (generating a CSR can be skipped for simplification):

`step certificate create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname.example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/hostname.crt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/hostname.key</span>` --profile leaf --ca `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/root-ca.crt</span>` --ca-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/root-ca.key</span>

- Verify a certificate chain:

`step certificate verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/hostname.crt</span>` --roots `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/root-ca.crt</span>` --verbose`

- Convert a PEM format certificate to DER and write it to disk:

`step certificate format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/certificate.pem</span>` --out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/certificate.der</span>

- Install or uninstall a root certificate in the system's default trust store:

`step certificate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">install|uninstall</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/root-ca.crt</span>

- Create a RSA/EC private and public keypair (append `--no-password --insecure` to skip private key password protection):

`step crypto keypair `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/public_key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/private_key</span>` --kty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">RSA|EC</span>

- Show help for subcommands:

`step `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path|base64|certificate|completion|context|crl|crypto|oauth|ca|beta|ssh</span>` --help`
