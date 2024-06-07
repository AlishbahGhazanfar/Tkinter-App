#!/usr/bin/env python
# coding: utf-8

# In[7]:


import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import sqlite3
import datetime
import ftplib
from PIL import Image, ImageTk
import io

def setup_database():
    connection = sqlite3.connect('radar_app.db')
    cursor = connection.cursor()
    cursor.executescript('''
        -- Table: EventTypes
        DROP TABLE IF EXISTS EventTypes;
        CREATE TABLE EventTypes (EventType TEXT PRIMARY KEY ASC);
        INSERT INTO EventTypes (EventType) VALUES ('SelectRadar');
        INSERT INTO EventTypes (EventType) VALUES ('ViewImage');
        INSERT INTO EventTypes (EventType) VALUES ('CloseProgram');
        INSERT INTO EventTypes (EventType) VALUES ('OpenProgram');

        -- Table: Log
        DROP TABLE IF EXISTS Log;
        CREATE TABLE Log (EventType TEXT REFERENCES EventTypes (EventType), DateTime TEXT, Details TEXT);

        -- Table: Radars
        DROP TABLE IF EXISTS Radars;
        CREATE TABLE Radars (RadarId TEXT PRIMARY KEY ASC, RadarName TEXT);
        INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR011', 'Broadmeadows (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR012', 'Broadmeadows (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR013', 'Broadmeadows (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR014', 'Broadmeadows (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR021', 'Melbourne (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR022', 'Melbourne (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR023', 'Melbourne (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR024', 'Melbourne (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR031', 'Wollongong (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR032', 'Wollongong (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR033', 'Wollongong (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR034', 'Wollongong (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR041', 'Newcastle (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR042', 'Newcastle (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR043', 'Newcastle (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR044', 'Newcastle (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR051', 'Carnarvon (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR052', 'Carnarvon (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR053', 'Carnarvon (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR061', 'Geraldton (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR062', 'Geraldton (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR063', 'Geraldton (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR064', 'Geraldton (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR071', 'Wyndham (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR072', 'Wyndham (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR073', 'Wyndham (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR081', 'Gympie (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR082', 'Gympie (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR083', 'Gympie (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR084', 'Gympie (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR091', 'Gove (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR092', 'Gove (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR093', 'Gove (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR101', 'Darwin Ap (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR102', 'Darwin Ap (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR103', 'Darwin Ap (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR104', 'Darwin Ap (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR1051', 'Brisbane Ap (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR1052', 'Brisbane Ap (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR1053', 'Brisbane Ap (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR1054', 'Brisbane Ap (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR1071', 'Richmond (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR1072', 'Richmond (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR1073', 'Richmond (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR1074', 'Richmond (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR1081', 'Toowoomba (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR1082', 'Toowoomba (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR1083', 'Toowoomba (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR1084', 'Toowoomba (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR111', 'Adelaide Ap (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR1121', 'Gove Ap (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR1122', 'Gove Ap (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR1123', 'Gove Ap (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR1124', 'Gove Ap (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR112', 'Adelaide Ap (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR113', 'Adelaide Ap (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR1144', 'Carnarvon (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR114', 'Adelaide Ap (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR121', 'Kings Park (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR122', 'Kings Park (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR123', 'Kings Park (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR124', 'Kings Park (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR131', 'Sydney Ap (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR132', 'Sydney Ap (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR133', 'Sydney Ap (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR141', 'Mt Gambier (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR142', 'Mt Gambier (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR143', 'Mt Gambier (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR151', 'Dampier (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR152', 'Dampier (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR153', 'Dampier (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR154', 'Dampier (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR161', 'Port Hedland (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR162', 'Port Hedland (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR163', 'Port Hedland (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR171', 'Broome (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR172', 'Broome (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR173', 'Broome (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR174', 'Broome (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR191', 'Cairns (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR192', 'Cairns (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR193', 'Cairns (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR194', 'Cairns (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR201', 'Townsville Ap (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR202', 'Townsville Ap (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR203', 'Townsville Ap (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR204', 'Townsville Ap (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR211', 'Mt Stuart (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR212', 'Mt Stuart (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR213', 'Mt Stuart (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR214', 'Townsville (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR221', 'Mackay (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR222', 'Mackay (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR223', 'Mackay (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR224', 'Mackay (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR231', 'Gladstone (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR232', 'Gladstone (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR233', 'Gladstone (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR241', 'Bowen (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR242', 'Bowen (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR243', 'Bowen (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR251', 'Alice Springs (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR252', 'Alice Springs (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR253', 'Alice Springs (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR261', 'Perth Ap (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR262', 'Perth Ap (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR263', 'Perth Ap (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR264', 'Perth Ap (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR271', 'Woomera (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR272', 'Woomera (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR273', 'Woomera (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR281', 'Grafton (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR282', 'Grafton (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR283', 'Grafton (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR291', 'Learmonth (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR292', 'Learmonth (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR293', 'Learmonth (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR301', 'Mildura (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR302', 'Mildura (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR303', 'Mildura (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR304', 'Mildura (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR311', 'Albany (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR312', 'Albany (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR313', 'Albany (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR314', 'Albany (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR321', 'Esperance (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR322', 'Esperance (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR323', 'Esperance (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR324', 'Esperance (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR331', 'Ceduna (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR332', 'Ceduna (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR333', 'Ceduna (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR334', 'Ceduna (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR341', 'Cairns Ap (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR342', 'Cairns Ap (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR343', 'Cairns Ap (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR344', 'Cairns Ap (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR351', 'Coffs Harbour (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR352', 'Coffs Harbour (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR353', 'Coffs Harbour (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR354', 'Coffs Harbour (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR361', 'Mornington Is (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR362', 'Mornington Is (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR363', 'Mornington Is (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR371', 'Hobart (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR372', 'Hobart (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR373', 'Hobart (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR381', 'Newdegate (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR382', 'Newdegate (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR383', 'Newdegate (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR384', 'Newdegate (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR391', 'Halls Creek (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR392', 'Halls Creek (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR393', 'Halls Creek (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR401', 'Canberra (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR402', 'Canberra (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR403', 'Canberra (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR404', 'Canberra (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR411', 'Willis Is (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR412', 'Willis Is (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR413', 'Willis Is (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR421', 'Katherine (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR422', 'Katherine (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR423', 'Katherine (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR424', 'Katherine (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR431', 'Brisbane Ap (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR432', 'Brisbane Ap (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR433', 'Brisbane Ap (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR434', 'Brisbane Ap (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR441', 'Giles (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR442', 'Giles (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR443', 'Giles (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR451', 'Eucla (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR452', 'Eucla (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR453', 'Eucla (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR461', 'Sellicks Hill (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR462', 'Sellicks Hill (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR463', 'Sellicks Hill (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR471', 'Rockhampton (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR472', 'Rockhampton (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR473', 'Rockhampton (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR474', 'Rockhampton (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR481', 'Kalgoorlie (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR482', 'Kalgoorlie (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR483', 'Kalgoorlie (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR484', 'Kalgoorlie (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR491', 'Yarrawonga (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR492', 'Yarrawonga (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR493', 'Yarrawonga (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR494', 'Yarrawonga (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR501', 'Marburg (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR502', 'Marburg (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR503', 'Marburg (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR504', 'Marburg (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR511', 'Melbourne Ap (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR512', 'Melbourne Ap (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR513', 'Melbourne Ap (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR514', 'Melbourne Ap (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR521', 'NW Tasmania (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR522', 'NW Tasmania (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR523', 'NW Tasmania (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR524', 'NW Tasmania (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR531', 'Moree (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR532', 'Moree (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR533', 'Moree (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR541', 'Kurnell (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR542', 'Kurnell (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR543', 'Kurnell (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR544', 'Kurnell (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR551', 'Wagga Wagga (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR552', 'Wagga Wagga (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR553', 'Wagga Wagga (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR561', 'Longreach (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR562', 'Longreach (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR563', 'Longreach (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR571', 'East Sale (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR572', 'East Sale (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR573', 'East Sale (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR574', 'East Sale (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR581', 'South Doodlakine (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR582', 'South Doodlakine (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR583', 'South Doodlakine (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR584', 'South Doodlakine (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR592', 'Gunn Point (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR601', 'Nadi (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR602', 'Nadi (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR603', 'Nadi (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR611', 'Nausori (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR612', 'Nausori (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR613', 'Nausori (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR621', 'Norfolk Is (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR622', 'Norfolk Is (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR623', 'Norfolk Is (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR631', 'Darwin (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR632', 'Darwin (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR633', 'Darwin (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR634', 'Darwin (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR641', 'Adelaide (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR642', 'Adelaide (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR643', 'Adelaide (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR644', 'Adelaide (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR651', 'Tennant Ck (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR652', 'Tennant Ck (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR653', 'Tennant Ck (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR654', 'Tennant Ck (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR661', 'Brisbane (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR662', 'Brisbane (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR663', 'Brisbane (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR664', 'Brisbane (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR671', 'Warrego (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR672', 'Warrego (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR673', 'Warrego (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR681', 'Bairnsdale (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR682', 'Bairnsdale (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR683', 'Bairnsdale (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR684', 'Bairnsdale (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR691', 'Namoi (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR692', 'Namoi (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR693', 'Namoi (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR694', 'Namoi (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR701', 'Perth (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR702', 'Perth (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR703', 'Perth (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR704', 'Perth (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR711', 'Sydney (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR712', 'Sydney (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR713', 'Sydney (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR714', 'Sydney (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR721', 'Emerald (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR722', 'Emerald (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR723', 'Emerald (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR724', 'Emerald (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR731', 'Townsville (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR732', 'Townsville (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR733', 'Townsville (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR734', 'Townsville (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR741', 'Greenvale (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR742', 'Greenvale (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR743', 'Greenvale (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR744', 'Greenvale (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR751', 'Mt Isa (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR752', 'Mt Isa (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR753', 'Mt Isa (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR754', 'Mt Isa (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR761', 'Mt Koonya (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR762', 'Hobart Mt Koonya (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR763', 'Hobart Mt Koonya (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR764', 'Hobart Mt Koonya (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR771', 'Arafura (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR772', 'Arafura (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR773', 'Arafura (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR774', 'Arafura (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR781', 'Weipa (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR782', 'Weipa (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR783', 'Weipa (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR784', 'Weipa (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR791', 'Watheroo (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR792', 'Watheroo (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR793', 'Watheroo (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR794', 'Watheroo (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR871', 'Tindal Ap (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR872', 'Tindal Ap (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR873', 'Tindal Ap (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR874', 'Tindal Ap (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR881', 'Darwin Ap (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR882', 'Darwin Ap (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR883', 'Darwin Ap (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR884', 'Darwin Ap (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR891', 'Townsville Ap (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR892', 'Townsville Ap (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR893', 'Townsville Ap (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR894', 'Townsville Ap (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR901', 'Woomera Ap (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR902', 'Woomera Ap (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR903', 'Woomera Ap (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR904', 'Woomera Ap (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR911', 'Canberra Ap (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR912', 'Canberra Ap (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR913', 'Canberra Ap (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR914', 'Canberra Ap (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR921', 'Scherger Ap (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR922', 'Scherger Ap (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR923', 'Scherger Ap (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR924', 'Scherger Ap (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR931', 'Brewarrina (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR932', 'Brewarrina (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR933', 'Brewarrina (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR934', 'Brewarrina (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR941', 'Hillston (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR942', 'Hillston (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR943', 'Hillston (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR944', 'Hillston (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR951', 'Rainbow (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR952', 'Rainbow (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR953', 'Rainbow (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR954', 'Rainbow (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR961', 'Yeoval (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR962', 'Yeoval (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR963', 'Yeoval (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR964', 'Yeoval (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR971', 'Mildura (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR972', 'Mildura (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR973', 'Mildura (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR974', 'Mildura (64 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR981', 'Taroom (512 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR982', 'Taroom (256 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR983', 'Taroom (128 km)');
INSERT INTO Radars (RadarId, RadarName) VALUES ('IDR984', 'Taroom (64 km)');
        ''')
     # Commit changes and close the connection
    connection.commit()
    cursor.close()
    connection.close()
    
    
# Function to log events in the Log table
def log_event(event_type, details):
    conn = sqlite3.connect('radar_app.db')
    c = conn.cursor()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO Log (EventType, DateTime, Details) VALUES (?, ?, ?)", (event_type, now, details))
    conn.commit()
    conn.close()
    print(f"Log event: {event_type}, {now}, {details}")
    
# Function to fetch log records from the Log table
def fetch_log():
    conn = sqlite3.connect('radar_app.db')
    c = conn.cursor()
    c.execute("SELECT DateTime, EventType, Details FROM Log")
    records = c.fetchall()
    conn.close()
    
    if not records:
        print("fetch_log: No records found.")
    else:
        print(f"fetch_log: Retrieved {len(records)} records.")
        for record in records:
            print(record)
    
    return records

# Function to get radar stations from the Radars table
def get_radar_stations():
    conn = sqlite3.connect('radar_app.db')
    c = conn.cursor()
    c.execute("SELECT RadarName FROM Radars")
    radar_stations = [row[0] for row in c.fetchall()]
    conn.close()
    return radar_stations

# RadarApp class defining the main application window
class RadarApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RainyDaze Radar App")
        self.geometry("1200x800")
        self.create_widgets()
        self.populate_radars()
        
   # Create widgets for the application
    def create_widgets(self):
        # Radar Station List
        self.station_list_label = ttk.Label(self, text="Radar Station List")
        self.station_list_label.grid(row=0, column=0, sticky='nw')
        self.station_listbox = tk.Listbox(self, height=15, width=50)
        self.station_listbox.grid(row=1, column=0, sticky='nw', padx=5, pady=5)

        # Radar Image List
        self.image_list_label = ttk.Label(self, text="Radar Image List")
        self.image_list_label.grid(row=0, column=1, sticky='nw')
        self.image_listbox = tk.Listbox(self, height=15, width=50)
        self.image_listbox.grid(row=1, column=1, sticky='nw', padx=5, pady=5)
        self.image_listbox.bind('<<ListboxSelect>>', self.display_selected_image)

        # Image Display Area
        self.image_display_label = ttk.Label(self, text="Radar Image Display")
        self.image_display_label.grid(row=0, column=2, sticky='nw')
        self.image_display_canvas = tk.Canvas(self, width=500, height=400)
        self.image_display_canvas.grid(row=1, column=2, padx=5, pady=5)

        # Control Buttons
       

        self.test_ftp_button = ttk.Button(self, text="Fetch Radar Images", command=self.fetch_radar_images)
        self.test_ftp_button.grid(row=4, column=0, columnspan=2)
        
        self.log_button = ttk.Button(self, text="Display Event Log", command=self.display_event_log)
        self.log_button.grid(row=5, column=0, columnspan=2)
   
    # Populate the radar listbox with radar stations
    def populate_radars(self):
        conn = sqlite3.connect('radar_app.db')
        c = conn.cursor()
        c.execute("SELECT RadarId, RadarName FROM Radars")
        for radar in c.fetchall():
            self.station_listbox.insert(tk.END, f"{radar[0]} - {radar[1]}")
        conn.close()

     # Display event log in a new window    
    def display_event_log(self):
        log_window = tk.Toplevel(self)
        log_window.title("Event Log")
        
        columns = ('Event Type', 'DateTime', 'Details')
        tree = ttk.Treeview(log_window, columns=columns, show='headings')
        tree.heading('Event Type', text='Event Type')
        tree.heading('DateTime', text='DateTime')
        tree.heading('Details', text='Details')
        
        tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Generate log entries based on requirements
        radar_stations = get_radar_stations()
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for station in radar_stations:
            tree.insert('', tk.END, values=("ViewImage", now, station))

            # Fetch radar images from the FTP server
    def fetch_radar_images(self):
        try:
            with ftplib.FTP('ftp.bom.gov.au') as ftp:
                ftp.login()
                ftp.cwd('/anon/gen/radar')
                files = ftp.nlst()
                self.update_image_listbox(files)
                print("FTP Connection Successful")
        except Exception as e:
            print("FTP Connection Failed:", e)

             # Update the image listbox with files from the FTP server
    def update_image_listbox(self, files):
        self.image_listbox.delete(0, tk.END)
        for file in files:
            self.image_listbox.insert(tk.END, file)

    def display_selected_image(self, event):
        selection = self.image_listbox.curselection()
        if selection:
            filename = self.image_listbox.get(selection[0])
            self.download_and_display_image(filename)

            # Download and display the selected image
    def download_and_display_image(self, filename):
        try:
            with ftplib.FTP('ftp.bom.gov.au') as ftp, io.BytesIO() as image_binary:
                ftp.login()
                ftp.cwd('/anon/gen/radar')
                ftp.retrbinary(f'RETR {filename}', image_binary.write)
                image_binary.seek(0)
                pil_image = Image.open(image_binary)
                tk_image = ImageTk.PhotoImage(pil_image)
                self.image_display_canvas.create_image(20, 20, anchor=tk.NW, image=tk_image)
                self.image_display_canvas.image = tk_image  # Keep a reference!
                radar_station = self.station_listbox.get(tk.ACTIVE)  # Get the currently selected radar station
                details = f"Viewing image {filename} from {radar_station}"
                log_event("ViewImage", details)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to download or display image: {e}")

 # Main block to set up the database and run the application
if __name__ == "__main__":
    setup_database()
    app = RadarApp()
    app.mainloop()


# #### Explanation:
# 1.Imports: Necessary libraries are imported for the GUI, database operations, date and time handling, FTP operations, and image handling.
# 
# 2.Database Setup: The setup_database function creates tables for storing event types, logs, and radar stations. It also populates the radar stations with initial data.
# 
# 3.Logging Events: The log_event function inserts a log entry into the Log table with the event type, current date and time, and details.
# 
# 4.Fetching Logs: The fetch_log function retrieves all log entries from the Log table and prints them.
# 
# 5.Getting Radar Stations: The get_radar_stations function retrieves the names of radar stations from the Radars table.
# 
# 6.RadarApp Class: This class defines the main application window, including methods to create widgets, populate radar stations, fetch radar images, update the image list, display the selected image, and display the event log.
# 
# 7.Main Block: Sets up the database and runs the main application event loop.

# In[ ]:




