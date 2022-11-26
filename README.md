# Beatmap Generator

#### CS222 Course Project Group 78

By: Akul Datta, Relena Li, Nisha Prasad, Kevin Wang

### Pitch

Rhythm games are a source of entertainment beloved by many, with fast-paced and engaging gameplay; however, many of them lack music that caters to each player’s individual tastes. A Beatmap Generator amplifies this experience by allowing players to automatically create levels to their own submitted music files.

### MVP Functionality

1. Users can submit music files

2. Users can generate beatmaps from music files

3. Users can play beatmaps

4. Users can save beatmaps

5. Users can export beatmap files

6. Users can view saved beatmaps

### Components

We decided to split our project into frontend and backend segments to increase the organization and modifiability of our code. 

#### Backend: 
We will write the backend using Python with music analysis libraries such as Librosa.

The backend has to do the following tasks:

1. Analyze Music

2. Generate Beatmaps 
   1. We will use Librosa, a Python music analysis library
   
3. Save and export beatmap files

#### Frontend: 
We will write the front end of our software with the Godot game engine using C++. We will create a simple GUI and login page with the front end. We will write tests for Godot using catch2.

The frontend has to do the following tasks:
1. Play Music
2. Allow users to play the game, determine scores with synchronization

### How to use:

to be implemented...

