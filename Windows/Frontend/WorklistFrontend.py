import os
import kivy
kivy.require("1.10.1")

from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color

front_direct = r'C:\\Harddrive_Desktop\\Python\\TECAN_Worklist\\Microsoft\\Frontend'
back_direct = r'C:\\Harddrive_Desktop\\Python\\TECAN_Worklist\\Microsoft\\Backend'

class FontSize:
    def __init__(self):
        self.header_size = 32
        self.subheader_size = 25
        self.label_size = 17
        self.bttn_size = 35

class ColorFormat:
    def __init__(self):
        self.bttn_bckgrd_color = (0.11, 0.28, 0.32, 1.00)
        self.scrn_bckgrd_color = (0.00,0.50,0.50,1.00)
        self.bttn_bck_color = (0.85, 0.09, 0.05, 1.00)
        self.bttn_fwd_color = (0.29, 0.55, 0.76, 1.00)
        self.label_color = (1.00, 1.00, 1.00, 1.00)
        self.header_color = (1.00, 1.00, 1.00, 1.00)

fontsize = FontSize()
colorformat = ColorFormat()

class WorklistGenerator(GridLayout):
    def __init__(self, **kwargs):
        super(WorklistGenerator, self).__init__(**kwargs)
        #adds fixed color to kivy background - it works thank god.
        with self.canvas:
            Color(rgba = colorformat.scrn_bckgrd_color)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect,
                size=self.update_rect)

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside1 = GridLayout()
        self.inside1.cols = 1

        self.inside2 = GridLayout()
        self.inside2.cols = 1

        self.inside3 = GridLayout()
        self.inside3.cols = 1

        self.inside4 = GridLayout()
        self.inside4.cols = 1

        self.cols = 1

        self.inside1.add_widget(Label(text = ""))
        self.inside2.add_widget(Label(text = ""))
        self.inside3.add_widget(Label(text = ""))
        self.inside4.add_widget(Label(text = ""))

        self.dna_select = Button(text = "[b]DNA[/b]", markup = True, color = colorformat.bttn_fwd_color, 
        background_normal = '', 
        background_color = colorformat.bttn_bckgrd_color,
        font_size = fontsize.bttn_size)
        self.dna_select.bind(on_press = self.dna)
        self.inside.add_widget(self.dna_select)

        self.protein_select = Button(text = "[b]PROTEIN[/b]", markup = True, color = colorformat.bttn_fwd_color, 
        background_normal = '', 
        background_color = colorformat.bttn_bckgrd_color,
        font_size = fontsize.bttn_size)
        self.protein_select.bind(on_press = self.protein)
        self.inside.add_widget(self.protein_select)

        self.add_widget(self.inside1)
        self.add_widget(self.inside2)
        self.add_widget(Label(text = "[b][i]TECAN Normalization Worklist Generator[/i][/b]", markup = True, color = colorformat.header_color, font_size = fontsize.header_size))
        #self.add_widget(Label(text = "[b][u]select molecule[/u][/b]", markup = True, color = header_format.color, font_size = header_format.subheader_font_size))
        self.add_widget(self.inside3)
        self.add_widget(self.inside4)
        self.add_widget(self.inside)

    def dna(self, instance):
        if instance:
            App.get_running_app().stop()
            SeqPromptApp().run()
            reset()

    def protein(self, instance):
        if instance:
            App.get_running_app().stop()
            ProtFrontApp().run()
            reset()

    def update_rect(self, *args):
            self.rect.pos = self.pos
            self.rect.size = self.size

class SeqYes(GridLayout):
    def __init__(self, **kwargs):
        super(SeqYes, self).__init__(**kwargs)
        #adds fixed color to kivy background - it works thank god.
        with self.canvas:
            Color(rgba = colorformat.scrn_bckgrd_color)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect,
                size=self.update_rect)

        self.inside0 = GridLayout()
        self.inside0.cols = 2
        
        self.inside1 = GridLayout()
        self.inside1.cols = 2

        self.inside2 = GridLayout()
        self.inside2.cols = 2

        self.inside3 = GridLayout()
        self.inside3.cols = 2

        self.cols = 1

        self.inside0.add_widget(Label(text = "[b]Sequencing Company (Sequetech)[/b]", markup = True, 
        color = colorformat.label_color, font_size = fontsize.label_size))
        self.seqcompany = TextInput(text = "Sequetech", multiline = False, font_size = fontsize.label_size)
        self.inside0.add_widget(self.seqcompany)

        self.inside0.add_widget(Label(text = "[b]Volume DNA for Sequencing (uL)[/b]", markup = True, 
        color = colorformat.label_color, font_size = fontsize.label_size))
        self.sequencevol = TextInput(text = "10", multiline = False, font_size = fontsize.label_size)
        self.inside0.add_widget(self.sequencevol)
        
        self.inside1.add_widget(Label(text = "[b]Forward Primer Name[/b]", markup = True, 
        color = colorformat.label_color, font_size = fontsize.label_size))
        self.fwdprimer = TextInput(text = "P0074_F", multiline = False, font_size = fontsize.label_size)
        self.inside1.add_widget(self.fwdprimer)

        self.inside1.add_widget(Label(text = "[b]Reverse Primer Name[/b]", markup = True, 
        color = colorformat.label_color, font_size = fontsize.label_size))
        self.revprimer = TextInput(text = "P0075_R", multiline = False, font_size = fontsize.label_size)
        self.inside1.add_widget(self.revprimer)

        self.inside2.add_widget(Label(text = "[b]Sequence Plate Name[/b]", markup = True, 
        color = colorformat.label_color, font_size = fontsize.label_size))
        self.seqname = TextInput(text = "Sequence Plate", multiline = False, font_size = fontsize.label_size)
        self.inside2.add_widget(self.seqname)

        self.inside2.add_widget(Label(text = "[b]Sequence Plate Labware[/b]", markup = True, 
        color = colorformat.label_color, font_size = fontsize.label_size))
        self.seqtype = TextInput(text = "VWR HalfSkirt Plate", multiline = False, font_size = fontsize.label_size)
        self.inside2.add_widget(self.seqtype)

        self.back = Button(text = "[b]BACK[/b]", markup = True, color = colorformat.bttn_bck_color, 
        background_normal = '', 
        background_color = colorformat.bttn_bckgrd_color,
        font_size = fontsize.bttn_size)
        self.back.bind(on_press = self.pressed_back)
        self.inside3.add_widget(self.back)

        self.submit = Button(text = "[b]SUBMIT[/b]", markup = True, color = colorformat.bttn_fwd_color, 
        background_normal = '', 
        background_color = colorformat.bttn_bckgrd_color,
        font_size = fontsize.bttn_size)
        self.submit.bind(on_press = self.pressed)
        self.inside3.add_widget(self.submit)

        self.add_widget(self.inside0)
        self.add_widget(self.inside1)
        self.add_widget(self.inside2)
        self.add_widget(self.inside3)

    def pressed(self, instance):
        global sequence_vol #in back
        global seq_company 
        global fwd_primer
        global rev_primer
        global rack_seq #in back
        global rack_type_seq #in back
        sequence_vol = self.sequencevol.text
        seq_company = self.seqcompany.text
        fwd_primer = self.fwdprimer.text
        rev_primer = self.revprimer.text
        rack_seq = self.seqname.text
        rack_type_seq = self.seqtype.text

        if instance:
            App.get_running_app().stop()
            DNAFrontApp().run()
            reset()

    def pressed_back(self, instance):
        if instance:
            App.get_running_app().stop()
            SeqPromptApp().run()
            reset()

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class SeqPrompt(GridLayout):
    def __init__(self, **kwargs):
        super(SeqPrompt, self).__init__(**kwargs)
        #adds fixed color to kivy background - it works thank god.
        with self.canvas:
            Color(rgba = colorformat.scrn_bckgrd_color)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect,
                size=self.update_rect)

        self.inside = GridLayout()
        self.inside.cols = 3

        self.inside1 = GridLayout()
        self.inside1.cols = 1

        self.inside2 = GridLayout()
        self.inside2.cols = 1

        self.inside3 = GridLayout()
        self.inside3.cols = 1

        self.inside4 = GridLayout()
        self.inside4.cols = 1

        self.cols = 1

        self.inside1.add_widget(Label(text = ""))
        self.inside2.add_widget(Label(text = ""))
        self.inside3.add_widget(Label(text = ""))
        self.inside4.add_widget(Label(text = ""))

        self.back = Button(text = "[b]BACK[/b]", markup = True, color = colorformat.bttn_bck_color, 
        background_normal = '', 
        background_color = colorformat.bttn_bckgrd_color,
        font_size = fontsize.bttn_size)
        self.back.bind(on_press = self.pressed_back)
        self.inside.add_widget(self.back)

        self.no_seq = Button(text = "[b]NO[/b]", markup = True, color = colorformat.bttn_fwd_color, 
        background_normal = '', 
        background_color = colorformat.bttn_bckgrd_color,
        font_size = fontsize.bttn_size)
        self.no_seq.bind(on_press = self.no)
        self.inside.add_widget(self.no_seq)

        self.yes_seq = Button(text = "[b]YES[/b]", markup = True, color = colorformat.bttn_fwd_color, 
        background_normal = '', 
        background_color = colorformat.bttn_bckgrd_color,
        font_size = fontsize.bttn_size)
        self.yes_seq.bind(on_press = self.yes)
        self.inside.add_widget(self.yes_seq)

        self.add_widget(self.inside1)
        self.add_widget(self.inside2)
        self.add_widget(Label(text = "[b]Would you like to make a sequencing plate?[/b]", markup = True, color = colorformat.header_color, font_size = fontsize.header_size))
        self.add_widget(self.inside3)
        self.add_widget(self.inside4)
        self.add_widget(self.inside)

    def yes(self, instance):
        if instance:
            App.get_running_app().stop()
            SeqYesApp().run()
            reset()

    def no(self, instance):
        if instance:
            App.get_running_app().stop()
            DNAFrontApp().run()
            reset()

    def pressed_back(self, instance):
        if instance:
            App.get_running_app().stop()
            WorklistGeneratorApp().run()
            reset()

    def update_rect(self, *args):
            self.rect.pos = self.pos
            self.rect.size = self.size

class DNAFront(GridLayout):
    def __init__(self, **kwargs):
        super(DNAFront, self).__init__(**kwargs)

        #adds fixed color to kivy background - it works thank god.
        with self.canvas:
            Color(rgba = colorformat.scrn_bckgrd_color)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect,
                size=self.update_rect)

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

        self.inside6 = GridLayout()
        self.inside6.cols = 2

        self.inside0.add_widget(Label(text = "[b]TECAN DNA Elution Volume[/b]", markup = True, color = colorformat.label_color, font_size = fontsize.label_size))
        self.elutionvol = TextInput(text = "100", multiline = False, font_size = fontsize.label_size)
        self.inside0.add_widget(self.elutionvol)
        
        self.inside0.add_widget(Label(text = "[b]Dilution Type (TE or Water)[/b]", markup = True, color = colorformat.label_color, font_size = fontsize.label_size))
        self.diltype = TextInput(text = "Water", multiline = False, font_size = fontsize.label_size)
        self.inside0.add_widget(self.diltype)
        
        self.inside1.add_widget(Label(text = "[b]Source Well[/b]", markup = True, color = colorformat.label_color, font_size = fontsize.label_size))
        self.sourcewell = TextInput(text = "A1", multiline = False, font_size = fontsize.label_size)
        self.inside1.add_widget(self.sourcewell)

        self.inside1.add_widget(Label(text = "[b]Sample Source Name[/b]", markup = True, color = colorformat.label_color, font_size = fontsize.label_size))
        self.sourcename = TextInput(text = "Source Rack", multiline = False, font_size = fontsize.label_size)
        self.inside1.add_widget(self.sourcename)

        self.inside2.add_widget(Label(text = "[b]Sample Source Labware[/b]", markup = True, color = colorformat.label_color, font_size = fontsize.label_size))
        self.sourcelab = TextInput(text = "96 Well ThermoMatrixRack", multiline = False, font_size = fontsize.label_size)
        self.inside2.add_widget(self.sourcelab)

        self.inside2.add_widget(Label(text = "[b]Destination Well[/b]", markup = True, color = colorformat.label_color, font_size = fontsize.label_size))
        self.destwell = TextInput(text = "A1", multiline = False, font_size = fontsize.label_size)
        self.inside2.add_widget(self.destwell)

        self.inside3.add_widget(Label(text = "[b]Destination Name[/b]", markup = True, color = colorformat.label_color, font_size = fontsize.label_size))
        self.destname = TextInput(text = "Destination Rack", multiline = False, font_size = fontsize.label_size)
        self.inside3.add_widget(self.destname)

        self.inside3.add_widget(Label(text = "[b]Destination Labware[/b]", markup = True, color = colorformat.label_color, font_size = fontsize.label_size))
        self.destlab = TextInput(text = "96 Well ThermoMatrixRack", multiline = False, font_size = fontsize.label_size)
        self.inside3.add_widget(self.destlab)

        self.inside4.add_widget(Label(text = "[b]Diluent Source Name[/b]", markup = True, color = colorformat.label_color, font_size = fontsize.label_size))
        self.dilname = TextInput(text = "TE Diluent", multiline = False, font_size = fontsize.label_size)
        self.inside4.add_widget(self.dilname)

        self.inside4.add_widget(Label(text = "[b]Diluent Source Labware[/b]", markup = True, color = colorformat.label_color, font_size = fontsize.label_size))
        self.dilsource = TextInput(text = "Trough 100ml", multiline = False, font_size = fontsize.label_size)
        self.inside4.add_widget(self.dilsource)

        self.inside5.add_widget(Label(text = "[b]Desired Concentration (ng.uL)[/b]", markup = True, color = colorformat.label_color, font_size = fontsize.label_size))
        self.concentration = TextInput(text = "200", multiline = False, font_size = fontsize.label_size)
        self.inside5.add_widget(self.concentration)

        self.inside5.add_widget(Label(text = "[b]Desired Final Volume (uL)[/b]", markup = True, color = colorformat.label_color, font_size = fontsize.label_size))
        self.final_v = TextInput(text = "50", multiline = False, font_size = fontsize.label_size)
        self.inside5.add_widget(self.final_v)

        self.back = Button(text = "[b]BACK[/b]", markup = True, color = colorformat.bttn_bck_color, 
        background_normal = '', 
        background_color = colorformat.bttn_bckgrd_color,
        font_size = fontsize.bttn_size)
        self.back.bind(on_press = self.pressed_back)
        self.inside6.add_widget(self.back)

        self.submit = Button(text = "[b]SUBMIT[/b]", markup = True, color = colorformat.bttn_fwd_color, 
        background_normal = '', 
        background_color = colorformat.bttn_bckgrd_color,
        font_size = fontsize.bttn_size)
        self.submit.bind(on_press = self.pressed)
        self.inside6.add_widget(self.submit)

        self.add_widget(self.inside0)
        self.add_widget(self.inside1)
        self.add_widget(self.inside2)
        self.add_widget(self.inside3)
        self.add_widget(self.inside4)
        self.add_widget(self.inside5)
        self.add_widget(self.inside6)
        self.click = 0

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

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
        global final_vol
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
        final_vol = self.final_v.text

        if instance:
            self.click += 1
            if self.click > 1:
                App.get_running_app().stop()
                reset()
            else:
                try:
                    os.chdir(back_direct)
                    global sequence_vol 
                    global seq_company 
                    global fwd_primer
                    global rev_primer
                    global rack_seq 
                    global rack_type_seq 
                    type(sequence_vol)
                    del(sequence_vol)
                    exec(open("SeqDNABackend.py").read(), globals(), globals())
                except NameError:
                    os.chdir(back_direct)
                    exec(open("DNABackend.py").read(), globals(), globals())
        
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
        self.submit.text = "[b]CLOSE[/b]"
        self.back.text = "[b]HOME[/b]"

    def pressed_back(self, instance):        
        if instance:
            if self.click >= 1:
                try:
                    global sequence_vol
                    global seq_company 
                    global fwd_primer
                    global rev_primer
                    global rack_seq 
                    global rack_type_seq 
                    os.chdir(front_direct)
                    #this is a workaround to returning to main sequence prompt if no sequence was selected
                    type(sequence_vol)
                    del sequence_vol
                    App.get_running_app().stop()
                    WorklistGeneratorApp().run()
                    reset()
                except NameError:
                    os.chdir(front_direct)
                    App.get_running_app().stop()
                    WorklistGeneratorApp().run()
                    reset()
                
            else:
                try:
                    os.chdir(front_direct)
                    type(sequence_vol)
                    del sequence_vol
                    App.get_running_app().stop()
                    SeqYesApp().run()
                    reset()
                except NameError:
                    os.chdir(front_direct)
                    App.get_running_app().stop()
                    SeqPromptApp().run()
                    reset()

class ProtFront(GridLayout):
    def __init__(self, **kwargs):
        super(ProtFront, self).__init__(**kwargs)

        #adds fixed color to kivy background - it works thank god.
        with self.canvas:
            Color(rgba = colorformat.scrn_bckgrd_color)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect,
                size=self.update_rect)

        self.cols = 1
        
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

        self.inside6 = GridLayout()
        self.inside6.cols = 2
        
        self.inside1.add_widget(Label(text = "[b]Source Well[/b]", markup = True, color = colorformat.label_color, font_size = fontsize.label_size))
        self.sourcewell = TextInput(text = "A1", multiline = False, font_size = fontsize.label_size)
        self.inside1.add_widget(self.sourcewell)

        self.inside1.add_widget(Label(text = "[b]Sample Source Name[/b]", markup = True, color = colorformat.label_color, font_size = fontsize.label_size))
        self.sourcename = TextInput(text = "Source Rack", multiline = False, font_size = fontsize.label_size)
        self.inside1.add_widget(self.sourcename)

        self.inside2.add_widget(Label(text = "[b]Sample Source Labware[/b]", markup = True, color = colorformat.label_color, font_size = fontsize.label_size))
        self.sourcelab = TextInput(text = "96 Well ThermoMatrixRack", multiline = False, font_size = fontsize.label_size)
        self.inside2.add_widget(self.sourcelab)

        self.inside2.add_widget(Label(text = "[b]Destination Well[/b]", markup = True, color = colorformat.label_color, font_size = fontsize.label_size))
        self.destwell = TextInput(text = "A1", multiline = False, font_size = fontsize.label_size)
        self.inside2.add_widget(self.destwell)

        self.inside3.add_widget(Label(text = "[b]Destination Name[/b]", markup = True, color = colorformat.label_color, font_size = fontsize.label_size))
        self.destname = TextInput(text = "Destination Rack", multiline = False, font_size = fontsize.label_size)
        self.inside3.add_widget(self.destname)

        self.inside3.add_widget(Label(text = "[b]Destination Labware[/b]", markup = True, color = colorformat.label_color, font_size = fontsize.label_size))
        self.destlab = TextInput(text = "96 Well ThermoMatrixRack", multiline = False, font_size = fontsize.label_size)
        self.inside3.add_widget(self.destlab)

        self.inside4.add_widget(Label(text = "[b]Diluent Source Name[/b]", markup = True, color = colorformat.label_color, font_size = fontsize.label_size))
        self.dilname = TextInput(text = "TE Diluent", multiline = False, font_size = fontsize.label_size)
        self.inside4.add_widget(self.dilname)

        self.inside4.add_widget(Label(text = "[b]Diluent Source Labware[/b]", markup = True, color = colorformat.label_color, font_size = fontsize.label_size))
        self.dilsource = TextInput(text = "Trough 100ml", multiline = False, font_size = fontsize.label_size)
        self.inside4.add_widget(self.dilsource)

        self.inside5.add_widget(Label(text = "[b]Desired Concentration (mg.mL)[/b]", markup = True, color = colorformat.label_color, font_size = fontsize.label_size))
        self.concentration = TextInput(text = "0.20", multiline = False, font_size = fontsize.label_size)
        self.inside5.add_widget(self.concentration)

        self.inside5.add_widget(Label(text = "[b]Desired Final Volume (uL)[/b]", markup = True, color = colorformat.label_color, font_size = fontsize.label_size))
        self.final_v = TextInput(text = "50", multiline = False, font_size = fontsize.label_size)
        self.inside5.add_widget(self.final_v)

        self.back = Button(text = "[b]BACK[/b]", markup = True, color = colorformat.bttn_bck_color, 
        background_normal = '', 
        background_color = colorformat.bttn_bckgrd_color,
        font_size = fontsize.bttn_size)
        self.back.bind(on_press = self.pressed_back)
        self.inside6.add_widget(self.back)

        self.submit = Button(text = "[b]SUBMIT[/b]", markup = True, color = colorformat.bttn_fwd_color, 
        background_normal = '', 
        background_color = colorformat.bttn_bckgrd_color,
        font_size = fontsize.bttn_size)
        self.submit.bind(on_press = self.pressed)
        self.inside6.add_widget(self.submit)

        self.add_widget(self.inside1)
        self.add_widget(self.inside2)
        self.add_widget(self.inside3)
        self.add_widget(self.inside4)
        self.add_widget(self.inside5)
        self.add_widget(self.inside6)
        self.click = 0

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def pressed(self, instance):
        global rack_source
        global rack_type_source
        global rack_dest
        global rack_type_dest
        global dil_source
        global dil_type_source
        global sample_loc
        global dest_loc
        global dilution
        global final_vol
        rack_source = self.sourcename.text
        rack_type_source = self.sourcelab.text
        rack_dest = self.destname.text
        rack_type_dest = self.destlab.text
        dil_source = self.dilname.text
        dil_type_source = self.dilsource.text
        sample_loc = self.sourcewell.text
        dest_loc = self.destwell.text
        dilution = self.concentration.text
        final_vol = self.final_v.text

        if instance:
            self.click += 1
            if self.click > 1:
                App.get_running_app().stop()
                reset()
            else:
                os.chdir(back_direct)
                exec(open("ProtBackend.py").read(), globals(), globals())
        
        self.sourcename.text = ""
        self.sourcelab.text = ""
        self.destname.text = ""
        self.destlab.text = ""
        self.dilname.text = ""
        self.dilsource.text = ""
        self.sourcewell.text = "Thanks for using! Please close window."
        self.destwell.text = ""
        self.concentration.text = ""
        self.final_v.text = ""
        self.submit.text = "[b]CLOSE[/b]"
        self.back.text = "[b]HOME[/b]"

    def pressed_back(self, instance):        
        if instance:
            os.chdir(front_direct)
            App.get_running_app().stop()
            WorklistGeneratorApp().run()
            reset()

class WorklistGeneratorApp(App):
    def build(self):
        return WorklistGenerator()

class SeqYesApp(App):
    def build(self):
        return SeqYes()

class SeqPromptApp(App):
    def build(self):
        return SeqPrompt()

class DNAFrontApp(App):
    def build(self):
        return DNAFront()

class ProtFrontApp(App):
    def build(self):
        return ProtFront()

def reset():
    import kivy.core.window as window
    from kivy.base import EventLoop
    if not EventLoop.event_listeners:
        from kivy.cache import Cache
        window.Window = window.core_select_lib('window', window.window_impl, True)
        Cache.print_usage()
        for cat in Cache._categories:
            Cache._objects[cat] = {}

if __name__ == "__main__":
    WorklistGeneratorApp().run()
    reset()
