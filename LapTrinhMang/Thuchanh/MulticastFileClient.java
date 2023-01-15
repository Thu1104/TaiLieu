import java.io.*;
import java.net.*;
import java.util.Scanner;

public class MulticastFileClient {
    public static void main(String[] args) {
        try{
            MulticastSocket ms = new MulticastSocket(9310);
            //tham gia vao nhom dia chi 228.5.6.7
            InetAddress ad = InetAddress.getByName("228.5.6.7");
            ms.joinGroup(ad);
            //nhan goi phuc vu
            byte b[] = new byte[60000];
            DatagramPacket goinhan = new DatagramPacket(b, 60000);
            ms.receive(goinhan);
            System.out.println("Da nhan duoc goi phuc vu tu server");
            //luu
            Scanner kb = new Scanner(System.in);
            System.out.print("Nhap ten file can luu: ");
            String fileluu = kb.nextLine();
            FileOutputStream f = new FileOutputStream(fileluu);
            int len = goinhan.getLength();
            f.write(b,0,len);
            f.close();
            System.out.println("Da luu file thanh cong");
            ms.close();
        }
    }
}