---
name: browse-collections
description: Look inside Spotify content you already have a URI for. Use when the user asks what tracks are on a playlist or album, which episodes a podcast has, the chapters of an audiobook, or details about specific items already shown in the chat, or when a generated playlist's tracks are needed. Covers get_entity (metadata for up to 20 URIs) and get_collection_items (paginated contents, with polling for playlists still being generated). Do not use to discover content from text; use search for that.
---

# Browse playlists, albums, shows, and items

Explicit user instructions take priority over this guidance.

## Pick the tool

| Need                                                                               | Tool                                                                           |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Metadata for items you hold URIs for (name, creators, availability, library state) | `get_entity`                                                                   |
| The tracks, episodes, or chapters inside a playlist, album, podcast, or audiobook  | `get_collection_items`                                                         |
| Finding content from a name or description                                         | `search` or `query_catalog` (see [search-spotify](../search-spotify/SKILL.md)) |

You don't need the contents to share or play a collection. Its link works as soon as you have it.

## get_entity

- `uris`: up to 20 Spotify URIs per call, from earlier results or pasted by the user. Never construct URIs.
- `language`: the user's BCP 47 locale (`en-US`, `sv-SE`, `pt-BR`). Required.
- Entities come back in request order. URIs that couldn't be resolved are listed in `unresolved` with a reason; tell the user those weren't found rather than dropping them silently.
- Works signed out for public content; signed in adds availability and library status.

## get_collection_items

- `uri`: a playlist, album, or show (podcast or audiobook) URI.
- `page_size`: default 10, max 60. Ask for only what you need.
- Pagination: pass `pagination.next_cursor` as `cursor` for the next page. With a cursor, omit `page_size` or repeat the first page's exact value; a different value is rejected.
- `total_items` counts items before availability filtering and may be absent for dynamic playlists. Don't promise an exact count from it.
- Podcasts usually list newest episodes first.

## Status and polling

Check `status` before using the contents:

| `status`                 | Action                                                                                                                                                                                                                                                                                      |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `READY`                  | Contents are complete.                                                                                                                                                                                                                                                                      |
| `GENERATION_IN_PROGRESS` | A generated playlist is still being assembled. Retry with the same `uri` and pagination arguments at most 5 times, waiting 2, 4, 8, 16, then 30 seconds. If it's still pending, stop, share the playlist link, and tell the user the tracks aren't ready yet. Retry later only if they ask. |
| `FAILED`                 | Stop polling and tell the user the contents couldn't be loaded.                                                                                                                                                                                                                             |

## Presenting

- Include the Spotify link for each item you list. Use names and links exactly as returned.
- Some items may be hidden for availability or licensing reasons. If `explanations` say results were filtered, mention it briefly when relevant.
