import  os
from synthesistool import connect
import time
class Synthesis_model():
    def __init__(self,file_paths,result_root_path,syn_type):
        self.file_paths=file_paths
        self.result_root_path=result_root_path
        self.syn_type=syn_type


    def get_synthesis_result(self):
        syn_result=""
        for file_path in self.file_paths:
            file_name=os.path.basename(file_path).split('.')[0]
            file_content=open(file_path,encoding='utf-8').read()
            result=self.synthesis_use_netease(file_name,file_content)
            if result=="1":
                syn_result=syn_result+file_path+" ok !\n"
            else:
                syn_result=syn_result+file_path+result
        return syn_result


    def synthesis_use_netease(self,file_name,text):
        result=connect(text,'zh-CHS')
        print(result)
        if result.headers['Content-Type']=="audio/mp3":
            millis = int(round(time.time() * 1000))
            filePath = "./result/" + file_name+"-"+str(millis) + ".mp3"
            fo = open(filePath, 'wb')
            fo.write(result.content)
            fo.close()
            return "1"
        else:
            return "error:"+result.content