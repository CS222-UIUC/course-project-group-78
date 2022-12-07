extends AudioStreamPlayer

var audio_loader = AudioLoader.new()

var note_idx = 0
var song_position = 0.0

signal spawn

func _on_music_conductor_ready():
	$note_timer.wait_time = float(global.beatmap[note_idx][2])
	set_stream(audio_loader.loadfile(global.audio_file))
	volume_db = -5
	pitch_scale = 1

func _process(_delta):
	if playing:
		song_position = get_playback_position() + AudioServer.get_time_since_last_mix()
		song_position -= AudioServer.get_output_latency()

func _on_note_timer_timeout():
	if note_idx < global.beatmap.size():
		emit_signal("spawn", note_idx)
		note_idx += 1
		if note_idx < global.beatmap.size():
			if playing:
				$note_timer.wait_time = float(global.beatmap[note_idx][2]) - song_position
				$note_timer.start()
