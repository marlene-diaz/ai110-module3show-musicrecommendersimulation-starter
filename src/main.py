"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""
from src.recommender import load_songs, recommend_songs

def main():
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}\n")

    user = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8
    }

    results = recommend_songs(user, songs, k=5)

    print("Top Recommendations:\n")
    for song, score, reasons in results:
        print(f"{song['title']} (Score: {round(score,2)})")
        for r in reasons:
            print(f"  - {r}")
        print()

if __name__ == "__main__":
    main()