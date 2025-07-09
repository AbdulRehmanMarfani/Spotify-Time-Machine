---

# 🎵 Billboard to Spotify Playlist Creator

Automatically create a Spotify playlist of the **Billboard Hot 100** songs for any past date using Python, BeautifulSoup, and Spotipy.

---

## 📌 Features

* 🔎 Scrapes Billboard Hot 100 chart for a specific date.
* 🔗 Searches Spotify for each song using the Spotify Web API.
* ✅ Creates a new private Spotify playlist (or updates an existing one).
* 🎧 Adds all matched songs to the playlist.
* 📄 Logs songs that could not be found on Spotify.

---

## 🖥️ Tech Stack

* **Python 3.7+**
* **BeautifulSoup** – Web scraping Billboard
* **Requests** – HTTP requests
* **Spotipy** – Python client for Spotify Web API
* **dotenv (optional)** – For environment variable management

---

## 🔐 Requirements

Before running the script, you’ll need:

1. **A Spotify Developer account**
2. A registered application to get:

   * `Client ID`
   * `Client Secret`
   * `Redirect URI`

You can register at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/billboard-spotify-playlist.git
cd billboard-spotify-playlist
```

### 2. Create and Activate a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory and add the following:

```
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
```

Alternatively, you can export them manually:

```bash
export SPOTIPY_CLIENT_ID=your_client_id
export SPOTIPY_CLIENT_SECRET=your_client_secret
export SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
```

---

## 🚀 Usage

Run the script using:

```bash
python main.py
```

You'll be prompted to enter a date in the format:

```
Which date do you want to travel to? (YYYY-MM-DD):
```

Example:

```
Which date do you want to travel to? (YYYY-MM-DD): 2008-07-12
```

The script will:

1. Scrape the Billboard Hot 100 chart for that date.
2. Search Spotify for each song and artist.
3. Create a playlist in your account.
4. Add all found songs to it.

---

## 📦 Sample Output

```
Playlist 'Billboard Hot 100 - 2008-07-12' created successfully!
Added 94 songs to the playlist.
6 songs not found on Spotify:
- Song 'XYZ' by 'Artist1'
- Song 'ABC' by 'Artist2'
...
```

---

## 🛑 Known Limitations

* Some songs may not be available on Spotify due to licensing issues.
* Artist names may not always match perfectly (leading to missed matches).
* Billboard page structure may change in the future, requiring parser updates.

---

## 📁 File Structure

```
.
├── main.py
├── requirements.txt
├── .env (optional)
└── README.md
```

---

## 🧠 Future Improvements

* Add support for other Billboard charts (Global, Rock, etc.)
* Build a GUI or web interface using Flask
* Add optional public playlist creation
* Save unmatched songs to a `.txt` file for review

---

## 👨‍💻 Author

**Abdul Rehman Marfani**
[Portfolio](https://abdulrehmanmarfani.github.io/portfolio/) · [GitHub](https://github.com/AbdulRehmanMarfani) · [LinkedIn](https://linkedin.com/in/abdul-rehman-marfani-4aa587276)

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---
