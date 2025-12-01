#---------------Starter Files--------------------------
#Dearpygui
import dearpygui.dearpygui as dearpy
#Colors
import comp151Colors
#------------------------------------------------------
dearpy.create_context()
dearpy.create_viewport(title='Get to the car!', width=900, height=1000)
with dearpy.window(label='Get to the car!', width=900, height=1000):
    with dearpy.drawlist(width=900, height=900):
        #Store
        dearpy.draw_rectangle((0, 0), (900, 100),
                               color=comp151Colors.BLUE, fill=comp151Colors.BLUE)
        dearpy.draw_text((100, 25), "Walmart",
                          color=comp151Colors.YELLOW, size=15)
        dearpy.draw_rectangle((400, 0), (500, 100),
                              color=comp151Colors.BLACK, fill=comp151Colors.WHITE)
        #Road (Truckers road)
        dearpy.draw_rectangle((0, 100), (900, 300),
                              color=comp151Colors.WHITE, fill=comp151Colors.BLACK)
        #Grass (Wildlife)
        dearpy.draw_rectangle((0, 300), (900, 500),
                              color=comp151Colors.WHITE, fill=comp151Colors.GREEN)
        #2nd Road
        dearpy.draw_rectangle((0, 500), (900, 700),
                              color=comp151Colors.WHITE, fill=comp151Colors.BLACK)
        #Parking lot
        dearpy.draw_rectangle((0, 700), (900, 900),
                              color=comp151Colors.WHITE, fill=comp151Colors.BLACK)
        #CAR PLACEHOLDER (DELETE)
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











#Boiler Plate----------------------------------------------------------
dearpy.setup_dearpygui()
dearpy.show_viewport()
dearpy.start_dearpygui()
dearpy.destroy_context()