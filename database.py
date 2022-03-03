
import mysql.connector as sqltor
db=sqltor.connect(host="localhost",user="root",passwd="amirCHAND9#2005",database="snake_game")
cc=db.cursor()




def create(p_name="unknown",point=0):
    
    
    
    stt="insert into snake_game.points values"
    stt=stt+str((0,p_name,point))
    cc.execute(stt)
    cc.execute("commit")
    

    cc.execute("select Player_Name,max(High_Scores) from snake_game.points group by  Player_Name ")
    data=cc.fetchall()
    for i in data :
        if p_name in i :
            return "Name:{}  High score:{}".format(i[0],i[1])

    

def high__score(p_name="unknown"):
    cc.execute("select Player_Name,max(High_Scores) from snake_game.points group by  Player_Name ")
    data=cc.fetchall()
    for i in data :
        if p_name in i :
            return (i[0],i[1])
        else:
            return "Player don't exist"

    


