#---------------Starter Files--------------------------
#Dearpygui
import dearpygui.dearpygui as dearpy
#Colors
import comp151Colors
#--------Overlap Checker--------------------------------
def do_overlap(l1, r1, l2, r2):
    # If one rectangle is to the left of the other
    if l1.get('x') > r2.get('x') or l2.get('x') > r1.get('x'):
        return False

    # If one rectangle is above the other
    if r1.get('y') < l2.get('y') or r2.get('y') < l1.get('y'):
        return False
    return True
#----------------Player Character-----------------------
boy_x=400
boy_y=0
boy_speed=7
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
#--------Truck 1-------------------------
truck_x=0
truck_y=100
truck_speed=7
truck_w, truck_h, channels, truck_file_pict= dearpy.load_image("dumper_1_2.png")
#---------Truck 2----------------------------------
truck2_x=0
truck2_y=200
truck2_speed=7
truck2_w, truck2_h, channels, truck2_file_pict= dearpy.load_image("dumper_1_2.png")

#--------Truck 3----------------------------------
truck3_x=300
truck3_y=200
truck3_speed=7
truck3_w, truck3_h, channels, truck3_file_pict= dearpy.load_image("dumper_1_2.png")
#-------Dog----------------------------------------
dog_x=0
dog_y=300
dog_speed=7
dog_w, dog_h, channels, dog_file_pict= dearpy.load_image("dog2.png")
#------Dog 2----------------------------------------
dog2_x=300
dog2_y=300
dog2_speed=7
dog2_w, dog2_h, channels, dog2_file_pict= dearpy.load_image("dog2.png")
#-----Bear-------------------------------------------
bear_x=0
bear_y=400
bear_speed=7
bear_w, bear_h, channels, bear_file_pict= dearpy.load_image("bear.png")
#----Car----------------------------------------------
car_x=300
car_y=500
car_speed=7
car_w, car_h, channels, car_file_pict= dearpy.load_image("firebrigade_1_2.png")
#-----Car2--------------------------------------------
car2_x=500
car2_y=500
car2_speed=7
car2_w, car2_h, channels, car2_file_pict= dearpy.load_image("firebrigade_1_2.png")
#-----Car3--------------------------------------------
car3_x=700
car3_y=500
car3_speed=7
car3_w, car3_h, channels, car3_file_pict= dearpy.load_image("firebrigade_1_2.png")
#-----Van---------------------------------------------
van_x=0
van_y=600
van_speed=0
van_w, van_h, channels, van_file_pict= dearpy.load_image("van1.png")
#-------Work Area--------------------------------------
dearpy.create_context()
#Texture Loadout (add each time)
with dearpy.texture_registry():
    dearpy.add_static_texture(boy_w, boy_h, boy1_file_pict, tag="boy1_pict")
    dearpy.add_static_texture(truck_w, truck_h, truck_file_pict, tag="truck_pict")
    dearpy.add_static_texture(truck2_w, truck2_h, truck2_file_pict, tag="truck2_pict")
    dearpy.add_static_texture(truck3_w, truck3_h, truck3_file_pict, tag="truck3_pict")
    dearpy.add_static_texture(dog_w, dog_h, dog_file_pict, tag="dog_pict")
    dearpy.add_static_texture(dog2_w, dog2_h, dog2_file_pict, tag="dog2_pict")
    dearpy.add_static_texture(bear_w, bear_h, bear_file_pict, tag="bear_pict")
    dearpy.add_static_texture(car_w, car_h, car_file_pict, tag="car_pict")
    dearpy.add_static_texture(car2_w, car2_h, car2_file_pict, tag="car2_pict")
    dearpy.add_static_texture(car2_w, car2_h, car2_file_pict, tag="car3_pict")
    dearpy.add_static_texture(van_w, van_h, van_file_pict, tag="van_pict")
#------------------------------------------------
with dearpy.handler_registry():
    dearpy.add_key_press_handler(callback=move_boy)
dearpy.create_viewport(title='Get to the Car!', width=900, height=1000)
with dearpy.window(label='Get to the Car!', width=900, height=1000):
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
        dearpy.draw_rectangle((0, 600), (900, 900),
                          color=comp151Colors.WHITE, fill=comp151Colors.BLACK)
        dearpy.draw_line((100, 600), (100, 900),
                         color=comp151Colors.WHITE)
        dearpy.draw_line((200, 600), (200, 900),
                         color=comp151Colors.WHITE)
        dearpy.draw_line((300, 600), (300, 900),
                         color=comp151Colors.WHITE)
        dearpy.draw_line((400, 600), (400, 900),
                         color=comp151Colors.WHITE)
        dearpy.draw_line((500, 600), (500, 900),
                         color=comp151Colors.WHITE)
        dearpy.draw_line((600, 600), (600, 900),
                         color=comp151Colors.WHITE)
        dearpy.draw_line((700, 600), (700, 900),
                         color=comp151Colors.WHITE)
        dearpy.draw_line((800, 600), (800, 900),
                         color=comp151Colors.WHITE)
#-------------CHARACTERS--------------------------------------------------------
        #Boy
        dearpy.draw_image("boy1_pict", (boy_x, boy_y),
                          (boy_x + boy_w+100, boy_y + boy_h+100), tag="boy_update")
        #Truck 1
        dearpy.draw_image("truck_pict", (truck_x, truck_y),
                          (truck_x + truck_w+100, truck_y + truck_h+100), tag="truck_update")
        #Truck 2
        dearpy.draw_image("truck_pict", (truck2_x, truck2_y),
                          (truck2_x + truck_w+100, truck2_y + truck2_h+100), tag="truck2_update")
        #Truck 3
        dearpy.draw_image("truck_pict", (truck3_x, truck3_y),
                          (truck3_x + truck3_w + 100, truck3_y + truck3_h + 100), tag="truck3_update")
        #Dog
        dearpy.draw_image("dog_pict", (dog_x, dog_y),
                          (dog_x + dog_w+100, dog_y + dog_h+100), tag="dog_update")
        #Dog 2
        dearpy.draw_image("dog2_pict", (dog2_x, dog2_y),
                          (dog2_x + dog2_w+100, dog2_y + dog2_h+100), tag="dog2_update")
        #Bear
        dearpy.draw_image("bear_pict", (bear_x, bear_y),
                          (bear_x+bear_w+100, bear_y + bear_h+100), tag="bear_update")
        #Car
        dearpy.draw_image("car_pict", (car_x, car_y),
                          (car_x+car_w+100, car_y + car_h+100), tag="car_update")
        #Car 2
        dearpy.draw_image("car2_pict", (car2_x, car2_y),
                          (car2_x+car2_w+100, car2_y + car2_h+100), tag="car2_update")
        #Car 3
        dearpy.draw_image("car3_pict", (car3_x, car3_y),
                          (car3_x+car3_w+100, car3_y + car3_h+100), tag="car3_update")
        #Van
        dearpy.draw_image("van_pict", (van_x, van_y),
                          (van_x+van_w+100, van_y + van_h+200), tag="van_update")
#Boiler Plate----------------------------------------------------------
dearpy.setup_dearpygui()
dearpy.show_viewport()
#Movement
while dearpy.is_dearpygui_running():
    #Truck 1
    truck_x+= truck_speed
    if truck_x>=900:
         truck_x=-truck_w
    dearpy.configure_item("truck_update", pmin=(truck_x, truck_y), pmax=(truck_x+truck_w, truck_y+truck_h))
    #Truck 2
    truck2_x += truck2_speed
    if truck2_x >= 900:
        truck2_x = -truck2_w
    dearpy.configure_item("truck2_update", pmin=(truck2_x, truck2_y), pmax=(truck2_x + truck2_w, truck2_y + truck2_h))
    #Truck 3
    truck3_x += truck3_speed
    if truck3_x >= 900:
        truck3_x = -truck3_w
    dearpy.configure_item("truck3_update", pmin=(truck3_x, truck3_y), pmax=(truck3_x + truck3_w, truck3_y + truck3_h))
    #Dog
    dog_x += dog_speed
    if dog_x >= 900 or dog_x <= 0:
        dog_speed=-dog_speed
    dearpy.configure_item("dog_update", pmin=(dog_x, dog_y), pmax=(dog_x+dog_w+50, dog_y+dog_h+50))
    #Dog 2
    dog2_x += dog2_speed
    if dog2_x >= 900 or dog2_x <= 0:
        dog2_speed = -dog2_speed
    dearpy.configure_item("dog2_update", pmin=(dog2_x, dog2_y), pmax=(dog2_x + dog2_w+50, dog2_y + dog2_h+50))
    #Bear
    bear_x += bear_speed
    if bear_x >= 900 or bear_x <= 0:
        bear_speed = -bear_speed
    dearpy.configure_item("bear_update", pmin=(bear_x, bear_y), pmax=(bear_x + bear_w, bear_y + bear_h))
    #Car
    car_x -= car_speed
    if car_x < -car_w:
        car_x = 900 + car_w
    dearpy.configure_item("car_update", pmin=(car_x, car_y), pmax=(car_x + car_w, car_y + car_h))
    #Car 2
    car2_x -= car2_speed
    if car2_x < -car2_w:
        car2_x = 900 +car2_w
    dearpy.configure_item("car2_update", pmin=(car2_x, car2_y), pmax=(car2_x + car2_w, car2_y + car2_h))
    #Car 3
    car3_x -= car3_speed
    if car3_x < -car3_w:
        car3_x = 900+ car3_w
    dearpy.configure_item("car3_update", pmin=(car3_x, car3_y), pmax=(car3_x + car3_w, car3_y + car3_h))
    #Van (not moving but movement makes it normal-sized)
    van_x += van_speed
    if van_x >= 900 or van_x <= 0:
        van_speed = -van_speed
    dearpy.configure_item("van_update", pmin=(van_x, van_y), pmax=(van_x + 100, van_y + 200))

#Additional Boiler Plate
    dearpy.render_dearpygui_frame()
dearpy.start_dearpygui()