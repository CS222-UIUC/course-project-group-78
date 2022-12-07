extends Node2D

var audio_file = "res://audio_files/example_1.mp3"
var beatmap_file = "res://no_hold_output.csv"
var beatmap = []

var score = 0
var perfect = 0
var great = 0
var good = 0
var missed = 0
var grade = "N/A"

func set_score(new):
	score = new
	if score > 300:
		grade = "SSS"
	elif score > 200:
		grade = "SS"
	elif score > 150:
		grade = "S"
	elif score > 100:
		grade = "A"
	elif score > 70:
		grade = "B"
	elif score > 50:
		grade = "C"
	elif score > 30:
		grade = "D"
	else:
		grade = "F"


func load_csv():
	var file = File.new()
	file.open(beatmap_file, file.READ)
	var _column_names = file.get_csv_line()
	while !file.eof_reached():
		var csv = file.get_csv_line()
		if (csv.size() > 2):
			beatmap.append(csv)
	file.close()

func reset_csv():
	var file = File.new()
	file.open(beatmap_file, file.WRITE)
	file.close()
	
func _on_global_ready():
	pass
