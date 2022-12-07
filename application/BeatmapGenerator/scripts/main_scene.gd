extends Node2D

func _ready():
	pass

func _on_start_button_pressed():
	if get_tree().change_scene("res://scenes/download_scene.tscn") != OK:
		print ("Error changing scene to download scene")
