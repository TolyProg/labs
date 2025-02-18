import apackage as p

import dearpygui.dearpygui as dpg

def save_callback():
    print("Save Clicked")

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

with dpg.window(label='lab12'):
    def out(f):
        t = dpg.get_value
        if f == p.mass or f == p.report: dpg.set_value('out', f(t('a'), t('b'), t('c'), t('m')))
        else: dpg.set_value('out', f(t('a'), t('b'), t('c')))
    dpg.add_combo(p.list_shapes(), label='shape', tag='shape', callback=lambda: p.select(dpg.get_value('shape')))
    dpg.add_slider_float(label='a', tag='a')
    dpg.add_slider_float(label='b', tag='b')
    dpg.add_slider_float(label='c', tag='c')
    dpg.add_combo(p.list_materials(), tag='m')
    dpg.add_button(label='Surface', callback=lambda: out(p.selected.surface))
    dpg.add_button(label='Volume', callback=lambda: out(p.selected.volume))
    dpg.add_button(label='Mass', callback=lambda: out(p.mass))
    dpg.add_text(tag='out')
    dpg.add_button(label='Make report.docx', callback=lambda: out(p.report))

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
