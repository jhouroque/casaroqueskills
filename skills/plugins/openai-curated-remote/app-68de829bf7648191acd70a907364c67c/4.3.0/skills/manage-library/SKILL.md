---
name: manage-library
description: Save or remove Spotify content in the user's library. Use when the user explicitly asks to save, like, add to library, follow an artist, podcast, or someone else's playlist, or the reverse (unsave, unlike, remove, unfollow) for a track, album, playlist, artist, podcast show, episode, or audiobook. Do not use proactively, on behalf of third parties, or to add tracks to a playlist.
---

# Manage the user's library

Explicit user instructions take priority over this guidance.

## When to act

- Only call `save_to_library` or `remove_from_library` when the user explicitly asks. Never save things just because they were recommended or played.
- "Add this to my workout playlist" is a playlist edit, not a library save (see [build-playlists](../build-playlists/SKILL.md)).
- Following an artist or podcast is a save; unfollowing is a remove.

## Getting the URI

- Any valid Spotify URI works: one from an earlier tool result (`search`, `query_catalog`, `get_entity`, `get_collection_items`, `get_currently_playing`) or one the user pastes. Never construct or guess one.
- If you don't have it yet, find the item first, and confirm with the user if more than one result could match.
- Supported: `spotify:track:`, `spotify:album:`, `spotify:playlist:`, `spotify:artist:`, `spotify:show:` (podcasts and audiobooks), `spotify:episode:`.
- One URI per call. For several items, make one call per item.
- "Save this song" usually means the song just discussed: reuse that result's URI. Call `get_currently_playing` (now-playing) only when the user means what is playing now ("like what's playing", "save the song on right now"). If it's unclear which song they mean, ask.

## Before calling

If the entity already shows `library_status`, use it:

| `library_status` | Meaning                                                                                                                               |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `SAVED`          | Already saved; don't save again. Removable.                                                                                           |
| `NOT_SAVED`      | Can be saved.                                                                                                                         |
| `NOT_SAVEABLE`   | Don't call `save_to_library`. This also covers the user's own playlists, which are already in their library and can still be removed. |
| `PRE_SAVED`      | Unreleased item the user pre-saved. Treat as saved.                                                                                   |

## After calling

- Success: `save_to_library` returns `library_status: SAVED`; `remove_from_library` returns `NOT_SAVED`. Confirm to the user by name, with the Spotify link.
- If `library_status` is absent, the call failed. Never claim success.

| Error              | Action                                                       |
| ------------------ | ------------------------------------------------------------ |
| `NOT_SAVEABLE`     | Don't retry. Tell the user Spotify can't save this item.     |
| `INVALID_ARGUMENT` | The URI was wrong. Re-find the item, then retry once.        |
| `RATE_LIMITED`     | Wait a moment, then retry once.                              |
| `INTERNAL_ERROR`   | Retry once; if it fails again, tell the user it didn't work. |
