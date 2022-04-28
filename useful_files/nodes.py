class Nodes:

    def __init__(self):
        self.rightNodes = []
        self.leftNodes = []
        self.lungNodes = []

    def set_nodes(self, bodies=None):
    
        if bodies.lower() == 'right' or bodies.lower() == 'r':
            self.rightNodes = ['1.1' ,'1.2' ,'1.3' ,'1.4' ,'1.5' ,'2.1' ,'2.2' ,'3.1' ,'3.2' ,'3.3' ,'4.1' ,'4.2',
              '5.1','5.2' ,'6.1' ,'6.2' ,'7.1' ,'7.2' ,'7.3' ,'7.4' ,'7.5' ,'8.1' ,'8.2' ,'9.1' ,'9.2' ,'9.3' ,'9.4',
              '10.1','10.2' ,'11.1' ,'11.2','12.1' ,'12.2' ,'13.1' ,'13.2' ,'14.1' ,'14.2' ,'14.3' ,'15.1' ,'15.2',
              '16.1','16.2' ,'17.1' ,'17.2','18.1' ,'18.2' ,'19' ,'20.1' ,'20.2' ,'20.3' ,'20.4' ,'20.5' ,'21' ,'22',
              '23.1','23.2' ,'24.1' ,'24.2','25','26.1' ,'26.2' ,'26.3' ,'26.4' ,'26.5' ,'27' ,'28' ,'29.1' ,'29.2',
              '29.3','29.4' ,'29.5' ,'30.1','30.2','31.1' ,'31.2' ,'31.3' ,'31.4' ,'31.5' ,'31.6' ,'32.1' ,'32.2',
              '33.1','33.2' ,'33.3' ,'33.4','33.5','34.1' ,'34.2' ,'35.1' ,'35.2' ,'35.3' ,'35.4' ,'36.1' ,'36.2',
              '37.1','37.2' ,'38.1' ,'38.2','38.3' ,'38.4' ,'38.5' ,'38.6' ,'39.1' ,'39.2' ,'40.1' ,'40.2' ,'41',
              '42','43' ,'44.1' ,'44.2','45','46' ,'47' ,'48.1' ,'48.2' ,'48.3' ,'48.4' ,'48.5' ,'49.1' ,'49.2' ,'50.1',
              '50.2','50.3','50.4','50.5']
            return self.rightNodes
            
        elif bodies.lower() == 'right' or bodies.lower() == 'left':
            self.leftNodes = ['51.1' ,'51.2' ,'51.3' ,'51.4' ,'51.5' ,'52.1' ,'52.2' ,'52.3' ,'52.4',
             '52.5' ,'52.6' ,'53.1' ,'53.2' ,'54.1' ,'54.2' ,'56.1' ,'56.2' ,'56.3' ,'56.4' ,'56.5' ,'57.1' ,'57.2',
             '57.3' ,'57.4' ,'58.1' ,'58.2' ,'59.1' ,'59.2' ,'61.1' ,'61.2' ,'61.3' ,'61.4' ,'61.5' ,'61.6' ,'62.1',
             '62.2' ,'63.1' ,'63.2' ,'65.1' ,'65.2' ,'66' ,'67.1' ,'67.2' ,'67.3' ,'67.4' ,'67.5' ,'68' ,'70.1' ,'70.2',
             '71.1' ,'71.2' ,'72' ,'73.1' ,'73.2' ,'73.3' ,'73.4' ,'73.5' ,'74' ,'76.1' ,'76.2' ,'77' ,'78.1' ,'78.2',
             '78.3' ,'78.4' ,'78.5' ,'78.6' ,'80.1' ,'80.2' ,'80.3' ,'80.4' ,'80.5' ,'81.1' ,'81.2' ,'83' ,'84.1'
             ,'84.2','84.3' ,'84.4' ,'84.5' ,'84.6' ,'86.1' ,'86.2' ,'87' ,'88' ,'90.1' ,'90.2' ,'91' ,'92' ,'94.1' ,'94.2'
             ,'94.3','94.4' ,'94.5' ,'96.1' ,'96.2' ,'96.3' ,'96.4' ,'96.5']
            return self.leftNodes
            
        elif bodies.lower() == 'lr' or bodies.lower() == 'rl':
            self.lungNodes = ['1.1' ,'1.2' ,'1.3' ,'1.4' ,'1.5' ,'2.1' ,'2.2' ,'3.1' ,'3.2' ,'3.3' ,'4.1' ,'4.2',
             '5.1' ,'5.2' ,'6.1' ,'6.2' ,'7.1' ,'7.2' ,'7.3' ,'7.4' ,'7.5' ,'8.1' ,'8.2' ,'9.1' ,'9.2' ,'9.3' ,'9.4',
             '10.1' ,'10.2' ,'11.1' ,'11.2' ,'12.1' ,'12.2' ,'13.1' ,'13.2' ,'14.1' ,'14.2' ,'14.3' ,'15.1' ,'15.2',
             '16.1' ,'16.2' ,'17.1' ,'17.2' ,'18.1' ,'18.2' ,'19' ,'20.1' ,'20.2' ,'20.3' ,'20.4' ,'20.5' ,'21' ,'22',
             '23.1' ,'23.2' ,'24.1' ,'24.2' ,'25' ,'26.1' ,'26.2' ,'26.3' ,'26.4' ,'26.5' ,'27' ,'28' ,'29.1' ,'29.2',
             '29.3' ,'29.4' ,'29.5' ,'30.1' ,'30.2' ,'31.1' ,'31.2' ,'31.3' ,'31.4' ,'31.5' ,'31.6' ,'32.1' ,'32.2',
             '33.1' ,'33.2' ,'33.3' ,'33.4' ,'33.5' ,'34.1' ,'34.2' ,'35.1' ,'35.2' ,'35.3' ,'35.4' ,'36.1' ,'36.2',
             '37.1' ,'37.2' ,'38.1' ,'38.2' ,'38.3' ,'38.4' ,'38.5' ,'38.6' ,'39.1' ,'39.2' ,'40.1' ,'40.2' ,'41' ,'42',
             '43' ,'44.1' ,'44.2' ,'45' ,'46' ,'47' ,'48.1' ,'48.2' ,'48.3' ,'48.4' ,'48.5' ,'49.1' ,'49.2' ,'50.1',
             '50.2' ,'50.3' ,'50.4' ,'50.5' ,'51.1' ,'51.2' ,'51.3' ,'51.4' ,'51.5' ,'52.1' ,'52.2' ,'52.3' ,'52.4',
             '52.5' ,'52.6' ,'53.1' ,'53.2' ,'54.1' ,'54.2' ,'56.1' ,'56.2' ,'56.3' ,'56.4' ,'56.5' ,'57.1' ,'57.2',
             '57.3' ,'57.4' ,'58.1' ,'58.2' ,'59.1' ,'59.2' ,'61.1' ,'61.2' ,'61.3' ,'61.4' ,'61.5' ,'61.6' ,'62.1',
             '62.2' ,'63.1' ,'63.2' ,'65.1' ,'65.2' ,'66' ,'67.1' ,'67.2' ,'67.3' ,'67.4' ,'67.5' ,'68' ,'70.1' ,'70.2',
             '71.1' ,'71.2' ,'72' ,'73.1' ,'73.2' ,'73.3' ,'73.4' ,'73.5' ,'74' ,'76.1' ,'76.2' ,'77' ,'78.1' ,'78.2',
             '78.3' ,'78.4' ,'78.5' ,'78.6' ,'80.1' ,'80.2' ,'80.3' ,'80.4' ,'80.5' ,'81.1' ,'81.2' ,'83' ,'84.1'
             ,'84.2','84.3' ,'84.4' ,'84.5' ,'84.6' ,'86.1' ,'86.2' ,'87' ,'88' ,'90.1' ,'90.2' ,'91' ,'92' ,'94.1' ,'94.2'
             ,'94.3','94.4' ,'94.5' ,'96.1' ,'96.2' ,'96.3' ,'96.4' ,'96.5']
            return self.lungNodes
            
        elif bodies.lower() == 'lrt' or bodies.lower() == 'rlt':
            self.torsolungNodes = ['1.1' ,'1.2' ,'1.3' ,'1.4' ,'1.5' ,'2.1' ,'2.2' ,'3.1' ,'3.2' ,'3.3' ,'4.1' ,'4.2',
                 '5.1' ,'5.2' ,'6.1' ,'6.2' ,'7.1' ,'7.2' ,'7.3' ,'7.4' ,'7.5' ,'8.1' ,'8.2' ,'9.1' ,'9.2' ,'9.3' ,'9.4',
                 '10.1' ,'10.2' ,'11.1' ,'11.2' ,'12.1' ,'12.2' ,'13.1' ,'13.2' ,'14.1' ,'14.2' ,'14.3' ,'15.1' ,'15.2',
                 '16.1' ,'16.2' ,'17.1' ,'17.2' ,'18.1' ,'18.2' ,'19' ,'20.1' ,'20.2' ,'20.3' ,'20.4' ,'20.5' ,'21' ,'22',
                 '23.1' ,'23.2' ,'24.1' ,'24.2' ,'25' ,'26.1' ,'26.2' ,'26.3' ,'26.4' ,'26.5' ,'27' ,'28' ,'29.1' ,'29.2',
                 '29.3' ,'29.4' ,'29.5' ,'30.1' ,'30.2' ,'31.1' ,'31.2' ,'31.3' ,'31.4' ,'31.5' ,'31.6' ,'32.1' ,'32.2',
                 '33.1' ,'33.2' ,'33.3' ,'33.4' ,'33.5' ,'34.1' ,'34.2' ,'35.1' ,'35.2' ,'35.3' ,'35.4' ,'36.1' ,'36.2',
                 '37.1' ,'37.2' ,'38.1' ,'38.2' ,'38.3' ,'38.4' ,'38.5' ,'38.6' ,'39.1' ,'39.2' ,'40.1' ,'40.2' ,'41' ,'42',
                 '43' ,'44.1' ,'44.2' ,'45' ,'46' ,'47' ,'48.1' ,'48.2' ,'48.3' ,'48.4' ,'48.5' ,'49.1' ,'49.2' ,'50.1',
                 '50.2' ,'50.3' ,'50.4' ,'50.5' ,'51.1' ,'51.2' ,'51.3' ,'51.4' ,'51.5' ,'52.1' ,'52.2' ,'52.3' ,'52.4',
                 '52.5' ,'52.6' ,'53.1' ,'53.2' ,'54.1' ,'54.2' ,'56.1' ,'56.2' ,'56.3' ,'56.4' ,'56.5' ,'57.1' ,'57.2',
                 '57.3' ,'57.4' ,'58.1' ,'58.2' ,'59.1' ,'59.2' ,'61.1' ,'61.2' ,'61.3' ,'61.4' ,'61.5' ,'61.6' ,'62.1',
                 '62.2' ,'63.1' ,'63.2' ,'65.1' ,'65.2' ,'66' ,'67.1' ,'67.2' ,'67.3' ,'67.4' ,'67.5' ,'68' ,'70.1' ,'70.2',
                 '71.1' ,'71.2' ,'72' ,'73.1' ,'73.2' ,'73.3' ,'73.4' ,'73.5' ,'74' ,'76.1' ,'76.2' ,'77' ,'78.1' ,'78.2',
                 '78.3' ,'78.4' ,'78.5' ,'78.6' ,'80.1' ,'80.2' ,'80.3' ,'80.4' ,'80.5' ,'81.1' ,'81.2' ,'83' ,'84.1'
                 ,'84.2','84.3' ,'84.4' ,'84.5' ,'84.6' ,'86.1' ,'86.2' ,'87' ,'88' ,'90.1' ,'90.2' ,'91' ,'92' ,'94.1' ,'94.2'
                 ,'94.3','94.4' ,'94.5' ,'96.1' ,'96.2' ,'96.3' ,'96.4' ,'96.5',
                 '97','98','99', 100','101','102','103','104','105','106','107','108','109','110','111',
                 '112','113','114','115','116','117','118','119','120','121','122','123',
                 '124','125','126','127','128','129','130','131','132','133','134','135',
                 '136','137','138','139','140','141','142','143','144','145','146','147',
                 '148','149','150','151','152','153','154','155','156','157','158','159',
                 '160','161','162','163','164','165','166','167','168','169','170','171',
                 '172','173','174','175','176','177','178','179','180','181','182','183',
                 '184','185','186','187','188','189','190','191','192','193','194','195',
                 '196','197','198','199','200','201','202','203','204','205','206','207','208']
                return self.torsolungNodes
        