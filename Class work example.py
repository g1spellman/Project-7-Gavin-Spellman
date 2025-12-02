import dearpygui.dearpygui as dearpy
import comp151Colors

boy_x=100
boy_y=300
boy_speed=3
boy_w, boy_h, channels, ship_file_pict= dearpy.load_image("ship.png")
gold_w, gold_h, channels, gold_file_pict= dearpy.load_image("gold-pile.png")
def move_ship(sender, app_data):
    key=app_data
    global boy_x, boy_y, boy_speed, boy_h, boy_w
    if key == dearpy.mvKey_Left:
        ship_x -= ship_speed
    elif key == dearpy.mvKey_Right:
        ship_x += ship_speed
    elif key == dearpy.mvKey_Up:
        ship_y -= ship_speed
    elif key == dearpy.mvKey_Down:
        ship_y += ship_speed
    with dearpy.mutex():
        dearpy.configure_item("ship_update", pmin= (ship_x, ship_y), pmax= (ship_x+ship_w, ship_y+ship_h))

dearpy.create_context()
with dearpy.texture_registry():
    dearpy.add_static_texture(boy_w, boy_h, ship_file_pict, tag="ship_pict")
    dearpy.add_static_texture(gold_w, gold_h, gold_file_pict, tag="gold_pict")
with dearpy.handler_registry():
    dearpy.add_key_press_handler(callback=move_ship)
dearpy.create_viewport(title="image demo", width=800, height=800)
with dearpy.window(label="image demo", width=800, height=800):
    with dearpy.drawlist(width=800, height=800):
        dearpy.draw_rectangle((0,0), (800,800),
                          fill=comp151Colors.BLUE)
        dearpy.draw_image("ship_pict", (boy_x, boy_y),
                          (boy_x + boy_w * 2, boy_y + boy_h * 2), tag="ship_update")


dearpy.setup_dearpygui()
dearpy.show_viewport()
while dearpy.is_dearpygui_running():
    # ship_x+= ship_speed
    # if ship_x>=800 or ship_x <=0:
    #     ship_speed=-ship_speed
    # dearpy.configure_item("ship_update", pmin=(ship_x, ship_y), pmax=(ship_x+ship_w, ship_y+ship_h))
    dearpy.render_dearpygui_frame()
dearpy.start_dearpygui()