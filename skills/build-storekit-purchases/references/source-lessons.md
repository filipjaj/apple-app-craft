# Source lessons

## Curated channel review — 2026-10-06

Complete timestamped transcripts were acquired. Selected technical passages were reviewed; this does not claim full-transcript reading or continuous video viewing. Lessons below paraphrase the reviewed passages. Current SDK documentation and the actual project take precedence over historical examples, numeric limits and speech-recognition spelling.

### WWDC23: What’s new in StoreKit 2 and StoreKit Testing in Xcode | Apple — 00:11:12.000

Local StoreKit testing helps exercise purchase behavior before store configuration but has a distinct validation scope.

[Evidence at 00:11:12.000](https://www.youtube.com/watch?v=oWZYcO_DD3c&t=672s). Caption anchor: “With StoreKit Testing in Xcode you can”.

### WWDC23: Explore testing in-app purchases | Apple — 00:10:00.000

Sandbox retry and grace-period durations differ from production and must be interpreted accordingly.

[Evidence at 00:10:00.000](https://www.youtube.com/watch?v=PGPTDQxC9oA&t=600s). Caption anchor: “Remember, these durations apply to production only,”.

### WWDC26: What’s new in Apple In-App Purchase | Apple — 00:04:17.000

Display and purchase only billing plans actually available in the customer's storefront and supported program.

[Evidence at 00:04:17.000](https://www.youtube.com/watch?v=yTkVCs9OfBY&t=257s). Caption anchor: “Note, that billing plan metadata is only”.

### WWDC26: Explore Retention Messaging in App Store Connect | Apple — 00:09:54.000

Real-time retention messaging needs tested latency and truthful fallback when the server does not respond.

[Evidence at 00:09:54.000](https://www.youtube.com/watch?v=jPhMM2enfUE&t=594s). Caption anchor: “To ensure a great customer experience, you'll”.

### WWDC26: Offer subscriptions to groups and organizations | Apple — 00:05:48.000

Group and organization entitlements depend on actual seat assignment, not just an invitation link.

[Evidence at 00:05:48.000](https://www.youtube.com/watch?v=Ut7TWRP1ay8&t=348s). Caption anchor: “and ensure they are owned and managed”.

### Current documentation checked

- [Official getting started with in app purchases using storekit views documentation](https://developer.apple.com/documentation/storekit/getting-started-with-in-app-purchases-using-storekit-views).
- [Official purchaseresult documentation](https://developer.apple.com/documentation/storekit/product/purchaseresult).
- [Official finish%28%29 documentation](https://developer.apple.com/documentation/storekit/transaction/finish%28%29).
- [Official currententitlement documentation](https://developer.apple.com/documentation/storekit/product/currententitlement).

Implementation steps and verification scenarios also include engineering interpretation: validate permissions, lifetime, failure recovery and the actual task rather than copying a sample mechanically. Local transcript, passage-review and documentation provenance is retained under `source-additions/curated-200/` and excluded from the portable plugin.
