#modified 2019-04-13 to add elution vol and diluent type into the worklist
#work on making a summary .csv file fot the user to view

import os
import kivy
kivy.require("1.10.1")

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside0 = GridLayout()
        self.inside0.cols = 2
        
        self.inside1 = GridLayout()
        self.inside1.cols = 2

        self.inside2 = GridLayout()
        self.inside2.cols = 2

        self.inside3 = GridLayout()
        self.inside3.cols = 2

        self.inside4 = GridLayout()
        self.inside4.cols = 2

        self.inside5 = GridLayout()
        self.inside5.cols = 2

        self.inside0.add_widget(Label(text = "TECAN DNA Elution Volume"))
        self.elutionvol = TextInput(text = "100", multiline = False)
        self.inside0.add_widget(self.elutionvol)
        
        self.inside0.add_widget(Label(text = "Dilution Type (TE or Water)"))
        self.diltype = TextInput(text = "Water", multiline = False)
        self.inside0.add_widget(self.diltype)
        
        self.inside1.add_widget(Label(text = "Source Well"))
        self.sourcewell = TextInput(text = "A1", multiline = False)
        self.inside1.add_widget(self.sourcewell)

        self.inside1.add_widget(Label(text = "Sample Source Name"))
        self.sourcename = TextInput(text = "Source Rack", multiline = False)
        self.inside1.add_widget(self.sourcename)

        self.inside2.add_widget(Label(text = "Sample Source Labware"))
        self.sourcelab = TextInput(text = "96 Well ThermoMatrixRack", multiline = False)
        self.inside2.add_widget(self.sourcelab)

        self.inside2.add_widget(Label(text = "Destination Well"))
        self.destwell = TextInput(text = "A1", multiline = False)
        self.inside2.add_widget(self.destwell)

        self.inside3.add_widget(Label(text = "Destination Name"))
        self.destname = TextInput(text = "Destination Rack", multiline = False)
        self.inside3.add_widget(self.destname)

        self.inside3.add_widget(Label(text = "Destination Labware"))
        self.destlab = TextInput(text = "96 Well ThermoMatrixRack", multiline = False)
        self.inside3.add_widget(self.destlab)

        self.inside4.add_widget(Label(text = "Diluent Source Name"))
        self.dilname = TextInput(text = "TE Diluent", multiline = False)
        self.inside4.add_widget(self.dilname)

        self.inside4.add_widget(Label(text = "Diluent Source Labware"))
        self.dilsource = TextInput(text = "Trough 100ml", multiline = False)
        self.inside4.add_widget(self.dilsource)

        self.inside5.add_widget(Label(text = "Desired Concentration (ng.uL)"))
        self.concentration = TextInput(text = "200", multiline = False)
        self.inside5.add_widget(self.concentration)

        self.inside5.add_widget(Label(text = "Desired Final Volume (uL)"))
        self.final_v = TextInput(text = "50", multiline = False)
        self.inside5.add_widget(self.final_v)

        self.add_widget(self.inside0)
        self.add_widget(self.inside1)
        self.add_widget(self.inside2)
        self.add_widget(self.inside3)
        self.add_widget(self.inside4)
        self.add_widget(self.inside5)

        self.submit = Button(text = "Submit", font_size = 40)
        self.submit.bind(on_press = self.pressed)
        self.add_widget(self.submit)


    def pressed(self, instance):
        global elution_vol
        global dil_type
        global rack_source
        global rack_type_source
        global rack_dest
        global rack_type_dest
        global dil_source
        global dil_type_source
        global sample_loc
        global dest_loc
        global dilution
        global final_v
        elution_vol = self.elutionvol.text
        dil_type = self.diltype.text
        rack_source = self.sourcename.text
        rack_type_source = self.sourcelab.text
        rack_dest = self.destname.text
        rack_type_dest = self.destlab.text
        dil_source = self.dilname.text
        dil_type_source = self.dilsource.text
        sample_loc = self.sourcewell.text
        dest_loc = self.destwell.text
        dilution = self.concentration.text
        final_v = self.final_v.text

        if instance:
            exec(open("dna_worklist_back.py").read(), globals(), globals())
        
        self.elutionvol.text = "Thanks for using! Please close window."
        self.diltype.text = ""
        self.sourcename.text = ""
        self.sourcelab.text = ""
        self.destname.text = ""
        self.destlab.text = ""
        self.dilname.text = ""
        self.dilsource.text = ""
        self.sourcewell.text = ""
        self.destwell.text = ""
        self.concentration.text = ""
        self.final_v.text = ""
        self.submit.text = "Submit"



class Worklist_GeneratorApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    Worklist_GeneratorApp().run()