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
        dearpy.draw_arrow((100, 0), (100, 700), color=comp151Colors.LIGHT_GREY,
                          thickness=3)











#Boiler Plate----------------------------------------------------------
dearpy.setup_dearpygui()
dearpy.show_viewport()
dearpy.start_dearpygui()
dearpy.destroy_context()