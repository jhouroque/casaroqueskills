---
name: now-playing
description: Tell the user what is playing on their Spotify right now. Use only when the user directly asks what song, track, episode, or audiobook is currently playing on Spotify, or explicitly refers to what is playing now. Not for "this song" when a song was just discussed in the chat. Do not call proactively, and do not use for play, pause, skip, or other playback control, which is not available.
---

# What's playing now

Explicit user instructions take priority over this guidance.

## When to call

- Call `get_currently_playing` (no arguments) only when the user asks what is playing, or explicitly refers to what is playing now ("save the song on right now"). For "save this song" or "more like this", reuse the item discussed in the conversation; ask if the reference is ambiguous.
- Don't call it proactively or to start a conversation.
- Play, pause, skip, queue, and volume aren't supported. Say so, and point the user to the Spotify app.

## Using the result

- Attribute playback to Spotify: "This is playing on Spotify: ...". Include the item's Spotify link.
- If nothing is playing, say there's no active Spotify playback right now.
- For follow-ups, reuse the returned entity's URI:
  - "Save this" → `save_to_library` (see [manage-library](../manage-library/SKILL.md)).
  - "More like this" → `search` with a prompt such as "more like <track> by <artist>" (see [search-spotify](../search-spotify/SKILL.md)).

## Errors

| Error                                                           | Action                                                                                   |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `LICENSOR_RESTRICTED`                                           | Something is playing, but it can't be shown. Say the current content can't be displayed. |
| `DEVICE_UNAVAILABLE`                                            | No active Spotify device. Suggest opening Spotify and starting playback.                 |
| `CONTENT_NOT_PLAYABLE`, `CONTENT_NOT_AVAILABLE`, `NOT_ELIGIBLE` | Say the current item isn't available to show. Don't retry.                               |
| `UNKNOWN_ERROR`                                                 | Retry once, then say something went wrong.                                               |
