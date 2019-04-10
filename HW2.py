from tkinter import *
from tkinter import messagebox

import base64

hello = b'iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAACkUlEQVR42uyai3GDMAyGQyegGzACnaCMkBHoBhkhnSAj0A2SDaAT0E6QbEA3cOXW6XEpBtnImMv9utOllxjF/qKHLTdRSm0gdnkAAgACIAACIAACIAACIAgAARAAARAAARAAARBEAFCSJINKkpLuSTtSZbQz76W25zhKkpFWPbtaz6Q75vPuoluuPmqxlZK2yi76s9RznjlpN2K7CrFWaUAHNS0HT0Atw3YpDSjxbdoPuaziG3uk579cvIdeWsbQD7L7NAYoWpKmLy8chueO5reB7KKKrQnQJdDYn9AJZHc5QBT7enINY2hjxrqItsvJWSdxFxKuYlOlWJmE6zPPcsJuN7WFiF7me5DOAws4OyZyG6TOsr/KQziDaJm/mcy2V1V0+T0JeXxqqlrWC9mGGy3O6wwFaI0SdR+EMg9AEAACIAByqViZb+/prgFdN6qb306j3lTWs0BJ76Qjw0ktO+3ad60PQhMrfM9YwqK7lUPe4j+/OR40cDaqJeJ+xo80JsWih1WTBAcb8ysKrb+TfowQKy3v55wbBkk49FJbQusqr4snadL9hEtXC3nO1G1HG6UfxIj5oDnJlHPOVVAerWGmvYQxwc70hiTh7Bidy3/3ZFE6isxf8epNhUCl4n5ftYqWKzMP3IIquaFnquXO0sZ1yn/RWq69SuK6GdPXORfSz4HPnk1bNXO0+UZze5HqKIodNYwnHVVcOUivNcStxj4CGFYhWAWgXgmuF4JzdMhn6wDUm1DpmFyVY7IvQqeTRdod2v2F8lNn/gcpW+rUsOi9mAmFwlSo3Pw9JQ3p+8bhgnAMkPM613BxOBQqc2FEB4SmPQSAAAiAAAiAAAiAAAiAIAAEQAAEQAAEQPco3wIMADOXgFhOTghuAAAAAElFTkSuQmCC'
master = Tk()
 

def main():
    circle_size = 30
    canvas_width = 500
    canvas_height = 500
    circle_num = 0
    someLine = 0
    online = 0
    coordinate = []
    linkData = [ ]
    Guardian = False
    mouse = 0
    MX, MY = 0 , 0
    Radeon = []
    
    print('[說明]滑鼠左鍵畫線、滑鼠右鍵畫圈、滑鼠中鍵檢查')
    def mousedown( event ):
        nonlocal MX, MY, Guardian, online, mouse
        MX = event.x
        MY = event.y
        i = -1
        for space  in coordinate:
            i += 1
            if (space[0] < MX & MX < space[2]) & (space[1] < MY & MY < space[3]):
                mouse = i
                print('[動作]滑鼠點下了圓圈:',i)
       
            
    def mouseup( event ):
        nonlocal MX, MY, Guardian, online, mouse
        MX = event.x
        MY = event.y
        i = -1
        for space in coordinate:
            i += 1
            if (space[0] < MX & MX < space[2]) & (space[1] < MY & MY < space[3]):
                print('[動作]滑鼠點下了圓圈:', i,' 並和', mouse, '形成了連線')
                linkData.append( [mouse ,i])
                linkData.append( [i, mouse])
                # linkData.append( [mouse ,i])
                online += 1
            
            
        Guardian = False
    def alerted():
        print('[檢測]無窮迴圈啦')
        messagebox.showinfo('[檢測]', '[檢測]無窮迴圈啦')   

        
    def find(arr):
        # print('---',arr)
        search = []
        num = 0
        for i,j in enumerate(arr):
            if  j in search:
                num += 1
            else:
                search.append(j)
        # print(search)        
        return num
    def start( val):
        run = int(len(linkData))
        for i in range(run):
            if val == linkData[i][0]:
                return linkData[i]
    
        return []
    
    def Geforce( arr):
        run = int(len(linkData))
        if len(arr) == 0:
            return False
        for i in range(run):
            if (arr[1] == linkData[i][0]) & (arr != linkData[i]) & (arr[0] !=linkData[i][1]) :
                return linkData[i]
        
        return False
    def chance():
        nonlocal linkData,online,circle_num,Radeon
        Radeon = []
        RTXon = []
        run = int(len(linkData) * 0.5)
        for j in range(circle_num):
            # print(j)
            RTXon = start(j)
            Radeon.append([])
            for i in range( run + 1):
                if i == 0:
                    RTXon = start(j)
                    Radeon[j].append(RTXon)
                   
                else:
                    if Geforce(RTXon):
                        # print(RTXon,Geforce(RTXon))
                        RTXon = Geforce(RTXon)
                        Radeon[j].append(RTXon)  
            # print('==============================')

    def check():
        VII = 0 
        run = int(len(linkData) * 0.5)
        for k in range(run):
            # print('重複幾次: ',find(Radeon[k]))
            if( find(Radeon[k]) > VII):
                VII = find(Radeon[k])
        
        return VII
    def deep( event):
        nonlocal linkData,online,circle_num,Radeon
        print('[執行]開始執行深度檢測')
        # print( linkData)
        linkData.sort()
        chance()
   
        # print('linkData : ',linkData)
        
        # print('Radeon : ',Radeon)
        
        
        # print(VII , online, Radeon)
        print('------------------------')
        if check() > 0:
           alerted()
        else:
            linkData.sort(reverse=True)
            chance()
            if check() > 0:
                alerted()
            else:
                print('[執行]檢測未發現')
        print('------------------------')

        
    def mousemove( event ):
        nonlocal MX, MY
        canvas.create_line( MX, MY, event.x, event.y)
        MX = event.x
        MY = event.y

    def circle( event ):
        nonlocal circle_size, circle_num
        x1, y1 = ( event.x - circle_size ), ( event.y - circle_size )
        x2, y2 = ( event.x + circle_size ), ( event.y + circle_size )
        canvas.create_oval(x1, y1, x2, y2)
        canvas.create_text( (x1+x2) * 0.5, (y1+y2) * 0.5,text=circle_num)
        coordinate.append([x1, y1, x2 , y2])
        circle_num += 1
        # print([x1, y1, x2 , y2])

    
    master.title( "HW2 python" )
    # C:\Windows\System32\@WindowsHelloFaceToastIcon.png
    img = PhotoImage(data= hello) 
    master.tk.call('wm', 'iconphoto', master._w, img)

    canvas = Canvas(master,  width = canvas_width, height = canvas_height)
    canvas.pack(expand = TRUE, fill = BOTH)
    # canvas.create_image(50, 50,image = img)
    canvas.bind("<Button-1>", mousedown)
    canvas.bind("<B1-Motion>", mousemove)
    canvas.bind("<ButtonRelease-1>", mouseup)
    canvas.bind("<Button-2>", deep)
    canvas.bind("<Button-3>", circle )

    # message = Label( master, text = "Press and Drag the mouse to draw" )
    # message.pack( side = BOTTOM )
    master.mainloop()

main()