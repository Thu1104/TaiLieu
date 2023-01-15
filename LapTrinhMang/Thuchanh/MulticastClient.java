import java.io.*;
import java.net.*;
import java.util.Scanner;
public class MulticastClient {
    public static void main(String[] args) {
        try{
            MulticastSocket ms = new MulticastSocket(9310);
            InetAddress ad = InetAddress.getByName("228.5.6.7");
            ms.joinGroup(ad);
            byte b[] = new byte[64000];
            DatagramPacket goinhan = new DatagramPacket(b, 64000);
            ms.receive(goinhan);
            System.out.println("Nhap ten file can luu");
            Scanner kb = new Scanner(System.in);
            String tenfile = kb.nextLine();
            FileOutputStream f = new FileOutputStream(tenfile);
            int len = goinhan.getLength();
            f.write(b, 0, len);
            f.close();
            ms.close();
        }
    }
}
