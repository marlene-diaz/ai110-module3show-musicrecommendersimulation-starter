# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

VibeMatch 1.0


---

## 2. Intended Use  

This system generates song recommendations based on a user’s preferred genre, mood, and energy level.
It assumes that users have consistent taste and that these three features are enough to describe a musical “vibe.”

 It simplifies how platforms like Spotify work by focusing only on content-based filtering 
 instead of using large-scale user behavior data.

---

## 3. How the Model Works  

The model looks at each song’s features—specifically genre, mood, and energy—and compares them to the user’s preferences.
 If a song matches the user’s genre, it gets the most points. If it matches the mood, it gets additional points.

For energy, the system doesn’t just check if it’s high or low. Instead, it calculates how close the song’s energy is to the user’s preferred energy. Songs with similar energy levels receive higher scores.

After scoring every song, the system ranks them from highest to lowest score and recommends the top results.this version adds a realistic energy similarity calculation and includes explanations (“reasons”) for each recommendation.
---

## 4. Data  

The model uses a small dataset of songs stored in a CSV file, with around 10–20 songs. 
Each song includes features such as genre, mood, energy, and tempo.

The dataset includes a limited range of genres and moods, which means it cannot fully represent all types of musical taste.
 Some styles, like niche genres or mixed moods, may be missing. I added a few additional songs to increase diversity, 
 but the dataset is still relatively small.
---

## 5. Strengths  

The system works well for users with clear and simple preferences, such as “happy pop” or “intense rock.” .the recommendations feel accurate because the scoring strongly prioritizes matching genre and mood.

It also captures the idea of “vibe” pretty good through the energy similarity calculation. Songs with similar intensity levels tend to appear near the top, which often matches real listening preferences.

---

## 6. Limitations and Bias 

One major limitation is that the system over-prioritizes genre. Songs outside the preferred genre rarely 
appear, even if they match the mood and energy very well.

The dataset is  small and not diverse, it can create a bias toward the most common genres included. 
lastly, the model does not consider other important features like lyrics, artist similarity, or user listening history.

Because of this, the system may produce repetitive recommendations and don't introduce new or unexpected songs.

## 7. Evaluation  

I tested the system using multiple user profiles, including “high-energy pop,” “chill lofi,” and “intense rock.”
 I checked whether the top recommendations matched what I would expect for each type of listener.

One surprising result was that the same songs sometimes appeared across different profiles, especially when 
genre matched strongly. This showed that the genre weight might be too high.

I also experimented with changing the importance of energy, which changed the rankings and helped confirm that the scoring system is wary to feature weights.
---

## 8. Future Work  

To improve the model, I would add more features such as danceability, acousticness, or artist similarity.

I would also expand the dataset to include more songs and genres to improve diversity. Another improvement 
would be adjusting the scoring weights so the system can better balance genre, mood, and energy.

Finally, I would explore adding collaborative filtering so recommendations could be influenced by other users’ behavior.
---

## 9. Personal Reflection  

This project helped me understand how recommendation systems break down into scoring and ranking steps. I learned 
that even simple rules can produce results that feel personalized.

One interesting takeaway was how sensitive the system is to weights—small changes and shift recommendations.

This made me realize that real-world apps like Spotify are much more complex, but they are built on the
 same core ideas of matching user preferences to content.
