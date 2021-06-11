//Ricardo Longo

import java.io.PrintWriter; 
import java.net.Socket; 
import java.net.ServerSocket;

public class SocketServer { 
    public final static int port = 9999;
    
    public static void main(String[] args) {  
        //The Declarations
        PrintWriter outputStream; 
        ServerSocket serverSocket; 
          
       try  {   
           serverSocket = new ServerSocket(9999);
           while(true){
                Socket socket = serverSocket.accept();
                outputStream = new PrintWriter(socket.getOutputStream());
                // Connection made, set up streams     
                Thread Client = new ClientExecution(socket, outputStream);
                Client.start();
            } 
        }  
       catch (Exception e){    
           // If any exception occurs, display it     
           System.out.println("Error " + e);  
       } 
    }
}
