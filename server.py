import socket
import tkMessageBox
import Tkinter
window = Tkinter.Tk()
window.wm_withdraw()
server = socket.socket() 
server.bind(("192.168.43.160", 5000)) 
server.listen(4) 
client_socket, client_address = server.accept()
while 1==1:
    recvieved_data = client_socket.recv(1024)
    if recvieved_data is not None :
    	print(recvieved_data)
    	tkMessageBox.showinfo(title="Data Usage", message=recvieved_data)
    	client_socket.close()