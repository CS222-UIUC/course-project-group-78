# Beatmap Generator

#### CS222 Course Project Group 78

By: Akul Datta, Relena Li, Nisha Prasad, Kevin Wang

### Pitch

Rhythm games are a source of entertainment beloved by many, with fast-paced and engaging gameplay; however, many of them lack music that caters to each player’s individual tastes. A Beatmap Generator amplifies this experience by allowing players to automatically create levels to their own submitted music files.

### MVP Functionality

1. Users can submit music files

2. Users can generate beatmaps from music files

3. Users can play beatmaps

### Components

We decided to split our project into frontend and backend segments to increase the organization and modifiability of our code. 

#### Backend: 

Akul - Music conversion

Kevin - Algorithms

Relena - testing

We will write the backend using Python with music analysis libraries such as Librosa.

The backend has to do the following tasks:

1. Analyze Music

2. Generate Beatmaps 
   1. We will use Librosa, a Python music analysis library
   
3. Save and export beatmap files

#### Frontend: (Nisha)

We will write the front end of our software with the Godot game engine using C++. We will create a simple GUI and login page with the front end. We will write tests for Godot using catch2.

The frontend has to do the following tasks:
1. Accept music files

2. Play music

3. Retrieve beatmap files

4. Allow users to play the game

5. Determine scores with synchronization

### How to use:

Due to issues with exportation, at the moment it is necessary to download the Godot engine and the project, then import the project.godot file into the engine. After that, if you click on the play button in the top right corner, the application will launch and you can run it.

