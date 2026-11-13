---
name: search-spotify
description: Finds and recommends Spotify music, podcasts, and audiobooks. Use for discovery, mood or activity requests, "more like X", known-title lookups, finding existing playlists, listening history, and saved-content queries. Excludes playlist creation or editing, library mutations, current-playback identification, lyrics, concerts, artist bios, and music news.
---

# Find music, podcasts, and audiobooks

Explicit user instructions take priority over this guidance.

## Pick the tool

| Request                                                                        | Tool                                                                    |
| ------------------------------------------------------------------------------ | ----------------------------------------------------------------------- |
| Mood, vibe, activity, genre, "something like X", recommendations               | `search`                                                                |
| Listening history, recently played, top artists, Liked Songs, "my playlists"   | `search` (personalized when signed in)                                  |
| Vague or partial memories ("that song from the Barbie movie")                  | `search`                                                                |
| Known titles with trusted values, e.g. a list of albums with artists and years | `query_catalog`                                                         |
| Several known items at once ("these 6 albums")                                 | `query_catalog`, one call with up to 10 `queries`                       |
| You already hold Spotify URIs                                                  | `get_entity` (see [browse-collections](../browse-collections/SKILL.md)) |

When unsure, use `search`. A `search` call on a known title is never wrong; `query_catalog` on a mood or description returns nothing useful.

## Calling search

- `prompt`: pass the user's wording as-is, in their original language. Do not translate or reduce it to keywords.
- Allowed rewrites only (plus adding "audiobook" for audiobook requests, see below):
  - Replace private user identifiers (the user's own name, usernames) with "me" or "my". Preserve artist, author, narrator, and content names exactly.
  - Merge multi-turn context into one self-contained request. Prefer one search for "a + b + c" over three searches.
  - Convert durations to minutes ("2 hours" becomes "120 minutes").
- `language`: the user's BCP 47 locale (`en-US`, `sv-SE`, `pt-BR`). Required.
- Expect at most 5 results per call, whatever `limit` says. To show more variety, run a second, differently-phrased search rather than raising `limit`.
- Personalization is automatic when the user is signed in. Do not add phrases like "based on my taste" unless the user said them.

## Calling query_catalog

- One object per item: `query` is the title or name, plus optional `creator` (artist, publisher, author, or narrator), `year` (`"1977"` or `"1975-1980"`), and `entity_types` (`MUSIC`, `TALK`, `BOOK`, `COLLECTION`, `CREATOR`).
- Results come back as one group per query, in input order. Read each group's `entities`, `warnings`, and `error` on their own.
- If some groups failed temporarily, keep the successful ones and retry only the failed queries.
- If a group is empty and the input might be conversational or misremembered, retry that item with `search`.

## Audiobooks

- Treat book requests ("listen to a book", "an audiobook for my commute", "books by Brandon Sanderson") as audiobook searches. Say "audiobook" in the `search` prompt so results lean toward books rather than podcasts about the book.
- Known title: `query_catalog` with the title in `query`, `entity_types: ["BOOK"]`, and the author or narrator in `creator` if known.
- Author- or narrator-only requests ("books by Brandon Sanderson"): use `search`. `query_catalog` matches titles, so an author name alone can miss their books.
- Audiobooks use `spotify:show:` URIs, like podcasts. Use `entity_type` `BOOK` (audiobook) vs `TALK` (podcast) to tell them apart, and call it an audiobook when describing it.
- Credit the author and, when present, the narrator.
- Chapters: `get_collection_items` on the audiobook URI (see [browse-collections](../browse-collections/SKILL.md)). Saving: `save_to_library` with the same URI (see [manage-library](../manage-library/SKILL.md)).
- Some audiobooks are not playable for every user. If an item comes back not playable, say it isn't available to them and offer alternatives; don't retry.

## Presenting results

- Include the Spotify link for every item you mention. Use only links and names from the tool output; never construct URLs or alter names.
- Lead with playlists for mood and activity requests. People usually want a ready-made listening experience, not a list of tracks.
- Attribute to Spotify ("Here's what I found on Spotify").
- `search` is read-only. Never say something was saved, followed, played, or added.

## Errors and explanations

| Signal                                                                                                  | What to do                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `NO_CONTENT`                                                                                            | Rephrase once (broader, or with different context). If still empty, tell the user Spotify couldn't find it.                                                    |
| `CONTENT_NOT_AVAILABLE`, `LICENSOR_RESTRICTED`, `ALL_CONTENT_LICENSOR_RESTRICTED`, `RESTRICTED_CONTENT` | Do not retry. Say the content isn't available on Spotify for them and offer alternatives.                                                                      |
| `EXPLICIT_CONTENT_FORBIDDEN`                                                                            | Do not retry. Explain explicit content is blocked on their account; suggest a non-explicit alternative.                                                        |
| `INVALID_ARGUMENT`                                                                                      | Fix the arguments (usually `language` or an empty `prompt`) and retry silently once.                                                                           |
| `TEMPORARILY_UNAVAILABLE`, `UNKNOWN_ERROR`                                                              | Retry once, then tell the user something went wrong.                                                                                                           |
| Explanation `NOT_A_CONTENT_REQUEST`                                                                     | Answer from your own knowledge. Do not retry the search.                                                                                                       |
| Explanation `RESULTS_FILTERED_*`                                                                        | Results were partly hidden for region, age, explicit, or licensing reasons. Present what came back; mention filtering if the user asked for something missing. |
| Explanation `RESULTS_TRUNCATED`                                                                         | More matches exist. Offer to look further.                                                                                                                     |
| Explanation `NO_PLAYABLE_RESULTS`                                                                       | Matches exist but none are playable for this user. Say so and offer alternatives.                                                                              |

## Handoffs

- "Make a playlist from these" after a search: use build-playlists (create_playlist + add_playlist_items) with the URIs you already have. Don't search again.
- "Save the second one", "follow this artist": use manage-library with the URI from the results.
- "What's on this album/playlist?": use browse-collections with the result's URI.

## Out of scope

For lyrics, transcripts, concerts, tour dates, artist bios, music news, or creating podcasts, tell the user they can find this in the Spotify app or answer from general knowledge. Do not call these tools for it.
