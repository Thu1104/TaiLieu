import java.io.*;
import java.net.*;
import java.util.Scanner;

public class BinaryClient {
    public static void main(String[] args) {
        try {
            Socket s = new Socket("127.0.0.1", 3000);
            InputStream is = s.getInputStream();
            OutputStream os = s.getOutputStream();
            Scanner kb = new Scanner(System.in);
            while (true) {
                System.out.print("Nhap chuoi tu ban phim: ");
                String ch = kb.nextLine();
                //Gui chuoi qua Server
                byte inputByte[] = ch.getBytes();
                os.write(inputByte);
                if(ch.equals("exit"))
                    break;
                //Nhan ket qua tu serer
                byte b[] = new byte[1000];
                int n = is.read(b);
                String ketqua = new String(b, 0, n);
                System.out.print("Nhan duoc tu Server: "+ ketqua);
            }
            s.close();
        }
        catch (IOException e) {
            System.out.print(e);
        }
    }
}