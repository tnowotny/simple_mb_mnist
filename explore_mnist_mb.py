import mnist_mb
import time
from mnist_mb_para import para

#para["RECORD_PN_SPIKES"]= True
#para["RECORD_KC_SPIKES"]= True
#para["RECORD_GGN_SPIKES"]= True
para["rho"]= 0.01
#para["plot"]= True
para["NUM_STIM"]= 100
today= time.strftime("%Y%m%d")

for NKC in [20000 ]:
    para["NUM_KC"] = NKC
    for nKC in [200]: #[ 20, 50, 100, 200, 500, 1000 ]: 
        para["num_KC"]= nKC
        for wMax in [1]: #[ 5, 10, 20 ]:
            para["wMax"]= 0.023316192520205694 #wMax*(1.0/(0.44324564+1.07*nKC))
            for eta in [1]: #[ 0.00005, 0.0001, 0.0002]:
                para["eta"]= 2.03718224620342e-05 #eta*(1.0/(0.44324564+1.07*nKC))/0.04578126
                for repeat in range(100):
                    para["TRAIN"]= True
                    para["input_range"]= range(50000)
                    para["RECORD_MBON_SPIKES"]= False
                    para["basename"]= today+"-NKC{}-nKC{}-wMax{}-eta{}-rep{}".format(para["NUM_KC"],para["num_KC"],para["wMax"],para["eta"],2)
                    para["SHUFFLE"]= True
                    para["NUM_STIM"]= 2000
                    g= mnist_mb.run_mb(para)
                    para["TRAIN"]= False
                    para["inputs"]= "training"
                    para["input_range"]= range(50000,60000)
                    para["SHUFFLE"]= False
                    para["write_progress"]= open("eval_progress.dat","a")
                    mnist_mb.run_mb(para,g)
                para["TRAIN"]= False
                para["inputs"]= "testing"
                para["RECORD_MBON_SPIKES"]= True
                para["SHUFFLE"]= False
                para["write_progress"]= open("test_progress.dat","a")
                mnist_mb.run_mb(para,g)
