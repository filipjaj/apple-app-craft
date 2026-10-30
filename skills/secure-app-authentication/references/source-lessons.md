# Source lessons

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC25: What’s new in passkeys | Apple — 00:18:36.000

Credential-management URLs must work for unauthenticated arrival and return after required sign-in.

[Evidence at 00:18:36.000](https://www.youtube.com/watch?v=mV68bUYVSL0&t=1116s). Caption anchor: “It’s important that these URLs correctly handle”.

### WWDC22: Meet passkeys | Apple — 00:27:19.000

The server verifies the challenge response; a private key does not leave the credential device.

[Evidence at 00:27:19.000](https://www.youtube.com/watch?v=7MZyAjlVT8I&t=1639s). Caption anchor: “and only sends the solution back to”.

### WWDC24: Streamline sign-in with passkey upgrades and credential managers | Apple — 00:08:32.000

Password retirement requires an intentional account lifecycle decision rather than merely adding a passkey.

[Evidence at 00:08:32.000](https://www.youtube.com/watch?v=p8a6ODX1zHY&t=512s). Caption anchor: “If your service notices that an account”.

### Current documentation checked

- [Official supporting passkeys documentation](https://developer.apple.com/documentation/authenticationservices/supporting-passkeys).
- [Official attestationobject documentation](https://developer.apple.com/documentation/authenticationservices/aspasskeyregistrationcredential/attestationobject).

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
