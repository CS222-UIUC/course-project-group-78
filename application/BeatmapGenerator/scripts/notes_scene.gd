extends Area2D

const TARGET_Y = 500
const SPAWN_Y = -30
const DIST_TO_TARGET = TARGET_Y - SPAWN_Y

const LEFT_LANE_SPAWN = Vector2(152, SPAWN_Y)
const UP_LANE_SPAWN = Vector2(246, SPAWN_Y)
const DOWN_LANE_SPAWN = Vector2(342, SPAWN_Y)
const RIGHT_LANE_SPAWN = Vector2(439, SPAWN_Y)

var speed = 0
var hit = false

func _ready():
	pass

func _physics_process(delta):
	if !hit:
		position.y += speed * delta
		if position.y > 600:
			queue_free()
	else:
		$Node2D.position.y -= speed * delta


func initialize(lane):
	if lane == 0:
		$arrow.frame = 0
		position = LEFT_LANE_SPAWN
	elif lane == 1:
		$arrow.frame = 1
		position = UP_LANE_SPAWN
	elif lane == 2:
		$arrow.frame = 2
		position = DOWN_LANE_SPAWN
	elif lane == 3:
		$arrow.frame = 3
		position = RIGHT_LANE_SPAWN
	else:
		printerr("Invalid lane set for note: " + str(lane))
		return
	
	speed = DIST_TO_TARGET / 2.0


func destroy(score):
	$arrow.visible = false
	$timer.start()
	hit = true
	if score == 3:
		$Node2D/note_hit.text = "PERFECT!"
		$Node2D/note_hit.modulate = Color("f6d6bd")
	elif score == 2:
		$Node2D/note_hit.text = "GREAT"
		$Node2D/note_hit.modulate = Color("c3a38a")
	elif score == 1:
		$Node2D/note_hit.text = "GOOD"
		$Node2D/note_hit.modulate = Color("997577")


func _on_timer_timeout():
	queue_free()
