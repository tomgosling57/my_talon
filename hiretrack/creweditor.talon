app: hiretrack
tag: user.htcreweditor
-

edit [crew] type [<user.crew_type>]:
    user.edit_crew_type(crew_type or "Text Audio-Visual")
edit [crew] quantity [<user.crew_quantity>]:
    user.edit_crew_quantity(crew_quantity or "one")
edit [crew] start:
    user.edit_crew_start()
edit [crew] end:
    user.edit_crew_end()

apply: 
    user.crew_apply()
