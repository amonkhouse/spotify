import os

import pandas as pd

song_files = [f"data/{file}" for file in os.listdir(
    'data/') if file.startswith('endsong')]

df = pd.read_json(song_files[0])

for song_file in song_files[1:]:
    df = df.append(pd.read_json(song_file), ignore_index=True)

df_filtered = df[df['ms_played'] >= 30000]


def get_most_played_info(df, columns, filename, limit=1000):
    play_counts_df = df.groupby(by=columns)[['ms_played']].count()
    play_counts_df.columns = ['total_plays']
    play_counts_df = play_counts_df.sort_values(
        by='total_plays', ascending=False)
    play_counts_df.iloc[:limit, :].to_csv(filename)


if not os.path.exists('output'):
    os.makedirs('output')

get_most_played_info(df_filtered, ['master_metadata_track_name',
                     'master_metadata_album_artist_name'], 'output/most_played_songs_30secs_or_more.csv')
get_most_played_info(df, ['master_metadata_track_name',
                     'master_metadata_album_artist_name'], 'output/most_played_songs_no_playtime_filter.csv')
get_most_played_info(df_filtered, [
                     'master_metadata_album_artist_name'], 'output/most_played_artists_with_songtime_filter.csv')
get_most_played_info(df, ['master_metadata_album_artist_name'],
                     'output/most_played_artists_without_songtime_filter.csv')
