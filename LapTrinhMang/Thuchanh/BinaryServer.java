import java.net.*;
import java.io.*;

public class BinaryServer {
    public static void main(String[] args) {
        try {
            ServerSocket ss = new ServerSocket(3000);
            System.out.println("Da khoi tao thanh cong Server cong 3000");
            while (true) {
                Socket s = ss.accept();
                InputStream is = s.getInputStream();
                OutputStream os = s.getOutputStream();
                while (true) {
                    byte b[] = new byte[1000];
                    int n = is.read(b);
                    String ch = new String(b, 0, n);
                    if (ch.equals("exit"))
                        break;
                    String ketqua = "";
                    try{
                        int input = Integer.parseInt(ch);
                        ketqua = Integer.toBinaryString(input); 
                    } catch (NumberFormatException ex) {
                        ketqua = "Khong phai la so nguyen";
                    }
                    
                    os.write(ketqua.getBytes());
                }
                s.close();
                System.out.println("Dong noi ket cong "+ s.getPort());
            }
        }
        catch (IOException e) {
            System.out.print("Loi nhap xuat!");
        }
    }
}
