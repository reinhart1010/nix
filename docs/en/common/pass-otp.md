---
layout: page
title: common/pass-otp (English)
description: "A pass extension for managing one-time-password (OTP) tokens."
content_hash: 3bc25175f3aba0ce85e999c2af90c5afeea43af3
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pass otp

A pass extension for managing one-time-password (OTP) tokens.
More information: <https://github.com/tadfisher/pass-otp#readme>.

- Prompt for an otpauth URI token and create a new pass file:

`pass otp insert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/pass</span>

- Prompt for an otpauth URI token and append to an existing pass file:

`pass otp append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/pass</span>

- Print a 2FA code using the OTP token in a pass file:

`pass otp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/pass</span>

- Copy and don't print a 2FA code using the OTP token in a pass file:

`pass otp --clip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/pass</span>

- Display a QR code using the OTP token stored in a pass file:

`pass otp uri --qrcode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/pass</span>

- Prompt for an OTP secret value specifying issuer and account (at least one must be specified) and append to existing pass file:

`pass otp append --secret --issuer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">issuer_name</span>` --account `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">account_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/pass</span>
