#---------------Starter Files--------------------------
#Dearpygui
import dearpygui.dearpygui as dearpy
#Colors
import comp151Colors
#----------------Player Character-----------------------
boy_x=400
boy_y=0
boy_speed=5
boy_w, boy_h, channels, boy1_file_pict= dearpy.load_image("boy1.png")
def move_boy(sender, app_data):
    key=app_data
    global boy_x, boy_y, boy_speed, boy_h, boy_w
    if key == dearpy.mvKey_Left:
        boy_x -= boy_speed
    elif key == dearpy.mvKey_Right:
        boy_x += boy_speed
    elif key == dearpy.mvKey_Up:
        boy_y -= boy_speed
    elif key == dearpy.mvKey_Down:
        boy_y += boy_speed
    with dearpy.mutex():
        dearpy.configure_item("boy_update", pmin= (boy_x, boy_y), pmax= (boy_x + 100, boy_y + 100))
#--------Trucks Near Store-------------------------
truck_x=400
truck_y=0
truck_speed=5
truck_w, truck_h, channels, truck_file_pict= dearpy.load_image("dumper_1_2.png")
def move_truck(sender, app_data):


#---------------------------------------------------
dearpy.create_context()
with dearpy.texture_registry():
    dearpy.add_static_texture(boy_w, boy_h, boy1_file_pict, tag="boy1_pict")
with dearpy.handler_registry():
    dearpy.add_key_press_handler(callback=move_boy)
dearpy.create_viewport(title='Get to the car!', width=900, height=1000)
with dearpy.window(label='Get to the car!', width=900, height=1000):
    with dearpy.drawlist(width=900, height=900):
#-----------BACKGROUND ELEMENTS-------------------------------------------
        # Store
        dearpy.draw_rectangle((0, 0), (900, 100),
                              color=comp151Colors.BLUE, fill=comp151Colors.BLUE)
        dearpy.draw_text((100, 25), "Walmart",
                              color=comp151Colors.YELLOW, size=15)
        dearpy.draw_rectangle((400, 0), (500, 100),
                              color=comp151Colors.BLACK, fill=comp151Colors.WHITE)
        # Road (Truckers road)
        dearpy.draw_rectangle((0, 100), (900, 300),
                              color=comp151Colors.WHITE, fill=comp151Colors.BLACK)
        # Grass (Wildlife)
        dearpy.draw_rectangle((0, 300), (900, 500),
                              color=comp151Colors.WHITE, fill=comp151Colors.GREEN)
        # 2nd Road
        dearpy.draw_rectangle((0, 500), (900, 700),
                              color=comp151Colors.WHITE, fill=comp151Colors.BLACK)
        # Parking lot
        dearpy.draw_rectangle((0, 700), (900, 900),
                              color=comp151Colors.WHITE, fill=comp151Colors.BLACK)
        # CAR PLACEHOLDER (DELETE)
        dearpy.draw_rectangle((400, 700), (500, 900),
                              color=comp151Colors.BLACK, fill=comp151Colors.RED)
        dearpy.draw_line((100, 700), (100, 900),
                         color=comp151Colors.WHITE)
        dearpy.draw_line((200, 700), (200, 900),
                         color=comp151Colors.WHITE)
        dearpy.draw_line((300, 700), (300, 900),
                         color=comp151Colors.WHITE)
        dearpy.draw_line((400, 700), (400, 900),
                         color=comp151Colors.WHITE)
        dearpy.draw_line((500, 700), (500, 900),
                         color=comp151Colors.WHITE)
        dearpy.draw_line((600, 700), (600, 900),
                         color=comp151Colors.WHITE)
        dearpy.draw_line((700, 700), (700, 900),
                         color=comp151Colors.WHITE)
        dearpy.draw_line((800, 700), (800, 900),
                         color=comp151Colors.WHITE)
#-------------CHARACTERS--------------------------------------------------------
        #Boy
        dearpy.draw_image("boy1_pict", (boy_x, boy_y),
                          (boy_x + boy_w+100, boy_y + boy_h+100), tag="boy_update")












#Boiler Plate----------------------------------------------------------
dearpy.setup_dearpygui()
dearpy.show_viewport()
dearpy.start_dearpygui()
dearpy.destroy_context()