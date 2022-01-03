# Spotify

Code to parse Spotify data.

# Install requirements

You must have Python 3 locally.

```
pip3 install -r requirements.txt
```

# Move data to correct folder

Your data from Spotify will include one or more files that have names beginning with "endsong". Create a folder in
this repository directory called "data" and move your files into there.

# Run python script

From the top level of this repository, run:

```
python3 parse_data.py
```

The output files will be saved to a dirctory called `output`. Four files are created:

1. Your top 1000 songs, only including plays where you listened for 30 or more seconds (as to reduce songs you quickly skipped).
2. Your top 1000 songs, with no time limits.
3. Your top 1000 artists, only including plays where you listened for 30 or more seconds (as to reduce songs you quickly skipped).
4. Your top 1000 artists, with no time limits.
