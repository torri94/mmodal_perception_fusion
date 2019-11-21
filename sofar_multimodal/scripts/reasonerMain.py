#!/usr/bin/env python

#Author: Baldassarre Nicolo', Panzera Matteo, Rusconi Andrea

import rospy
from os import system
from std_msgs.msg import String
from sofar_multimodal.msg import *

# Funzione invocata all'arrivo dei messaggi dal Correlation Table Manager
def callback(data):
    # Inizializzo l'array dei records (che corrispondono ai vari confronti)
    records = []

    # Ricevo i dati e costruisco i records
    for i in range(len(data.table)):
        record_line = []
        record_line.append(data.table[i].first_percepted_object)
        record_line.append(data.table[i].second_percepted_object)
        record_line.append(data.table[i].correlation)
        records.append(record_line)

    # Inizializzo l'array che conterra' tutti gli oggetti percepiti presenti sulla scena
    objects = []

    i = 0
    # Controllo per righe (prima colonna dell'array)
    while i < len(records):
        if not objects.__contains__(records[i][0]):
            objects.append(records[i][0])
        j=i+1
        while j < len(records):
            if records[i][0]==records[j][0]:
                corrI= list(records[i][1])
                corrJ = list(records[j][1])
                if len(set(corrI[0]) & set(corrJ[0])) > 0 : 
                    if records[i][2]>records[j][2]:
                        records.remove(records[j])
                        j -= 1
                    else:
                        records.remove(records[i])
                        j = len(records)
                        i-= 1
            j+=1
        i+=1

    # Controllo per colonne (seconda colonna dell'array)
    i=0
    while i < len(records):
        if not objects.__contains__(records[i][1]):
            objects.append(records[i][1])
        j=i+1
        while j < len(records):
            if records[i][1]==records[j][1]:
                corrI = list(records[i][0])
                corrJ = list(records[j][0])
                if len(set(corrI[0]) & set(corrJ[0]))>0 : 
                    if records[i][2]>records[j][2]:
                        records.remove(records[j])   
                        j -= 1 
                    else: 
                        records.remove(records[i])
                        j = len(records)
                        i -= 1
            j += 1
        i += 1
          
    # Calcolo correlazione minima
    i = 0
    while i < len(records):
        correlations = []
        correlations.append(records[i][2])
        records[i].remove(records[i][2])
        j=i+1
        while j < len(records):
            if len(set(records[i]) & set(records[j])) > 0: 
                correlations.append(records[j][2])
                records[j].remove(records[j][2])
                records[i]= list(set(records[i])|set(records[j]))
                records.remove(records[j])
                j -= 1
            j += 1 
        min = 2 
        for k in range(len(correlations)):
            if correlations[k]< min : 
                min = correlations[k]
        records[i].append(min)
        i+=1
    
    # GESTIONE ECCEZIONI
    # Eccezione 1: in una collezione e' presente piu' di un oggetto rilevato dallo stesso modulo percettivo
    i = 0
    for i in range(len(records)):
        j = 0
        intersection = []
        for j in range(len(records[i])-1):
            if not intersection.__contains__(records[i][j][0]):
                intersection.append(records[i][j][0])
            else:
                rospy.logerr("Errore: due oggetti del modulo percettivo " + records[i][j][0] + " sembrano essere correlati")
    
    # Eccezione 2: aggiunta degli oggetti riconosciuti in piu' da un solo modulo percettivo ma non correlati a nessun altro oggetto
    i = 0
    for i in range(len(records)):
        for j in range(len(records[i])-1):
            if objects.__contains__(records[i][j]):
                objects.remove(records[i][j])
    for i in range(len(objects)):
        listObject = []
        listObject.append(objects[i])
        listObject.append(0.0)
        records.append(listObject)
    # Costruzione del messaggio in output
    output = outputReasoner()
    output.lines = []
    i = 0
    for i in range(len(records)):
        j = 0
        record_line = record()
        record_line.rec = []
        for j in range(len(records[i])-1):
            record_line.rec.append(str(records[i][j]))
        record_line.corr = records[i][len(records[i])-1]
        output.lines.append(record_line)
    pub = rospy.Publisher('reasoner_output', outputReasoner, queue_size=10)     # Il talker pubblica sul topic reasoner_output
    pub.publish(output)


# Listener che ascolta i messaggi pubblicati dal Correlation Table Manager sul topic correlationTables
def listener():
        rospy.init_node('reasonerMain', anonymous=True)
        rospy.Subscriber('correlationTables', correlationTable, callback)
        rospy.Publisher
        rospy.spin()

# Chiamata al listener
if __name__ == '__main__':
    system("clear")
    listener()
