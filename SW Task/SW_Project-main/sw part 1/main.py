from my_software.Software_Ingestor.data_Ingestor_Proxy import Ingestor_Proxy

processing_engine_args=['Text',"Equation.txt",False]
ingertor_args=["example.txt","Text"]
#please replace 'root','Rana@1234' with your rootname and your password for mysql server
data_sink_args=['Mysql','localhost','assets_db','root','Rana@1234']
#use this commend if you want to skip database part and just get the result 
# data_sink_args=['Raw']
my_data_ingestor=Ingestor_Proxy(ingertor_args,processing_engine_args,data_sink_args)
my_data_ingestor.send_msg()

