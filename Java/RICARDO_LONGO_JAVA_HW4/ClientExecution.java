//Ricardo Longo

import java.net.*;
import java.io.*;

public class ClientExecution extends Thread 
{
  //The Declarations
  PrintWriter OutputStream;
  Socket serverSocket;
  static int Number = 0;
        
    ClientExecution(Socket socket, PrintWriter OutputPrinting)
    {
        //Constructor
        serverSocket = socket;
        OutputStream = OutputPrinting;
        Number++;
    }
        
    public void run() 
    {
        try 
        {
        OutputStream.println("Hello World " + Number);
        OutputStream.flush();
        serverSocket.close();
        return;           
        } catch (IOException e) 
        {      
        System.err.println(e);    
        }
    }
}