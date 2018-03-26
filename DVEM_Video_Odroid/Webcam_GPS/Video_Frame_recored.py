import cv2
import Ensure_dir
import os
import datetime
import Write_Logfile
def videoaufzeichnung(video_wdth,video_hight,eingang,num_frames=1000,qual=90):
    """function: videoaufzeichnung
    - video_wdth: Aufloesungsbreite des Frames
    - video_hight: Aufloesungshoehe des Frames
    - eingang: ID der CAM (ID entnehmen ueber "identify_Cam.py")
    - num_frames=1000: Anzahl der Frames die die Cams erstellen
    - qual=90: die Qualitaet der Frames in abhaengigkeit der Aufloesung
    """
    #==================================
    #1.Step: Festlegung der Bildeigenschaften
    import time
    cap = cv2.VideoCapture(eingang)
    cap.set(3,video_wdth) # wdth
    cap.set(4,video_hight) #hight 
    timestamp = int(time.time()) # generiert einen Unix Timestamp. 
    time_srt=str.replace(str(time.ctime(time.time())),':','_')[:-8]+" "+str(datetime.datetime.now().year)

    #Kann mit der Funktion  datetime.datetime.utcfromtimestamp(timestamp) in normale Zeit konvertiert werden
    #==============
    #2 Step: Aendern die aktuellen Arbeitspath
    dir_path = os.path.dirname(os.path.realpath(__file__))+"/log"
    os.chdir(dir_path) #Zuerst wird die cwd auf das aktuelle File gesetzt    
    #3.Step: Erstellt einen Order zum Abspeichern der Bilder
    folder_name=time_srt+"/"+"Kamera "+str(eingang)+"_videowdth "+str(video_wdth)+"_ videohight "+str(video_hight)+time_srt
    Ensure_dir.ensure_dir(folder_name)
    os.chdir(dir_path+"/"+folder_name)
    cwd= dir_path+"/"+folder_name #Das ist der Name in der 
    #4.Step: erstelle kamera.txt mit spalten ueberschrift
    os.chdir(dir_path) 
    Write_Logfile.logfile_schreiben('"Input","Wdth","hight","Timestamp","Number","Speicherort"',str(folder_name),dir_path)
    #5.Step: Kamera benoentig etwas aufwaermzeit, daher wird While-Loop bis success= true ist
    success,image = cap.read()    
    while success==False:
        import time
        time.sleep(1)
        success,image = cap.read()    

    #6.Step: Erstellen und Abspeichern der Bilder
    print "Kamera {} laeuft".format(eingang)
    #start = time.time() #ist fuer Berechnung der Frame notwendig
    for i in range(0,num_frames):
        timestamp = time.time() #ansonsten wird die Zeit nicht aktualisiert
        success,image = cap.read()
        message= str(folder_name)+"_"+str(timestamp)+"_Nummer "+str(i)+","#DIESE ZEILE fuer windows verwenden 
        cv2.imwrite(cwd+"/"+message.split("/")[1]+".jpg", image, [int(cv2.IMWRITE_JPEG_QUALITY), qual]) #Speichert frame mit einer absoluten Addresierung
        message2= str(folder_name)+","+str(timestamp)+",Nummer"+str(i)+","+str(cwd+"/"+message+".jpg")
        os.chdir(dir_path) 
        Write_Logfile.logfile_schreiben(message2[:-1],str(folder_name),dir_path)
        i += 1
    print "Kamera "+str(eingang)+" ist fertig"
    #========================
    #7.Berechnung der fps
#    end = time.time()
#    seconds = end - start
#    fps  = num_frames / seconds;
#    #7.1.Step: Nun wird die Liste in das Log.txt geschrieben
#    os.chdir(dir_path) 
#    #7.2Step: Schreibt die berechnete fps in txt-file
#    message3= ", {0} seconds, {1} num_frames, {2} fps".format(seconds,num_frames,fps)
#    Write_Logfile.logfile_schreiben(message3,str(folder_name))
    #========================
if __name__=="__main__":
    #================
    #Test 
    #Einstellungn=[(176, 144),(320,240),(352,288),(432,240),(544,288),(640,480),(800,448),(864,480) ,(960, 544),(960, 720),(1184, 656), (1280, 960)]
    #dir_path = os.path.dirname(os.path.realpath(__file__))
    #for element in Einstellungn:
    #    videoaufzeichnung(element[0],element[1],0,dir_path)
    #================
    dir_path = os.path.dirname(os.path.realpath(__file__))
    videoaufzeichnung(176,144,0,1000,90)
    
    
    
    
