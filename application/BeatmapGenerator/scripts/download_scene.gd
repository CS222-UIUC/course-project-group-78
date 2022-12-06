extends Node2D

func _on_quit_button_pressed():
	if get_tree().change_scene("res://scenes/main_scene.tscn") != OK:
		print ("Error changing scene to main menu")

func _on_select_button_pressed():
	$download_file.popup()
	$download_file.invalidate()

func _on_download_file_file_selected(path):
	if path.ends_with(".mp3"):
		global.audio_file = str(path)
		var python = ProjectSettings.globalize_path("res://addons/pythonscript/windows-64/python.exe")
		var backendfile = ProjectSettings.globalize_path("res://beatmaps/backend.py")
		var out = []
		# global.reset_csv()
		var exit = OS.execute(python, [backendfile, global.audio_file], true, out, true)
		if exit == OK:
			global.load_csv()
		else:
			printerr("Error running backend")
			print(out)
	else:
		printerr("Not an MP3 file")  # make a dialog box for this
	if get_tree().change_scene("res://scenes/gameplay_scene.tscn") != OK:
		printerr("Error changing scene to gameplay")
