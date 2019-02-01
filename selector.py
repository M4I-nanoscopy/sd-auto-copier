import time , os , shutil , filecmp
import threading


class selector(threading.Thread):
    def __init__(self,callback3):
        threading.Thread.__init__(self)
        self.detect1 = False
        self.detect2 = False
        self.running = True
        self.callback = callback3
        self.i = 0


    def detector1(self,p):
        if p:
            self.detect1 = True
        else:
            self.detect1 = False

    def detector2(self,p):
        if p:
            self.detect2 = True
        else:
            self.detect2 = False
    def stop(self):
        self.running = False
        print("over")

    def run(self):
        while self.running:
            if self.detect1 and self.detect2:
                time.sleep(5)
                break
        target_dir =  "/media/telmo/"
        self.openandlist(target_dir)



    def openandlist(self,target_dir):
        liste = os.listdir(target_dir)
        path_list = []
        for file in liste:
            file_path = (os.path.join(target_dir, file))+"/"
            if os.path.isfile(file_path):
                path_list.append(file)
            elif os.path.isdir(file_path):
                if file == "test":
                    self.i +=1
                    self.copydir(file_path,file)
                path_list.append(file)
                dir_path = file_path
                self.openandlist(dir_path)
            else:
                path_list.append(file)

        self.callback(path_list)

    def copydir(self,file_path,file):
        copyfile = "/home/telmo/Desktop/"+file+str(self.i)+"/"
        shutil.copytree(file_path,copyfile)
        for file in file_path:
            match, mismatch, error = filecmp.cmpfiles(file_path,copyfile,file).append
            if len(mismatch) > 0 or len(error) > 0:
                print("Erreur original files and copied files are different")

            time.sleep(0.5)

        print("copy over")