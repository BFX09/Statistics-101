from kivy.config import Config
Config.set('kivy', 'exit_on_escape', '0')
Config.set('input', 'mouse', 'mouse,disable_multitouch')
Config.set('graphics', 'minimum_width', '1070')
Config.set('graphics', 'minimum_height', '680')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.popup import Popup
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.image import Image
from StatisticsOOP import Frequency_Distribution
import math

Window.size = (1070, 680)

LabelBase.register(name='Comfortaa-Bold', fn_regular='Comfortaa-Bold.ttf')

texts = ['floors', 'fi', 'Xi', 'ri', 'Fi', 'gi', 'fi Xi', 'fi Xi²', 'fi (Xi - Xbar)³', 'fi (Xi - Xbar)⁴']


class MyW(FloatLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouse_pos)
        Window.bind(on_key_down=self._on_keyboard_down)
        Window.bind(on_key_up=self._on_keyboard_up)
        self.qtext = Button(pos_hint={'center_x': 0.155, 'center_y': 0.802}, size_hint=(0.22, 0.035),
                            background_normal='qtext.png', background_down='qtext.png',
                            border=[0, 0, 0, 0])
        self.qtext.bind(on_release=self.inpt_focus)
        self.inpt = TextInput(pos_hint={'center_x': 0.155, 'center_y': 0.802}, size_hint=(0.2, 0.035), hint_text='P:',
                              font_name='Comfortaa-Bold',
                              background_color=[1, 1, 1, 0], selection_color=[1, 0, 1, 0.3], cursor_color=[1, 0, 1, 1])
        self.inpt.write_tab = False
        self.inpt.multiline = False
        self.pop_counter = 0
        self.menu_state_value = False
        self.hover_unhover = True
        self.hover_smoother = True
        self.Tbtn = ToggleButton(group='tool', background_normal='101-menu/Table-Normal.png',
                                 background_down='101-menu/Table-Selected.png', border=[0, 0, 0, 0], size_hint=(1, 0.25),
                                 pos_hint={'center_x': 0.485, 'center_y': 0.839})
        self.Qbtn = ToggleButton(group='tool', background_normal='101-menu/Quantile-Normal.png',
                                 background_down='101-menu/Quantile-Selected.png', border=[0, 0, 0, 0], size_hint=(1, 0.25),
                                 pos_hint={'center_x': 0.485, 'center_y': 0.627})
        self.Mbtn = ToggleButton(group='tool', background_normal='101-menu/Mod-Normal.png',
                                 background_down='101-menu/Mod-Selected.png', border=[0, 0, 0, 0], size_hint=(1, 0.25),
                                 pos_hint={'center_x': 0.485, 'center_y': 0.414})
        self.Morebtn = ToggleButton(group='tool', background_normal='101-menu/More-Normal.png',
                                    background_down='101-menu/More-Selected.png', border=[0, 0, 0, 0], size_hint=(1, 0.25),
                                    pos_hint={'center_x': 0.485, 'center_y': 0.202})
        self.Tbtn.state = 'down'
        self.Tbtn.bind(on_press=self.remover_p)
        self.Mbtn.bind(on_press=self.remover_p)
        self.Morebtn.bind(on_press=self.remover_p)
        self.Qbtn.bind(on_press=self.q_select)
        self.starter_hover_smoother = True
        self.starter_unhover_smoother = True

    def start(self):
        Window.set_system_cursor('arrow')
        self.ids.bfx_btn.disabled = False
        self.ids.version.opacity = 0
        animation_start_btn = Animation(opacity=0, duration=0.08)
        animation_start_btn.start(self.ids.hoverer)
        animation_start_btn.start(self.ids.starter)
        animation_start_btn.start(self.ids.start_txt)
        animation_start = Animation(pos_hint={'center_x': 0.5, 'top': 0}, duration=0.5)
        animation_start.start(self.ids.start_background)
        animation_bfx_btn = Animation(size_hint=(0.05, 0.04), pos_hint={'center_x': 0.95, 'center_y': 0.03},
                                      duration=0.5)
        animation_bfx_btn.start(self.ids.bfx_btn)
        animation_header = Animation(pos_hint={'center_x': 0.2, 'center_y': 0.95}, duration=0.5)
        animation_header.start(self.ids.title)
        animation_header_right = Animation(size_hint=(1, 0.01), pos_hint={'center_x': 0.86, 'center_y': 0.945},
                                           duration=0.5)
        animation_header_right.start(self.ids.header_right)
        animation_header_left = Animation(size_hint=(0.06, 0.01), pos_hint={'center_x': 0.01, 'center_y': 0.945},
                                          duration=0.5)
        animation_header_left.start(self.ids.header_left)
        if self.Qbtn.state == 'down':
            self.p_adder()

    def restart(self):
        self.p_remover()
        Window.set_system_cursor('arrow')
        self.ids.bfx_btn.disabled = True
        self.ids.version.opacity = 1
        self.ids.start_txt.source = '101-StartScreen/StartText.png'
        animation_start_btn = Animation(opacity=1, duration=0.08)
        animation_start_btn.start(self.ids.starter)
        animation_start_btn.start(self.ids.start_txt)
        animation_start = Animation(pos_hint={'center_x': 0.5, 'top': 1}, duration=0.5)
        animation_start.start(self.ids.start_background)
        animation_bfx_btn = Animation(size_hint=(0.319, 0.27), pos_hint={'center_x': 0.491, 'center_y': 0.463},
                                      duration=0.5)
        animation_bfx_btn.start(self.ids.bfx_btn)
        animation_header = Animation(pos_hint={'center_x': 0.5, 'center_y': 0.95}, duration=0.5)
        animation_header.start(self.ids.title)
        animation_header_right = Animation(size_hint=(0.53, 0.01), pos_hint={'center_x': 0.93, 'center_y': 0.945},
                                           duration=0.5)
        animation_header_right.start(self.ids.header_right)
        animation_header_left = Animation(size_hint=(0.53, 0.01), pos_hint={'center_x': 0.07, 'center_y': 0.945},
                                          duration=0.5)
        animation_header_left.start(self.ids.header_left)

    def starter_hover(self):
        if self.ids.bfx_btn.disabled:
            self.ids.start_txt.source = '101-StartScreen/StartTextHover.png'
            self.starter_hover_smoother = False
            self.starter_unhover_smoother = True
            self.ids.starter.opacity = 0
            self.ids.hoverer.opacity = 1
            anime = Animation(size_hint=(0.16, 0.07), duration=0.06)
            anime.start(self.ids.hoverer)

    def starter_unhover(self):
        if self.ids.bfx_btn.disabled:
            self.ids.start_txt.source = '101-StartScreen/StartText.png'
            self.starter_hover_smoother = True
            self.starter_unhover_smoother = False
            self.ids.starter.opacity = 1
            self.ids.hoverer.opacity = 0
            anime = Animation(size_hint=(0.15, 0.06), duration=0.06)
            anime.start(self.ids.hoverer)

    def q_select(self, _):
        if self.Qbtn.state == 'down':
            self.p_adder()
        else:
            self.p_remover()

    def opener(self):
        self.ids.menu.visible = True
        self.ids.menu2.source = self.ids.menu3.source = self.ids.menu4.source = 'MenupopUp.png'
        self.ids.menu.add_widget(self.Tbtn)
        self.ids.menu.add_widget(self.Mbtn)
        self.ids.menu.add_widget(self.Qbtn)
        self.ids.menu.add_widget(self.Morebtn)
        self.on_mouse_pos(window=Window, pos=Window.mouse_pos)

    def closer(self):
        self.ids.menu.visible = False
        self.ids.menu.clear_widgets()

    def pop_counter_subtract(self, _):
        self.pop_counter -= 1
        self.on_mouse_pos(window=Window, pos=Window.mouse_pos)

    def inpt_focus(self, _):
        self.inpt.focus = True

    def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
        if not self.ids.bfx_btn.disabled:
            if not self.ids.box1.focus:
                if keycode == 40 and self.pop_counter == 0:
                    self.ids.btn.state = 'down'
                    self.selector()

                elif keycode == 41 and self.ids.menu1.state == 'down':
                    self.closer()
                    self.menu_unhover()
                    self.ids.menu1.state = 'normal'

                elif keycode == 43 and self.pop_counter == 0:
                    if self.Qbtn.state == 'down':
                        if self.ids.menu1.state == 'normal' and not self.inpt.focus:
                            self.ids.box1.focus = True
                            self.menu_unhover()
                            self.on_mouse_pos(window=Window, pos=Window.mouse_pos)
                        elif self.ids.menu1.state == 'normal' and self.inpt.focus:
                            self.opener()
                            self.ids.menu1.state = 'down'
                            self.menu_hover()
                            self.inpt.focus = False
                        elif self.ids.menu1.state == 'down' and not self.inpt.focus:
                            self.ids.box1.focus = True
                            self.closer()
                            self.ids.menu1.state = 'normal'
                            self.menu_unhover()
                            self.on_mouse_pos(window=Window, pos=Window.mouse_pos)
                    elif self.Qbtn.state != 'down':
                        if self.ids.menu1.state == 'down':
                            self.ids.box1.focus = True
                            self.closer()
                            self.ids.menu1.state = 'normal'
                            self.menu_unhover()
                            self.on_mouse_pos(window=Window, pos=Window.mouse_pos)
                        else:
                            self.ids.box1.focus = True
                            self.menu_unhover()
                            self.on_mouse_pos(window=Window, pos=Window.mouse_pos)
            elif self.ids.box1.focus:
                if keycode == 43:
                    self.ids.box1.focus = False
                    if self.Qbtn.state == 'down':
                        self.inpt.focus = True
                    elif self.Qbtn.state != 'down':
                        self.opener()
                        self.ids.menu1.state = 'down'
                        self.menu_hover()

    def _on_keyboard_up(self, instance, keyboard, keycode):
        if not self.ids.box1.focus and keycode == 40:
            self.ids.btn.state = 'normal'

    def on_touch_down(self, touch):
        super(MyW, self).on_touch_down(touch)
        if (self.inpt.collide_point(*touch.pos) or self.qtext.collide_point(
                *touch.pos)) and not self.ids.bfx_btn.disabled:
            self.qtext.background_normal = self.qtext.background_down = 'qtext.png'
            self.closer()
            self.menu_unhover()
            self.ids.menu1.state = 'normal'
        elif not self.ids.menu1.collide_point(*touch.pos) and not self.ids.menu2.collide_point(
                *touch.pos) and not self.ids.menu3.collide_point(*touch.pos) and not self.ids.menu4.collide_point(*touch.pos):
            if not self.Tbtn.collide_point(*touch.pos) and not self.Qbtn.collide_point(
                    *touch.pos) and not self.Mbtn.collide_point(*touch.pos) and not self.Morebtn.collide_point(*touch.pos) and not self.ids.bfx_btn.disabled:
                self.closer()
                self.ids.menu1.state = self.ids.menu2.state = self.ids.menu3.state = self.ids.menu4.state = 'normal'
                self.menu_state_value = False
                self.menu_unhover()
        for i in self.ids.mf.children:
            if i.collide_point(*touch.pos) and not self.ids.bfx_btn.disabled and self.ids.menu1.state == 'normal':
                b1 = TextInput(pos_hint={'center_x': 0.5, 'center_y': 0.17}, size_hint=(0.8, 0.1), text=f'{i.text}', font_size='55dp',
                               background_color=[91/255, 15/255, 104/255, 1], foreground_color=[1, 1, 1, 1], font_name='Comfortaa-Bold',
                               selection_color=[1, 0, 1, 0.4])
                b1.border = [0, 0, 0, 0]
                b1.padding_y = 30
                b1.readonly = True
                b1.font_size = '55dp'
                b1.halign = 'center'
                self.ids.floor_magnified.add_widget(b1)
        for j in self.ids.floor_magnified.children:
            if not j.collide_point(*touch.pos) and not self.ids.mf.collide_point(*touch.pos):
                self.ids.floor_magnified.clear_widgets()


    def on_mouse_pos(self, window, pos):
        if self.ids.btn.collide_point(*pos) and self.pop_counter == 0 and not self.ids.bfx_btn.disabled:
            Window.set_system_cursor('hand')
            self.ids.text_top.background_normal = self.ids.text_top.background_down = 'top.png'
            self.ids.text_border.background_normal = self.ids.text_border.background_down = 'mid.png'
            self.ids.text_bot.background_normal = self.ids.text_bot.background_down = 'bot.png'
            self.qtext.background_normal = self.qtext.background_down = 'qtext.png'

        elif not self.ids.bfx_btn.disabled and self.ids.bfx_btn.collide_point(*pos):
            Window.set_system_cursor('hand')

        elif (self.ids.box1.collide_point(*pos) or self.ids.text_border.collide_point(
                *pos) or self.ids.text_bot.collide_point(*pos) or self.ids.text_top.collide_point(*pos)) and self.pop_counter == 0 and not self.ids.bfx_btn.disabled:
            Window.set_system_cursor('ibeam')
            self.qtext.background_normal = self.qtext.background_down = 'qtext.png'
            if not self.ids.box1.focus:
                self.ids.text_top.background_normal = self.ids.text_top.background_down = 'tophover.png'
                self.ids.text_border.background_normal = self.ids.text_border.background_down = 'midhover.png'
                self.ids.text_bot.background_normal = self.ids.text_bot.background_down = 'bothover.png'

        elif (self.inpt.collide_point(*pos) or self.qtext.collide_point(*pos)) and self.pop_counter == 0 and not self.ids.bfx_btn.disabled:
            Window.set_system_cursor('ibeam')
            if not self.inpt.focus:
                self.qtext.background_normal = self.qtext.background_down = 'qtexthover.png'
            elif self.inpt.focus:
                self.qtext.background_normal = self.qtext.background_down = 'qtext.png'

        elif self.ids.menu1.collide_point(*pos) and self.pop_counter == 0 and not self.ids.bfx_btn.disabled:
            Window.set_system_cursor('hand')
            self.Tbtn.background_normal = '101-menu/Table-Normal.png'
            self.Mbtn.background_normal = '101-menu/Mod-Normal.png'
            self.Qbtn.background_normal = '101-menu/Quantile-Normal.png'
            self.Morebtn.background_normal = '101-menu/More-Normal.png'
            if self.hover_smoother:
                self.menu_hover()

        elif self.Tbtn.collide_point(*pos) and self.ids.menu.visible and not self.ids.bfx_btn.disabled:
            Window.set_system_cursor('hand')
            self.Tbtn.background_normal = '101-menu/Table-Hover.png'
            self.Mbtn.background_normal = '101-menu/Mod-Normal.png'
            self.Qbtn.background_normal = '101-menu/Quantile-Normal.png'
            self.Morebtn.background_normal = '101-menu/More-Normal.png'

        elif self.Qbtn.collide_point(*pos) and self.ids.menu.visible and not self.ids.bfx_btn.disabled:
            Window.set_system_cursor('hand')
            self.Qbtn.background_normal = '101-menu/Quantile-Hover.png'
            self.Mbtn.background_normal = '101-menu/Mod-Normal.png'
            self.Tbtn.background_normal = '101-menu/Table-Normal.png'
            self.Morebtn.background_normal = '101-menu/More-Normal.png'

        elif self.Mbtn.collide_point(*pos) and self.ids.menu.visible and not self.ids.bfx_btn.disabled:
            Window.set_system_cursor('hand')
            self.Mbtn.background_normal = '101-menu/Mod-Hover.png'
            self.Qbtn.background_normal = '101-menu/Quantile-Normal.png'
            self.Tbtn.background_normal = '101-menu/Table-Normal.png'
            self.Morebtn.background_normal = '101-menu/More-Normal.png'

        elif self.Morebtn.collide_point(*pos) and self.ids.menu.visible and not self.ids.bfx_btn.disabled:
            Window.set_system_cursor('hand')
            self.Morebtn.background_normal = '101-menu/More-Hover.png'
            self.Mbtn.background_normal = '101-menu/Mod-Normal.png'
            self.Qbtn.background_normal = '101-menu/Quantile-Normal.png'
            self.Tbtn.background_normal = '101-menu/Table-Normal.png'

        elif self.ids.starter.collide_point(*pos) and self.ids.bfx_btn.disabled:
            Window.set_system_cursor('hand')
            if self.starter_hover_smoother:
                self.starter_hover()

        else:
            Window.set_system_cursor('arrow')
            self.ids.text_top.background_normal = self.ids.text_top.background_normal = 'top.png'
            self.ids.text_border.background_normal = self.ids.text_border.background_down = 'mid.png'
            self.ids.text_bot.background_normal = self.ids.text_bot.background_down = 'bot.png'
            self.qtext.background_normal = self.qtext.background_down = 'qtext.png'
            self.Mbtn.background_normal = '101-menu/Mod-Normal.png'
            self.Qbtn.background_normal = '101-menu/Quantile-Normal.png'
            self.Morebtn.background_normal = '101-menu/More-Normal.png'
            self.Tbtn.background_normal = '101-menu/Table-Normal.png'
            if (self.ids.menu1.state == 'normal') and (not self.hover_unhover):
                self.menu_unhover()
            if self.starter_unhover_smoother:
                self.starter_unhover()
        for i in self.ids.mf.children:
            if i.collide_point(*pos) and not self.ids.bfx_btn.disabled:
                Window.set_system_cursor('hand')

    def menu_unhover(self):
        self.hover_unhover = True
        self.hover_smoother = True
        self.ids.menu2.source = self.ids.menu3.source = self.ids.menu4.source = 'Menupop.png'
        hover_animation1 = Animation(pos_hint={'center_x': 0.95, 'center_y': 0.84}, duration=0.3)
        hover_animation2 = Animation(pos_hint={'center_x': 0.95, 'center_y': 0.86}, duration=0.3)
        hover_animation1.start(self.ids.menu2)
        hover_animation2.start(self.ids.menu4)

    def menu_hover(self):
        self.hover_unhover = False
        self.hover_smoother = False
        self.ids.menu2.source = self.ids.menu3.source = self.ids.menu4.source = 'MenupopUp.png'
        hover_animation1 = Animation(pos_hint={'center_x': 0.95, 'center_y': 0.8385}, duration=0.3)
        hover_animation2 = Animation(pos_hint={'center_x': 0.95, 'center_y': 0.8615}, duration=0.3)
        hover_animation1.start(self.ids.menu2)
        hover_animation2.start(self.ids.menu4)

    def maximize(self):
        animation = Animation(size_hint=(0.18, 0.3), pos_hint={'center_x': .145, 'center_y': .717}, duration=0.2)
        border_animation = Animation(size_hint=(0.2, 0.3), pos_hint={'center_x': .1446, 'center_y': .715}, duration=0.2)
        bot_animation = Animation(size_hint=(0.2, 0.01), pos_hint={'center_x': .1446, 'center_y': .56}, duration=0.22)
        animation.start(self.ids.box1)
        border_animation.start(self.ids.text_border)
        bot_animation.start(self.ids.text_bot)

    def minimize(self):
        animation = Animation(size_hint=(0.18, 0.04), pos_hint={'center_x': .145, 'center_y': .85}, duration=0.2)
        border_animation = Animation(size_hint=(0.2, 0.03), pos_hint={'center_x': .1446, 'center_y': .85}, duration=0.2)
        bot_animation = Animation(size_hint=(0.2, 0.01), pos_hint={'center_x': .1446, 'center_y': .8309}, duration=0.2)
        animation.start(self.ids.box1)
        border_animation.start(self.ids.text_border)
        bot_animation.start(self.ids.text_bot)

    def on_focus(self, value):
        if value:
            self.ids.text_top.background_normal = self.ids.text_top.background_down = 'top.png'
            self.ids.text_border.background_normal = self.ids.text_border.background_down = 'mid.png'
            self.ids.text_bot.background_normal = self.ids.text_bot.background_down = 'bot.png'
            self.maximize()
            self.remove_widget(self.qtext)
            self.remove_widget(self.inpt)
        elif not value:
            if self.Qbtn.state == 'normal':
                self.minimize()
            else:
                self.p_adder()

    def selector(self):
        if self.Tbtn.state == self.Mbtn.state == self.Qbtn.state == self.Morebtn.state == 'normal':
            self.Tbtn.state = 'down'
            self.selector()
        elif self.Tbtn.state == 'down':
            return self.table()
        elif self.Mbtn.state == 'down':
            return self.M()
        elif self.Morebtn.state == 'down':
            return self.More()
        elif self.Qbtn.state == 'down':
            return self.Q()

    def text_validate(self, _):
        self.Q()

    def table(self):
        try:
            self.ids.mf.clear_widgets()
            self.ids.mf1.clear_widgets()
            newstr = ''.join((ch if ch in '0123456789.-e' else ' ') for ch in self.ids.box1.text)
            listOfNumbers = [float(i) for i in newstr.split()]
            f = Frequency_Distribution(listOfNumbers)
            si = ['Total', '-', '-', '-', '-', '-', str(f.sigma3), str(f.sigma4), str(f.sigma1), str(f.sigma2)]
            self.ids.mf.rows = f.k + 2
            self.ids.mf.cols = 10

            for text in texts:
                if text == 'floors':
                    self.ids.mf.add_widget(Button(text=text, color=(1, 1, 1), font_name='Comfortaa-Bold',
                                                  background_normal='topleft.png',
                                                  background_down='topleft.png', border=[0, 0, 0, 0]))
                elif text == 'fi (Xi - Xbar)⁴':
                    self.ids.mf.add_widget(Button(text=text, color=(1, 1, 1), font_name='Comfortaa-Bold',
                                                  background_normal='topright.png',
                                                  background_down='topright.png', border=[0, 0, 0, 0]))
                else:
                    self.ids.mf.add_widget(Button(text=text, color=(1, 1, 1), font_name='Comfortaa-Bold',
                                                  background_normal='hamin.png',
                                                  background_down='hamin.png', border=[0, 0, 0, 0]))
            for i in range(f.k):
                b1 = (Button(text=str(f.rows()[i]), color=(1, 1, 1), font_name='Comfortaa-Bold',
                      background_normal='hamin.png', background_down='hamin.png',
                      border=[0, 0, 0, 0]))
                b1.font_size = f'{b1.width/(f.DecimalCounter()+5)}dp'
                b1.texture_update()
                self.ids.mf.add_widget(b1)
                self.ids.mf.add_widget(Button(text=str(f.fi()[i]), color=(1, 1, 1), font_name='Comfortaa-Bold',
                                              background_normal='hamin.png', background_down='hamin.png',
                                              border=[0, 0, 0, 0]))
                self.ids.mf.add_widget(Button(text=str(f.Xi()[i]), color=(1, 1, 1), font_name='Comfortaa-Bold',
                                              background_normal='hamin.png', background_down='hamin.png',
                                              border=[0, 0, 0, 0]))
                self.ids.mf.add_widget(Button(text=str(f.ri()[i]), color=(1, 1, 1), font_name='Comfortaa-Bold',
                                              background_normal='hamin.png', background_down='hamin.png',
                                              border=[0, 0, 0, 0]))
                self.ids.mf.add_widget(Button(text=str(f.Fi()[i]), color=(1, 1, 1), font_name='Comfortaa-Bold',
                                              background_normal='hamin.png', background_down='hamin.png',
                                              border=[0, 0, 0, 0]))
                self.ids.mf.add_widget(Button(text=str(f.gi()[i]), color=(1, 1, 1), font_name='Comfortaa-Bold',
                                              background_normal='hamin.png', background_down='hamin.png',
                                              border=[0, 0, 0, 0]))
                self.ids.mf.add_widget(Button(text=str(f.fiXi()[i]), color=(1, 1, 1), font_name='Comfortaa-Bold',
                                              background_normal='hamin.png', background_down='hamin.png',
                                              border=[0, 0, 0, 0]))
                self.ids.mf.add_widget(Button(text=str(f.fiXi2()[i]), color=(1, 1, 1), font_name='Comfortaa-Bold',
                                              background_normal='hamin.png', background_down='hamin.png',
                                              border=[0, 0, 0, 0]))
                self.ids.mf.add_widget(Button(text=str(f.fiXi3()[i]), color=(1, 1, 1), font_name='Comfortaa-Bold',
                                              background_normal='hamin.png', background_down='hamin.png',
                                              border=[0, 0, 0, 0]))
                self.ids.mf.add_widget(Button(text=str(f.fiXi4()[i]), color=(1, 1, 1), font_name='Comfortaa-Bold',
                                              background_normal='hamin.png', background_down='hamin.png',
                                              border=[0, 0, 0, 0]))
            for haha in si:
                if haha == 'Total':
                    self.ids.mf.add_widget(Button(text=haha, color=(1, 1, 1), font_name='Comfortaa-Bold',
                                                  background_normal='botleft.png',
                                                  background_down='botleft.png', border=[0, 0, 0, 0]))
                elif haha == str(f.sigma2):
                    self.ids.mf.add_widget(Button(text=haha, color=(1, 1, 1), font_name='Comfortaa-Bold',
                                                  background_normal='botright.png',
                                                  background_down='botright.png', border=[0, 0, 0, 0]))
                else:
                    self.ids.mf.add_widget(Button(text=haha, color=(1, 1, 1), font_name='Comfortaa-Bold',
                                                  background_normal='hamin.png',
                                                  background_down='hamin.png', border=[0, 0, 0, 0]))

            self.minimize()
        except Exception as e:
            pop = Popup(title='Warning!',
                        content=Label(text=f"\n   Sorry Invalid Input!\n({e})",
                                      pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                      color=(1, 1, 1), font_name='Comfortaa-Bold'),
                        pos_hint={'center_x': 0.5, 'center_y': 0.5}, size_hint=(0.22, 0.15),
                        title_font='Comfortaa-bold', title_align='center')
            pop.separator_color = [1, 0, 1, 0.6]
            pop.bind(on_dismiss=self.pop_counter_subtract)
            if self.pop_counter == 0:
                pop.open()
                self.pop_counter += 1
                self.on_mouse_pos(Window, (0, 0))

    def M(self):
        try:
            self.ids.mf1.clear_widgets()
            self.ids.mf.clear_widgets()
            newstr = ''.join((ch if ch in '0123456789.-e' else ' ') for ch in self.ids.box1.text)
            listOfNumbers = [float(i) for i in newstr.split()]
            f = Frequency_Distribution(listOfNumbers)
            num = max(f.fi())
            s = round(f.x_min, f.DecimalCounter() + 1)
            y = 0.7
            for i in range(f.k):
                if i == 0:
                    a = 0
                    b = f.fi()[i + 1]
                elif i == f.k - 1:
                    a = f.fi()[i - 1]
                    b = 0
                else:
                    a = f.fi()[i - 1]
                    b = f.fi()[i + 1]
                if f.fi()[i] == num:
                    self.ids.mf1.add_widget(Image(source='hamin.png', allow_stretch=True,
                                                  keep_ratio=False,
                                                  pos_hint={'center_x': 0.17, 'center_y': y},
                                                  size_hint=(0.26, 0.1)))
                    b1 = Label(text=f'Mod = {str(s)} +', pos_hint={'center_x': 0.1, 'center_y': y}, color=(1, 1, 1),
                               font_name='Comfortaa-Bold')
                    b1.font_size = f'{b1.width/(f.DecimalCounter()+6)}dp'
                    b1.texture_update()
                    self.ids.mf1.add_widget(b1)
                    self.ids.mf1.add_widget(Label(text='(', pos_hint={'center_x': 0.142, 'center_y': y}, color=(1, 1, 1),
                                                  font_name='Comfortaa-Bold'))
                    self.ids.mf1.add_widget(
                        Image(source='101-StartScreen/HeaderLine.png',
                              pos_hint={'center_x': 0.173, 'center_y': y + 0.002},
                              size_hint=(0.055, 0.003), allow_stretch=True, keep_ratio=False))
                    numerator = Label(text=f'{f.fi()[i]} - {a}', pos_hint={'center_x': 0.173, 'center_y': y + 0.012},
                                      color=(1, 1, 1), font_name='Comfortaa-Bold')
                    numerator.font_size = f'{numerator.width/(f.DecimalCounter()+6)}dp'
                    numerator.texture_update()
                    self.ids.mf1.add_widget(numerator)
                    denominator = Label(text=f'{f.fi()[i] - a} + {f.fi()[i] - b}',
                                        pos_hint={'center_x': 0.173, 'center_y': y - 0.012}, color=(1, 1, 1),
                                        font_name='Comfortaa-Bold')
                    denominator.font_size = f'{denominator.width/(f.DecimalCounter()+6)}dp'
                    denominator.texture_update()
                    self.ids.mf1.add_widget(denominator)
                    self.ids.mf1.add_widget(Label(text=')', pos_hint={'center_x': 0.205, 'center_y': y}, color=(1, 1, 1),
                                                  font_name='Comfortaa-Bold'))
                    b2 = Label(text=f'*{f.l}  =    ', pos_hint={'center_x': 0.23, 'center_y': y}, color=(1, 1, 1),
                               font_name='Comfortaa-Bold')
                    b2.font_size = f'{b2.width/(f.DecimalCounter()+6)}dp'
                    b2.texture_update()
                    self.ids.mf1.add_widget(b2)
                    b3 = Label(text=str(
                        round(s + (f.fi()[i] - a) / ((f.fi()[i] - a) + (f.fi()[i] - b)) * f.l, f.DecimalCounter() + 2)),
                        pos_hint={'center_x': 0.265, 'center_y': y}, color=(1, 1, 1),
                        font_name='Comfortaa-Bold')
                    b3.font_size = f'{b3.width/(f.DecimalCounter()+6)}dp'
                    b3.texture_update()
                    self.ids.mf1.add_widget(b3)
                    y -= 0.15
                s = round(s + f.l, f.DecimalCounter() + 1)
                self.minimize()
        except Exception as e:
            pop = Popup(title='Warning!',
                        content=Label(text=f"\n   Sorry Invalid Input!\n({e})",
                                      pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                      color=(1, 1, 1), font_name='Comfortaa-Bold'),
                        pos_hint={'center_x': 0.5, 'center_y': 0.5}, size_hint=(0.22, 0.15),
                        title_font='Comfortaa-bold', title_align='center')
            pop.separator_color = [1, 0, 1, 0.6]
            pop.bind(on_dismiss=self.pop_counter_subtract)
            if self.pop_counter == 0:
                pop.open()
                self.pop_counter += 1
                self.on_mouse_pos(Window, (0, 0))

    def More(self):
        try:
            self.ids.mf1.clear_widgets()
            self.ids.mf.clear_widgets()
            newstr = ''.join((ch if ch in '0123456789.-e' else ' ') for ch in self.ids.box1.text)
            listOfNumbers = [float(i) for i in newstr.split()]
            f = Frequency_Distribution(listOfNumbers)
            y1 = 0.737
            y2 = 0.737
            list1 = ['Xbar', 'nXbar^2', 'Variance', 'S', 'Skewness', 'Kurt']
            list2 = ['n', 'Xmax', 'Xmin', 'R', 'l', 'k']
            list3 = [f.x_bar, round(f.n * f.x_bar ** 2, f.DecimalCounter() + 2), f.variance, f.S, f.skewness, f.kurt]
            list4 = [f.n, f.x_max, f.x_min, f.r, f.l, f.k]
            for i in range(6):
                self.ids.mf1.add_widget(
                    Button(text=f'{list2[i]} = {list4[i]}', pos_hint={'center_x': 0.3, 'center_y': y1}, color=(1, 1, 1),
                           font_name='Comfortaa-Bold', size_hint=(0.25, 0.1), background_normal='hamin.png',
                           background_down='hamin.png'))
                y1 -= 0.11
            for j in range(6):
                self.ids.mf1.add_widget(
                    Button(text=f'{list1[j]} = {list3[j]}', pos_hint={'center_x': 0.7, 'center_y': y2}, color=(1, 1, 1),
                           font_name='Comfortaa-Bold', size_hint=(0.25, 0.1), background_normal='hamin.png',
                           background_down='hamin.png'))
                y2 -= 0.11
            self.minimize()
        except Exception as e:
            pop = Popup(title='Warning!',
                        content=Label(text=f"\n   Sorry Invalid Input!\n({e})",
                                      pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                      color=(1, 1, 1), font_name='Comfortaa-Bold'),
                        pos_hint={'center_x': 0.5, 'center_y': 0.5}, size_hint=(0.22, 0.15),
                        title_font='Comfortaa-bold', title_align='center')
            pop.separator_color = [1, 0, 1, 0.6]
            pop.bind(on_dismiss=self.pop_counter_subtract)
            if self.pop_counter == 0:
                pop.open()
                self.pop_counter += 1
                self.on_mouse_pos(Window, (0, 0))

    def adder(self, _):
        self.remove_widget(self.inpt)
        self.remove_widget(self.qtext)
        self.add_widget(self.qtext)
        self.add_widget(self.inpt)

    def p_adder(self):
        self.minimize()
        Clock.schedule_once(self.adder, 0.15)

    def p_remover(self):
        self.remove_widget(self.inpt)
        self.remove_widget(self.qtext)
        self.inpt.text = ''

    def remover_p(self, _):
        self.p_remover()

    def Q(self):
        try:
            self.ids.mf1.clear_widgets()
            self.ids.mf.clear_widgets()
            newstr = ''.join((ch if ch in '0123456789.-e' else ' ') for ch in self.ids.box1.text)
            listOfNumbers = [float(i) for i in newstr.split()]
            f = Frequency_Distribution(listOfNumbers)
            pstr = ''.join((ch if ch in '0123456789.-e' else ' ') for ch in self.inpt.text)
            listOfPs = [float(j) for j in pstr.split()]
            y1 = 0.7
            y2 = 0.7
            y_pos1 = 0.7
            y_pos2 = 0.7
            first_half = 0
            second_half = 7
            for p in listOfPs[0:math.ceil(len(listOfPs) / 2)]:
                if first_half <= 6:
                    first_half += 1
                    s = round(f.x_min, f.DecimalCounter() + 1)
                    count = 0
                    self.ids.mf1.add_widget(Image(source='hamin.png', allow_stretch=True,
                                                  keep_ratio=False,
                                                  pos_hint={'center_x': 0.17, 'center_y': y_pos1},
                                                  size_hint=(0.25, 0.07)))
                    while count <= f.k:
                        if count == 0:
                            floorF = 0
                        else:
                            floorF = f.Fi()[count - 1]
                        if p * f.n <= f.Fi()[count]:
                            b1 = Label(text=f'Q{p} = {str(s)} +', pos_hint={'center_x': 0.1, 'center_y': y1},
                                       color=(1, 1, 1),
                                       font_name='Comfortaa-Bold')
                            b1.font_size = f'{b1.width/(f.DecimalCounter()+6)}dp'
                            b1.texture_update()
                            self.ids.mf1.add_widget(b1)
                            self.ids.mf1.add_widget(
                                Label(text='(', pos_hint={'center_x': 0.142, 'center_y': y1}, color=(1, 1, 1),
                                      font_name='Comfortaa-Bold'))
                            self.ids.mf1.add_widget(
                                Image(source='101-StartScreen/HeaderLine.png',
                                      pos_hint={'center_x': 0.173, 'center_y': y1 + 0.002},
                                      size_hint=(0.055, 0.003), allow_stretch=True, keep_ratio=False))
                            numerator = Label(text=f'{int(p * f.n)} - {floorF}',
                                              color=(1, 1, 1), font_name='Comfortaa-Bold',
                                              pos_hint={'center_x': 0.173, 'center_y': y1 + 0.012})
                            numerator.font_size = f'{numerator.width/(f.DecimalCounter()+6)}dp'
                            numerator.texture_update()
                            self.ids.mf1.add_widget(numerator)
                            denominator = Label(text=f'{f.fi()[count]}',
                                                color=(1, 1, 1),
                                                font_name='Comfortaa-Bold',
                                                pos_hint={'center_x': 0.173, 'center_y': y1 - 0.012})
                            denominator.font_size = f'{denominator.width/(f.DecimalCounter()+6)}dp'
                            denominator.texture_update()
                            self.ids.mf1.add_widget(denominator)
                            self.ids.mf1.add_widget(
                                Label(text=')', pos_hint={'center_x': 0.205, 'center_y': y1}, color=(1, 1, 1),
                                      font_name='Comfortaa-Bold'))
                            b2 = Label(text=f'*{f.l}  =    ', color=(1, 1, 1),
                                       font_name='Comfortaa-Bold',
                                       pos_hint={'center_x': 0.23, 'center_y': y1})
                            b2.font_size = f'{b2.width/(f.DecimalCounter()+6)}dp'
                            b2.texture_update()
                            self.ids.mf1.add_widget(b2)
                            b3 = Label(text=str(f.Quantile(p)), color=(1, 1, 1),
                                       font_name='Comfortaa-Bold',
                                       pos_hint={'center_x': 0.265, 'center_y': y1})
                            b3.font_size = f'{b3.width/(f.DecimalCounter()+6)}dp'
                            b3.texture_update()
                            self.ids.mf1.add_widget(b3)
                            break
                        s = round(s + f.l, f.DecimalCounter() + 1)
                        count += 1
                    y1 -= 0.09
                    y_pos1 -= 0.09
            for c in listOfPs[math.ceil(len(listOfPs) / 2):]:
                if second_half <= 13:
                    second_half += 1
                    s = round(f.x_min, f.DecimalCounter() + 1)
                    count = 0
                    self.ids.mf1.add_widget(Image(source='hamin.png', allow_stretch=True,
                                                  keep_ratio=False,
                                                  pos_hint={'center_x': 0.47, 'center_y': y_pos2},
                                                  size_hint=(0.25, 0.07)))
                    while count <= f.k:
                        if count == 0:
                            floorF = 0
                        else:
                            floorF = f.Fi()[count - 1]
                        if c * f.n <= f.Fi()[count]:
                            b1 = Label(text=f'Q{c} = {str(s)} +', pos_hint={'center_x': 0.4, 'center_y': y2},
                                       color=(1, 1, 1),
                                       font_name='Comfortaa-Bold')
                            b1.font_size = f'{b1.width/(f.DecimalCounter()+6)}dp'
                            b1.texture_update()
                            self.ids.mf1.add_widget(b1)
                            self.ids.mf1.add_widget(
                                Label(text='(', pos_hint={'center_x': 0.442, 'center_y': y2}, color=(1, 1, 1),
                                      font_name='Comfortaa-Bold'))
                            self.ids.mf1.add_widget(
                                Image(source='101-StartScreen/HeaderLine.png',
                                      pos_hint={'center_x': 0.473, 'center_y': y2 + 0.002},
                                      size_hint=(0.055, 0.003), allow_stretch=True, keep_ratio=False))
                            numerator = Label(text=f'{int(c * f.n)} - {floorF}',
                                              color=(1, 1, 1), font_name='Comfortaa-Bold',
                                              pos_hint={'center_x': 0.473, 'center_y': y2 + 0.012})
                            numerator.font_size = f'{numerator.width/(f.DecimalCounter()+6)}dp'
                            numerator.texture_update()
                            self.ids.mf1.add_widget(numerator)
                            denominator = Label(text=f'{f.fi()[count]}',
                                                color=(1, 1, 1),
                                                font_name='Comfortaa-Bold',
                                                pos_hint={'center_x': 0.473, 'center_y': y2 - 0.012})
                            denominator.font_size = f'{denominator.width/(f.DecimalCounter()+6)}dp'
                            denominator.texture_update()
                            self.ids.mf1.add_widget(denominator)
                            self.ids.mf1.add_widget(
                                Label(text=')', pos_hint={'center_x': 0.505, 'center_y': y2}, color=(1, 1, 1),
                                      font_name='Comfortaa-Bold'))
                            b2 = Label(text=f'*{f.l}  =    ', color=(1, 1, 1),
                                       font_name='Comfortaa-Bold',
                                       pos_hint={'center_x': 0.53, 'center_y': y2})
                            b2.font_size = f'{b2.width/(f.DecimalCounter()+6)}dp'
                            b2.texture_update()
                            self.ids.mf1.add_widget(b2)
                            b3 = Label(text=str(f.Quantile(c)), color=(1, 1, 1),
                                       font_name='Comfortaa-Bold',
                                       pos_hint={'center_x': 0.565, 'center_y': y2})
                            b3.font_size = f'{b3.width/(f.DecimalCounter()+6)}dp'
                            b3.texture_update()
                            self.ids.mf1.add_widget(b3)
                            break
                        s = round(s + f.l, f.DecimalCounter() + 1)
                        count += 1
                    y2 -= 0.09
                    y_pos2 -= 0.09
            self.minimize()
        except Exception as e:
            pop = Popup(title='Warning!',
                        content=Label(text=f"\n   Sorry Invalid Input!\n({e})",
                                      pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                      color=(1, 1, 1), font_name='Comfortaa-Bold'),
                        pos_hint={'center_x': 0.5, 'center_y': 0.5}, size_hint=(0.22, 0.15),
                        title_font='Comfortaa-bold', title_align='center')
            pop.separator_color = [1, 0, 1, 0.6]
            pop.bind(on_dismiss=self.pop_counter_subtract)
            if self.pop_counter == 0:
                pop.open()
                self.pop_counter += 1
                self.on_mouse_pos(Window, (0, 0))


class Statistics101App(App):
    def build(self):
        self.icon = 'ICON.png'
        self.title = 'Statistics-101'
        return MyW()


if __name__ == '__main__':
    Statistics101App().run()
