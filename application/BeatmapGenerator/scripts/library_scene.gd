extends Node2D

func _on_quit_button_pressed():
	get_tree().change_scene("res://scenes/main_scene/main_scene.tscn")

func _on_temp_go_to_gameplay_pressed():
	get_tree().change_scene("res://scenes/gameplay_scene/gameplay_scene.tscn")

func _on_download_button_pressed():
	get_tree().change_scene("res://scenes/download_scene/download_scene.tscn")
