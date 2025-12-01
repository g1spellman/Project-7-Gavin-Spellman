#---------------Starter Files--------------------------
#Dearpygui
import dearpygui.dearpygui as dearpy
#Colors
import comp151Colors
#------------------------------------------------------
dearpy.create_context()
dearpy.create_viewport(title='Housing Affordability', width=900, height=900)
with dearpy.window(label='Housing Affordability', width=900, height=900):
    with dearpy.drawlist(width=900, height=900):
        #Store
        dearpy.draw_rectangle((0, 0), (900, 100),
                               color=comp151Colors.BLUE, fill=comp151Colors.BLUE)
        dearpy.draw_text((100, 25), "Walmart",
                          color=comp151Colors.YELLOW, size=15)











#Boiler Plate----------------------------------------------------------
dearpy.setup_dearpygui()
dearpy.show_viewport()
dearpy.start_dearpygui()
dearpy.destroy_context()