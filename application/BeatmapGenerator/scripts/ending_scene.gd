extends Node2D

func _ready():
	$grade/gradebox.text = global.grade
	$score/scorebox.text = str(global.score)
	$perfect/perfects.text = str(global.perfect)
	$great/greats.text = str(global.great)
	$good/goods.text = str(global.good)
	$missed/misses.text = str(global.missed)
	
func _on_quit_button_pressed():
	if get_tree().change_scene("res://scenes/main_scene.tscn") != OK:
		print ("Error changing scene to main menu")

func _on_replay_button_pressed():
	if get_tree().change_scene("res://scenes/gameplay_scene.tscn") != OK:
		print ("Error changing scene to gameplay")

func _on_new_song_button_pressed():
	if get_tree().change_scene("res://scenes/download_scene.tscn") != OK:
		print ("Error changing scene to download scene")
