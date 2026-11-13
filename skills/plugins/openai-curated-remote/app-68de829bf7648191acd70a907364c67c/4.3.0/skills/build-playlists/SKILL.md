---
name: build-playlists
description: Creates and edits Spotify playlists. Use when the user explicitly asks to create, make, or generate a playlist, build one from songs discussed in the chat, or add, remove, rename, redescribe, or make collaborative an existing playlist. Excludes recommendations only, finding existing playlists, saving someone else's playlist, and audiobooks in playlists.
---

# Build and edit playlists

Explicit user instructions take priority over this guidance.

## Confirm intent first

- Only create a playlist when the user clearly asks for one. "Suggest workout songs" or "find me a party playlist" is a search, not a creation (see [search-spotify](../search-spotify/SKILL.md)).
- Hypothetical or tentative asks ("I might want a playlist...") wait until the user confirms.
- If the request has no detail ("make me a playlist"), ask for a mood, genre, activity, or artists before calling anything.
- `generate_playlist` builds music playlists only. For a playlist of specific podcast episodes, use `create_playlist` + `add_playlist_items` with the episode URIs.
- Audiobooks can't be added to playlists (only tracks and episodes can). Offer to save the audiobook instead.

## Pick the path

| Situation                                                                                             | Path                                                                                   |
| ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| User describes a vibe, theme, activity, or artists and wants Spotify to choose tracks                 | `generate_playlist`                                                                    |
| User wants specific tracks: a list they gave, songs from earlier in the chat, a tracklist from a file | `create_playlist`, then `add_playlist_items`                                           |
| `generate_playlist` didn't produce a playlist (see below)                                             | `search` for tracks, then `create_playlist` + `add_playlist_items`, if the user agrees |

## generate_playlist

- `prompt` must start with the creation intent ("Create a...", "Make a..."). Add it if the user's wording lacks it.
- Keep the user's original language and context words ("my", "by", "from"). Replace private user identifiers with "me"/"my"; preserve artist, author, narrator, and content names exactly. Merge multi-turn context into one request. Convert durations to minutes. Do not add constraints the user didn't ask for.
- `language`: the user's BCP 47 locale. Required.
- The playlist is private to the user.
- Requires a signed-in user with Spotify Premium. If the response carries `NOT_SUBSCRIBED` or the explanation `PREMIUM_REQUIRED_FALLBACK`, no playlist was created. Tell the user that generating playlists from a description needs Spotify Premium, and offer to build one from search results with `create_playlist` and `add_playlist_items` instead.
- Tracks are assembled after the call returns. The playlist link is valid right away; share it. To read the tracks, call `get_collection_items` on the playlist URI and follow its polling rules (see [browse-collections](../browse-collections/SKILL.md)).

## create_playlist + add_playlist_items

1. Resolve each track to a URI first with `search` or `query_catalog`. Never invent or guess URIs.
2. `create_playlist` with `name` (required), optional `description`, and `collaborative` (defaults to false). New playlists are private.
3. Check `result` is `APPLIED`, then take `entity.uri`.
4. `add_playlist_items` with `playlist_uri` and `uris` (tracks and episodes only, up to 100 per call; split larger lists). Items append to the end.
5. Check every `add_playlist_items` response. On failure, stop and tell the user which batches were added and which failed; don't describe a partially populated playlist as complete.
6. Share the playlist link from the `create_playlist` response.

## Editing an existing playlist

- If `can_edit_items` is false, don't try to edit; tell the user they can't edit this playlist. If it is absent (common for collaborative playlists), editability is unknown: go ahead when the user asks, and rely on the tool's `NOT_PERMITTED` result.
- `add_playlist_items`: append tracks or episodes.
- `remove_playlist_items`: removes every occurrence of each URI. Confirm with the user before removing items they did not name explicitly.
- `update_playlist_details`: change `name`, `description`, or `collaborative`. Send at least one.

## Handoffs

- Tracks from an earlier search, query_catalog, or browse-collections result are already resolved: reuse their URIs instead of searching again.
- "Add what's playing to my playlist": get the URI with `get_currently_playing` (now-playing), then `add_playlist_items`.

## Reading the result

All edit tools return `result`:

| `result`        | Meaning                                               | Action                                                                                                                                                                                                                                                                                   |
| --------------- | ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `APPLIED`       | Done                                                  | Confirm to the user with the playlist link                                                                                                                                                                                                                                               |
| `NOT_FOUND`     | Playlist doesn't exist                                | Re-check the URI; don't retry blindly                                                                                                                                                                                                                                                    |
| `NOT_PERMITTED` | User can't edit it                                    | Tell the user; offer to create their own copy                                                                                                                                                                                                                                            |
| `CHANGE_FAILED` | Unexpected failure; the change may still have applied | Don't retry `create_playlist` or `add_playlist_items`, which would duplicate the playlist or its tracks. Tell the user it may not have worked and offer to check the playlist with `get_collection_items`. `remove_playlist_items` and `update_playlist_details` are safe to retry once. |

Never claim a change happened unless `result` is `APPLIED`.
