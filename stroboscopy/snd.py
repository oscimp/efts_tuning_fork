#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: jmfriedt
# GNU Radio version: 3.10.12.0

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import analog
from gnuradio import audio
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import threading



class snd(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "snd")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)
        self.flowgraph_started = threading.Event()

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 96000
        self.f = f = 32768
        self.df = df = 1
        self.Level = Level = 0.3

        ##################################################
        # Blocks
        ##################################################

        self._f_range = qtgui.Range(0, samp_rate/2, .0005, 32768, 200)
        self._f_win = qtgui.RangeWidget(self._f_range, self.set_f, "'f'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._f_win)
        self._df_range = qtgui.Range(0, 10, 1, 1, 200)
        self._df_win = qtgui.RangeWidget(self._df_range, self.set_df, "'df'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._df_win)
        self.audio_sink_0 = audio.sink(samp_rate, 'hw:CARD=Audio,DEV=0', True)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, f, .9, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, (f+df), 0.9, 0, 0)
        self._Level_range = qtgui.Range(0, 0.6, 0.05, 0.3, 200)
        self._Level_win = qtgui.RangeWidget(self._Level_range, self.set_Level, "'Level'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Level_win)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.audio_sink_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.audio_sink_0, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "snd")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)

    def get_f(self):
        return self.f

    def set_f(self, f):
        self.f = f
        self.analog_sig_source_x_0.set_frequency((self.f+self.df))
        self.analog_sig_source_x_0_0.set_frequency(self.f)

    def get_df(self):
        return self.df

    def set_df(self, df):
        self.df = df
        self.analog_sig_source_x_0.set_frequency((self.f+self.df))

    def get_Level(self):
        return self.Level

    def set_Level(self, Level):
        self.Level = Level




def main(top_block_cls=snd, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()
    tb.flowgraph_started.set()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
