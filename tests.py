# Using the re module to test output

import re

# Random Example API response
api_response = "Here is some sample data: Movie Title (2022), [Verse 1] Lyrics go here, @username1, ISBN 123-4-567-89012-3, Why did the chicken cross the road? Because it wanted to get to the other side, Show Name S02E03: Episode Title, 17-May-2023, #ABC123, IP Address: 192.168.0.1"

# Extract and print movie titles
movie_titles = re.findall(r"(.+) \(\d{4}\)", api_response)
print("Movie Titles:", movie_titles)

# Extract and print song lyrics
song_lyrics = re.findall(r"\[Verse \d+\] (.+)", api_response)
print("Song Lyrics:", song_lyrics)

# Extract and print dates
dates = re.findall(r"\d{2}-[A-Z]{3}-\d{4}", api_response)
print("Dates:", dates)

# ISBN numbers
ISNB_numbers = re.findall(r"ISBN \d{3}-\d-\d{3}-\d{5}-\d", api_response)
print("ISNB numbers", ISNB_numbers)
