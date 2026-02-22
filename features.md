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

This score includes not only pricing/licensing, but also long-term project independence for self-hosters:
- Can the full stack be forked and continued without the original team?
- Is the protocol/API open enough that communities are not locked into one core team direction?

- **10**: Fully free and fully forkable. No paywalls on core functionality, full server/client stack is open-source, and self-hosting does not depend on proprietary closed components controlled by one team.
- **8-9**: Mostly free with minor limitations, or open-source full stack with some medium-term ecosystem/protocol lock-in concerns that do not currently block normal self-hosting.
- **6-7**: Core functionality is accessible, but there are meaningful constraints (feature gating, weak licensing terms, or significant dependence on one team's protocol direction).
- **4-5**: Major features are limited, the stack is only partially open, or long-term self-hosting/forkability risk is high.
- **2-3**: Heavy reliance on paid features/subscriptions or mostly non-forkable architecture for meaningful use.
- **0-1**: Not free in practice for meaningful use.

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

## UI Vote

This is a more personal vote since it is difficult to be objective. It is taken into consideration the similarity with Discord UI, the simplicity, and aesthetic. The UI Vote links to a detailed comparison page with screenshots where you can see the actual interface of each project.
