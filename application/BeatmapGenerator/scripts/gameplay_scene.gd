extends Node2D

var score = 0
var perfect = 0
var great = 0
var good = 0
var missed = 0

var script_output =[]
var note = load("res://scenes/notes_scene.tscn")
var instance

func _on_quit_button_pressed():
	if get_tree().change_scene("res://scenes/main_scene.tscn") != OK:
		print ("Error changing scene to main menu")

func _on_gameplay_scene_ready():
	var t = Timer.new()
	t.set_wait_time(2)
	t.set_one_shot(true)
	self.add_child(t)
	$music_conductor/note_timer.start()
	t.start()
	yield(t, "timeout")
	t.queue_free()
	$music_conductor.play()

func _on_music_conductor_spawn(note_idx):
	_spawn_note(note_idx)

func _spawn_note(idx):
	instance = note.instance()
	var lane = global.beatmap[idx][1]
	if lane == 'r':
		instance.initialize(0)
	elif lane == 'u':
		instance.initialize(1)
	elif lane == 'd':
		instance.initialize(2)
	else:
		instance.initialize(3)
	add_child(instance)

func increment_score(by):
	score += by
	if by == 3:
		perfect += 1
	elif by == 2:
		great += 1
	elif by == 1:
		good += 1
	else:
		missed += 1
	$score/scorebox.text = str(score)

func _on_music_conductor_finished():
	global.perfect = perfect
	global.great = great
	global.good = good
	global.missed = missed
	global.set_score(score)
	if get_tree().change_scene("res://scenes/ending_scene.tscn") != OK:
		print ("Error changing scene to end")
