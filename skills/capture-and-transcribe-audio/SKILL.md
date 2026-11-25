---
name: capture-and-transcribe-audio
description: "Build or repair recording and transcription in Apple apps with AVAudioEngine, Speech, WhisperKit or an explicit server transcription hand-off."
---

# Capture and Transcribe Audio

## Workflow

Decide whether the feature needs live partials, durable recording, file transcription or a mix. Choose an engine from supported locale/device, latency, offline use, consent and resource limits. Keep the original recording's identity and transcript revisions independent of engine choice.

- Own the capture session and engine together, request the required permissions, use a matching audio session category, and verify the actual input format after route selection. Keep blocking work off the realtime tap. Convert to the engine's expected format outside the tap and handle interruptions, route changes, media service reset and teardown. Write a recoverable file or flushed segments and close them before sending. On resume, remove any prior tap before reinstalling, renegotiate format for the route, and respect user stop and interruption state.
- For SpeechAnalyzer, gate OS availability, check locale and model assets with AssetInventory, choose the compatible format, and consume results concurrently. When a model is unavailable, keep a requested recording separately and transcribe that file when an authorized engine becomes ready. Replace volatile results by audio range and commit finalized ranges. Make stop idempotent. Stop capture, drain buffers and finish the input continuation before finalizing through end of input. Use the analyzer cancellation path for abort. If live results missed recorded ranges, reconcile by transcribing the file and merging by time range. Release the tap and audio session once. Use WhisperKit when its supported hardware, assets and latency fit. Keep model download and availability visible and cancellable. Follow the project’s dependency policy before adding an engine.
- For an authorized server option, retain the local recording until success or explicit discard. Upload via the app's authenticated, retryable job contract with a stable recording ID. Resume job polling and preserve consent and retention settings. Never silently fall back to transmitting microphone audio.
- Test permission denial, route changes, interruptions, rapid stop/restart, missing model and network disconnect. Check timestamps, duplicate or missing final text, and microphone release on real hardware. Use a known recording for reproducible engine comparisons.

## Deliverable

Report audio-file recovery, finalized transcript coverage, engine or model fallback, and on-device interruption and stop results.

## Sources

[Bring advanced speech-to-text to your app with SpeechAnalyzer](https://developer.apple.com/videos/play/wwdc2025/277/) at 2:41 and 9:06, [AVAudioEngine](https://developer.apple.com/documentation/avfaudio/avaudioengine) and [WhisperKit](https://github.com/argmaxinc/WhisperKit). Resolve current permissions, compatibility and APIs for the chosen engine.
