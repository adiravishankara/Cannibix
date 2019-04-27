#!/usr/bin/python3
import tkinter as tk
from tkinter import messagebox
import sys
import datetime
from pathlib import Path
import os
import _thread
import tkinter.ttk as ttk
import RPi.GPIO as GPIO
import serial
import numpy as np
import time
import Adafruit_ADS1x15
from numpy import genfromtxt
import math
from combined_expose_collect2 import *
from combined_expose_collect2 import run_test
import combined_expose_collect1
#full_run_test()
#os.system('combined_expose_collect1.py')
#combined_expose_collect()

run_test()
