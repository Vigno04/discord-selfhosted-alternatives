# Discord Alternatives Features

To clarify the definitions/meanings of the features that are included in the comparison, the below definitions are currently used:

## How Votes Are Assigned

Feature ratings use a simplified system:
- ✅ = Feature exists and works well
- 🚧 = Feature exists but may be incomplete or needs improvement
- ❌ = Feature does not yet exist

For features that use numerical ratings (like Freeness), scores are based on personal opinion after sufficient testing of the application. These ratings are subjective and may change as the project evolves.

## Github Stars

The number of stars on the primary github (or other) source code repository.

## Contributors

The number of contributors that have contributed to the project.

## Last Commit

The date of the last git commit to the project.

## Source Language

The primary language used in the repository's source code.

## License

The software license listed on the code repository. If the project has a custom license or the GitHub badge doesn't work properly, you can optionally specify a `license_url` field in the project entry to make the license badge link to a custom URL (e.g., the license file on GitHub).

## Demo

Does the project provide a demo instance?

## Freeness

How "free" the project is, rated on a scale of 0-10:

- **10**: Everything is completely free with no paywalls, subscriptions, or limitations. The project is truly open-source and can be self-hosted without any costs or restrictions.
- **8-9**: Mostly free but may have optional paid features or premium support offerings that don't affect core functionality.
- **6-7**: Some features may be limited or have soft paywalls, but the core functionality remains accessible.
- **4-5**: Major features are locked behind paywalls, or the license has significant limitations that restrict usage for certain use cases.
- **2-3**: Heavy reliance on paid features or subscriptions for basic functionality.
- **0-1**: Not free at all - requires payment for any meaningful use, probably will not be included in the list if the vote is so low.

## Web App

Is a web interface provided?

## Android App

Is an Android app provided?

## iOS App

Is an iOS app provided?

## Desktop App

Is a desktop app provided?

## Voice Chat

Does the platform support voice communication between users?

## Noise Cancelling

Does the platform support noise cancellation or noise suppression during voice communication (e.g. via RNNoise, Speex, or browser-native suppression)?

## Video Chat

Does the platform support video calls or conferencing?

## File Sharing

Can users share files within the platform?

## Channels/Rooms

Does the platform support organizing conversations into channels or rooms?

## User Roles/Permissions

Can user roles and permissions be defined and managed?

## Encryption

Does the platform provide encryption for messages and data, rated on a scale of 0-10:

- **10**: End-to-end encryption (E2EE) for all communications (messages, voice, video, files) with perfect forward secrecy. Client-side encryption keys, zero-knowledge architecture. No server access to decrypted content.
- **8-9**: Strong E2EE for most communications with modern protocols (Signal Protocol, Double Ratchet, or similar). May lack E2EE for some features like group calls or have minor key management limitations.
- **6-7**: E2EE available but optional or only for specific communication types (e.g., DMs only). Transport-layer encryption (TLS) for all connections. Server has some access to metadata or keys.
- **4-5**: Transport-layer encryption only (TLS/SSL). Messages encrypted in transit but stored unencrypted or with server-side keys. Server can access message content.
- **2-3**: Basic or incomplete encryption implementation. Significant security gaps, outdated protocols, or encryption only for some connections.
- **0-1**: No encryption or completely insecure implementation. Not recommended for any sensitive communications.

**Note:** Audited encryption implementations, proper key management, and open-source cryptographic libraries significantly influence the score. Custom or unvetted encryption will lower the rating.

## Ease of Setup

How easy is it to set up and deploy the platform, rated on a scale of 0-10:

- **10**: Extremely simple setup - single docker-compose file or one command with just a domain needed to expose it. No complex configuration required.
- **8-9**: Very easy setup - docker-compose with minimal configuration, or simple installation script. May require basic domain setup and minimal port configuration.
- **6-7**: Moderate setup complexity - requires multiple steps, port exposure, or multiple domains. Some technical knowledge needed but well-documented.
- **4-5**: Complex setup - involves multiple services, extensive configuration, custom networking, or significant infrastructure requirements.
- **2-3**: Very complex setup - requires deep technical expertise, custom development, or integration with multiple external services.
- **0-1**: Extremely difficult setup - only expert users can successfully deploy, requires extensive system administration knowledge and troubleshooting.

**Note:** Documentation quality significantly influences the score. Poor, incomplete, or missing documentation will lower the rating, even if the technical setup complexity is moderate.

## Screensharing

Does the platform support screen sharing during video calls?

## Screensharing Audio

Does the platform support audio sharing during screen sharing (system audio capture)?

## Plugins

Does the platform support plugins or extensions for additional functionality?

## Stability

How stable and reliable is the platform in terms of uptime and performance? A "wip" rating may also indicate that the application has not yet had an out-of-beta release.

## Authentication Providers

Are alternative authentication providers supported? (OAuth, LDAP, etc.)

## Translation

Does the platform support languages other than english, the number of translated language influence the score
